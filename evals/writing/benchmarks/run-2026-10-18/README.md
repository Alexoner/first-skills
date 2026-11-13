# Writing skill: published benchmark results

**The current skill did not reduce verbosity in this sampled test.** It improved agreement with human sentence edits, but produced longer answers without a clear long-answer completeness gain. The skill remains unchanged.

This is a native Codex CLI comparison using `gpt-6.1-sol`: 100 external benchmark inputs, two conditions, 200 generated responses. [Recorded results][summary]

## Results

| Published dataset | Cases | Mean words: baseline | Mean words: writing skill | Change |
| --- | ---: | ---: | ---: | ---: |
| [Wiki-Conciseness][wiki] | 50 | 19.46 | 19.96 | +2.6% |
| [YapBench][yap] | 30 | 9.47 | 10.10 | +6.7% |
| [QA-CompletenessRelevance][qa] | 20 | 165.20 | 190.40 | +15.3% |

Quality and task-specific scores give a more qualified result:

- **Wiki:** official ERRANT Full F0.5 improved **0.2523 → 0.3037**; Lite improved **0.1498 → 0.1812**. Both blinded judge passes accepted fidelity for **44/50 → 47/50** outputs. The passes disagreed on 3 baseline and 2 skill outputs. Reference-edit agreement and LLM judgments are separate measures, neither a proof of complete meaning preservation.
- **Yap:** the sampled Yap-style excess-character index increased **24.5 → 26.0**; lower is better. Its paired 95% bootstrap interval for the change was **−2.5 to +15.83**, so this does not establish a consistent increase either. Both passes accepted sufficiency for **28/30 → 29/30**, with no pass disagreement.
- **Long answers:** mean length increased **25.2 words**, with paired 95% interval **+16.3 to +35.05**. Judge-rated completeness changed **95.68 → 95.98/100**; the interval for that change was **−2.25 to +2.35**. Relevance changed **99.13 → 99.28/100**, but its evaluator calibration is weak. These results do not establish a quality benefit from the additional text. [Scores and intervals][summary]

A concrete failure persists in both conditions: `wiki-1889` omits the source's conference total of **11 teams**. The skill's preservation instruction did not prevent that loss. Some strict judge flags are more debatable, such as treating omission of “New York” after “New York City” as a loss. Inspect the [outputs][outputs] and [judgments][judgments] rather than treating every judge label as ground truth.

## Evaluator reliability

On **40 original human-rated answers from 20 separate questions**, the same judge's Spearman correlation with published human scores was **0.657 for completeness** and **0.308 for relevance**. Mean absolute errors were **16.09** and **17.71** points. The questions were excluded from generation, and human scores were withheld from the judge. Relevance agreement is weak; generated-answer relevance scores also approach the scale ceiling. They cannot establish that the skill avoids bloat. [Human/judge comparisons][calibration]

## Method

The [protocol][protocol] fixes the sample, seed, input hashes, conditions, model, and measures. It was written before generation and committed before generation finished and before scoring. Every input has one fresh ephemeral session per condition, with low reasoning and provider sampling defaults. Requests are identical across conditions; call order is randomized.

Baseline uses a neutral assistant instruction. The treatment adds the unchanged writing skill and its short ASD-STE reference to that instruction. The full PDF is absent. User configuration, project documents, and discovered installed skills are disabled. All **248 benchmark calls** (200 generation, 48 judge) completed with **zero tool calls**, including PDF/web retrieval. [Runtime audit][validation]

References and ratings are excluded from generation. Anonymous X/Y candidates receive two judge passes with reversed ordering, five cases per session, medium reasoning, and no skill. The judge shares the generator's model family. Calibration batches were checked separately against human labels. No outputs or ratings were regenerated to select better results.

ERRANT uses the released Lite/Full M2 gold annotations and published source tokens. Target tokenization uses spaCy 3.8.16 and `en_core_web_sm` 3.8.0; modern source tokenization differs on `wiki-1121`. Yap requests use an XML wrapper; its length normalization removes code-fence delimiter lines, backticks, bold markers, and heading markers. These subset adaptations must not be compared directly with published full-set leaderboards. Bootstrap intervals use 2,000 paired case resamples, stratified by category for Yap; they do not measure repeated-generation variability. [Scoring implementation][scorer]

## Reproduce and inspect

[Sources and revisions][sources], [download checksums][receipts], [all 200 responses][outputs], [all 440 judge ratings][judgments], [label mapping][mapping], and [official ERRANT logs][logs] are archived. Raw source datasets remain outside the repository.

From this directory, use Python 3.12 and an authenticated Codex CLI. Scoring requires `errant==3.0.2`, `spacy==3.8.16`, `en_core_web_sm==3.8.0`, and `scipy==1.17.0` in an environment whose `python` runs those packages:

```sh
python3 ../evaluate.py fetch --data-dir /tmp/writing-data
python3 ../evaluate.py prepare --data-dir /tmp/writing-data --run-dir /tmp/writing-eval
python3 ../evaluate.py generate --data-dir /tmp/writing-data --run-dir /tmp/writing-eval
python3 ../evaluate.py judge --data-dir /tmp/writing-data --run-dir /tmp/writing-eval
python ../score.py --data-dir /tmp/writing-data --run-dir /tmp/writing-eval
```

A fresh download reproduced all 100 selected input hashes, both condition hashes, and the 40 calibration answers. Regeneration is stochastic; the model identifier is an alias, not a verified immutable snapshot. New generations are new observations.

This tests explicit instruction injection on subsets, with one model and one generation per condition/input. It does not establish full-document performance, automatic skill discovery, user-designated keyword preservation, citation validity, single-source-of-truth behavior, or cross-agent effectiveness. Public benchmarks may also occur in model training data.

[summary]: summary.json
[outputs]: outputs.json
[judgments]: judgments.json
[calibration]: calibration.json
[protocol]: protocol.json
[validation]: validation.json
[receipts]: source-receipts.json
[mapping]: judge-mapping.json
[logs]: errant/
[scorer]: ../score.py
[sources]: ../README.md
[wiki]: https://github.com/google-research-datasets/wiki-conciseness-dataset
[yap]: https://huggingface.co/datasets/tabularisai/yapbench_dataset
[qa]: https://github.com/eduardogc8/QA-CompletenessRelevance
