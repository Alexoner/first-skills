"""Score the recorded run. Requires ERRANT 3.0.2, spaCy/en_core_web_sm, SciPy.

Usage: python score.py --data-dir DIR --run-dir DIR
"""
import argparse
import collections
import hashlib
import json
import pathlib
import random
import re
import statistics
import subprocess


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def mean(values):
    return statistics.mean(values)


def paired_ci(pairs, statistic, rounds=2000):
    rng = random.Random(20261018)
    draws = sorted(statistic([rng.choice(pairs) for _ in pairs]) for _ in range(rounds))
    return [round(draws[int(rounds * .025)], 4), round(draws[int(rounds * .975)], 4)]


def visible(text):
    # Explicit Yap-style adaptation, not an assertion of upstream byte identity.
    text = re.sub(r"(?m)^```[^\n]*\n?|^```\s*$", "", text)
    text = text.replace("`", "").replace("**", "")
    return re.sub(r"(?m)^#{1,6}\s+", "", text).strip()


def main(data, run):
    import spacy
    import errant
    from scipy.stats import spearmanr
    cases = json.loads((run / "cases-private.json").read_text())
    outputs = json.loads((run / "outputs.json").read_text())
    assert len(outputs) == 200
    indexed = {(r["id"], r["condition"]): r for r in outputs}
    assert len(indexed) == 200 and all(r["tool_calls"] == 0 for r in outputs)
    judgments = json.loads((run / "judgments.json").read_text())
    assert len(judgments) == 48
    mapping = json.loads((run / "judge-mapping.json").read_text())
    ratings = collections.defaultdict(list)
    cal_ratings = {}
    for batch in judgments:
        for r in batch["ratings"]:
            if batch["pass_id"] == 0:
                cal_ratings[r["id"]] = r
            else:
                condition = mapping[f"{batch['pass_id']}:{r['id']}:{r['candidate']}"]
                ratings[r["id"], condition].append(r)
    assert len(ratings) == 200 and all(len(r) == 2 for r in ratings.values())
    results = {"model_requested": "gpt-6.1-sol", "generation_calls": 200, "judge_calls": 48,
               "tool_calls": sum(r["tool_calls"] for r in outputs + judgments),
               "sampling": "Fixed subsets, one generation per condition/case; confidence intervals reflect case resampling only, not repeated-generation variability.", "datasets": {}}
    for dataset in ["wiki", "yap", "qa"]:
        subset = [c for c in cases if c["dataset"] == dataset]
        pairs = [tuple(len(indexed[c['id'], k]["answer"].split()) for k in ["baseline", "writing"]) for c in subset]
        stats = {"n":len(subset), "mean_words": {k:round(mean(p[i] for p in pairs), 3) for i,k in enumerate(["baseline", "writing"])},
                 "word_change_percent": round((sum(p[1] for p in pairs)/sum(p[0] for p in pairs)-1)*100, 3),
                 "paired_mean_word_delta_ci95": paired_ci(pairs, lambda sample:mean(b-a for a,b in sample))}
        if dataset in ["wiki", "yap"]:
            field = "fidelity" if dataset == "wiki" else "sufficient"
            stats["both_judge_passes_accept"] = {k:sum(all(r[field] is True for r in ratings[c['id'],k]) for c in subset) for k in ["baseline", "writing"]}
            stats["judge_pass_disagreements"] = {k:sum(ratings[c['id'],k][0][field] != ratings[c['id'],k][1][field] for c in subset) for k in ["baseline", "writing"]}
        if dataset == "yap":
            medians = {}
            for condition in ["baseline", "writing"]:
                medians[condition] = {cat:statistics.median(max(0, len(visible(indexed[c['id'],condition]['answer']))-len(visible(c['references'][0]))) for c in subset if c['category']==cat) for cat in 'ABC'}
            stats["yap_style_category_medians_excess_characters"] = medians
            stats["yap_style_index"] = {k:round(mean(v.values()),3) for k,v in medians.items()}
            def delta(sample):
                return mean(statistics.median(max(0,len(visible(indexed[c['id'],'writing']['answer']))-len(visible(c['references'][0]))) for c in sample if c['category']==cat)-statistics.median(max(0,len(visible(indexed[c['id'],'baseline']['answer']))-len(visible(c['references'][0]))) for c in sample if c['category']==cat) for cat in 'ABC')
            rng=random.Random(20261018)
            draws=[]
            for _ in range(2000):
                sampled=[]
                for cat in 'ABC':
                    group=[c for c in subset if c['category']==cat]
                    sampled.extend(rng.choices(group,k=len(group)))
                draws.append(delta(sampled))
            draws.sort()
            stats['yap_style_index_delta_ci95']=[round(draws[50],3),round(draws[1950],3)]
        if dataset == "qa":
            for field in ["completeness", "relevance"]:
                score_pairs=[tuple(mean(r[field] for r in ratings[c['id'],k]) for k in ['baseline','writing']) for c in subset]
                stats[field] = {k:round(mean(p[i] for p in score_pairs),3) for i,k in enumerate(['baseline','writing'])}
                stats[field]['paired_delta_ci95']=paired_ci(score_pairs,lambda sample:mean(b-a for a,b in sample))
                stats[field]['mean_absolute_pass_disagreement']={k:round(mean(abs(ratings[c['id'],k][0][field]-ratings[c['id'],k][1][field]) for c in subset),3) for k in ['baseline','writing']}
            stats['both_passes_find_no_apparent_factual_error']={k:sum(all(r['correctness'] is True for r in ratings[c['id'],k]) for c in subset) for k in ['baseline','writing']}
        results["datasets"][dataset]=stats
    calibration=json.loads((run/'calibration-private.json').read_text())
    assert len(cal_ratings)==len(calibration)==40
    results['judge_calibration']={'answers':40,'disjoint_questions':20}
    for field in ['completeness','relevance']:
        human=[float(r[field]) for r in calibration]
        model=[cal_ratings[r['question_id']+'-'+r['answer_source']][field] for r in calibration]
        rho=spearmanr(human,model)
        results['judge_calibration'][field]={'spearman_rho':round(float(rho.statistic),4),'mean_absolute_error':round(mean(abs(a-b) for a,b in zip(human,model)),3)}
    # Native official edit scoring; reuse published gold annotations verbatim.
    nlp=spacy.load('en_core_web_sm')
    wiki=[c for c in cases if c['dataset']=='wiki']
    scoring=run/'errant'; scoring.mkdir(exist_ok=True)
    tokenize=lambda text:' '.join(t.text for t in nlp(text.strip()))
    orig=None
    tokenizer_mismatches=[]
    for variant in ['full','lite']:
        raw=(data/f'concise_{variant}.m2').read_text()
        blocks=raw.strip().split('\n\n')
        assert len(blocks)==2000
        selected=[blocks[c['source_index']] for c in wiki]
        gold_orig=[b.splitlines()[0][2:] for b in selected]
        assert all(re.sub(r'\s','',s)==re.sub(r'\s','',c['source']) for s,c in zip(gold_orig,wiki)), 'Gold/source content mismatch'
        if orig is None:
            orig=gold_orig
            tokenizer_mismatches=[c['id'] for c,s in zip(wiki,orig) if tokenize(c['source'])!=s]
        else:
            assert gold_orig==orig, 'Lite/Full gold sources differ'
        (scoring/f'{variant}.m2').write_text('\n\n'.join(selected)+'\n\n')
    (scoring/'source.txt').write_text('\n'.join(orig)+'\n')
    tool=pathlib.Path(__import__('sys').executable).parent
    scores={}
    for condition in ['baseline','writing']:
        target=[tokenize(indexed[c['id'],condition]['answer'].replace('\n',' ')) for c in wiki]
        (scoring/f'{condition}.txt').write_text('\n'.join(target)+'\n')
        subprocess.run([str(tool/'errant_parallel'),'-orig',str(scoring/'source.txt'),'-cor',str(scoring/f'{condition}.txt'),'-out',str(scoring/f'{condition}.m2')],check=True,capture_output=True,text=True)
        scores[condition]={}
        for variant in ['full','lite']:
            result=subprocess.run([str(tool/'errant_compare'),'-hyp',str(scoring/f'{condition}.m2'),'-ref',str(scoring/f'{variant}.m2')],check=True,capture_output=True,text=True)
            (scoring/f'{condition}-{variant}.log').write_text(result.stdout.rstrip()+'\n')
            line=next(line for line in result.stdout.splitlines() if re.match(r'^\d+\s+\d+\s+\d+\s',line))
            values=line.split()
            scores[condition][variant]=dict(zip(['TP','FP','FN','precision','recall','F0.5'],[int(x) for x in values[:3]]+[float(x) for x in values[3:6]]))
    results['datasets']['wiki']['ERRANT']=scores
    results['ERRANT_versions']={'errant':errant.__version__,'spacy':spacy.__version__,'en_core_web_sm':nlp.meta['version']}
    results['ERRANT_tokenization']={'source':'Published M2 source tokens, verified to match TSV content ignoring whitespace','target':'en_core_web_sm 3.8.0 tokenization, newlines replaced with spaces','modern_source_tokenizer_mismatch_ids':tokenizer_mismatches,'limit':'Modern tokenizer differs from published source segmentation on these cases; do not compare subset scores to published full-set leaderboard values.'}
    results['gold_m2_sha256']={v:hashlib.sha256((data/f'concise_{v}.m2').read_bytes()).hexdigest() for v in ['full','lite']}
    write(run/'summary.json',results)
    print(json.dumps(results,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--data-dir',type=pathlib.Path,required=True)
    parser.add_argument('--run-dir',type=pathlib.Path,required=True)
    args=parser.parse_args()
    main(args.data_dir,args.run_dir)
