# Published studies and benchmark data for concise writing

**Use external benchmark data before drawing conclusions about the writing skill.** The relevant tasks are concise rewriting, avoiding excess output, and retaining necessary information in longer answers. They need different data and measures.

Checked 2026-10-18. Three releases below were downloaded and their actual records inspected. [sources.json](sources.json) records revisions, download URLs, checksums, schemas, and licensing notes. The [100-case native CLI comparison](run-2026-10-18/README.md) reports actual outputs and scores: reference-edit agreement improved, but the current skill did not reduce verbosity on these subsets.

## Directly useful releases

| Study and data | What is actually released | What it can test | Important limit |
| --- | --- | --- | --- |
| Stahlberg et al., [Conciseness: An Overlooked Language Task][wiki-paper] (TSAR 2022); [Wiki-Conciseness data][wiki-data] | 2,000 Wikipedia source sentences. Concise-Lite has two human rewrites per source; Concise-Full has five. Both variants use the same source sentences. | Removing wordiness while preserving sentence meaning, compared with human edits. | Sentence-level rewriting. It does not establish performance on full-document generation or preservation of user-designated keywords. |
| Borisov et al., [YapBench][yap-paper] (2026 preprint); [released prompts and baselines][yap-data] | Viewer contains 304 prompts: 60 clarification/minimal-input cases, 126 factual questions, and 118 coding/command requests. Each has a minimal-sufficient baseline and category. | Unnecessary explanations and boilerplate when a short response suffices. | Deliberately short tasks. The paper's main results have no explicit correctness gate, so an empty or wrong short answer must not be treated as a useful improvement. |
| Cortes et al., [Beyond accuracy][qa-paper] (Language Resources and Evaluation, 2026); [QA-CompletenessRelevance data][qa-data] | 106 instructional Computer Science questions; 212 human/GPT-4 answers; expert references; completeness and relevance scores averaged over four human annotators. | Calibrating an evaluator against human judgments of missing information and irrelevant content in longer answers. | Domain-specific. These ratings belong to the released answers; new answers need new assessment. Completeness and relevance do not independently establish factual correctness. |

### Data inspection

The two Wiki TSV files each contain 2,000 rows. The source columns match row for row. Lite has four fields: source, two references, and source URL. Full has seven: source, five references, and source URL. The authors release M2 edit annotations and ERRANT evaluation instructions, including edit precision, recall, and F0.5. These measures compare edits to finite references; they are not proof that every different rewrite is wrong. [Dataset documentation][wiki-data]

YapBench's complete viewer data was retrieved and checked for 304 unique IDs. Its revision-pinned Parquet file was downloaded and checksummed separately. The viewer API is not revision-pinned, so the manifest explicitly separates those checks. A dataset license was not found in the inspected release; the leaderboard's license is not assumed to cover the dataset. Raw data remains outside this repository. [Published data][yap-data]

The long-answer CSV contains 212 records for 106 question IDs: 106 human answers and 106 GPT-4 answers. The publisher's methods and author release agree on these counts and the annotation design. [Paper, §3][qa-paper] [Released files][qa-data]

## Related evidence, with different roles

- **[SummEval][summ-paper] (TACL 2021):** the [author release][summ-data] provides human judgments on 1,600 summaries from 100 news articles and 16 systems. Relevance assessment includes redundant or excess information, alongside separate consistency, fluency, and coherence ratings. This is useful for evaluating judges on document-derived outputs. It permits summarization, which differs from preserving a document's complete meaning; source articles must be reconstructed separately. The release was identified, but its full data was not downloaded in this inspection.
- **[ConCISE][concise-paper] (2025):** proposes compression-based conciseness assessment with meaning/entity checks. Its experiment expands WikiEval answers using GPT-4o and collects human judgments. [WikiEval][wikieval] is available; a release of the expanded answers and conciseness judgments was not located. Do not present the original WikiEval release as that annotated conciseness dataset.
- **[Disentangling Length from Quality in DPO][length-paper] (2024):** studies length exploitation during preference optimization. It supports separating length from quality; it does not establish that a particular writing instruction will improve outputs.

## How these data should inform the next evaluation

Start with the released task and its original records. Preserve IDs, source revisions, and reference answers. Keep references and human scores out of generation prompts. State any sampling method before observing outputs and report subset results as subsets.

Use Wiki-Conciseness for rewriting, YapBench for short-answer over-generation, and the long-answer corpus to check whether an evaluator agrees with human completeness/relevance judgments. Verify correctness, necessary coverage, meaning, and protected keywords separately from length. A shorter response earns no quality claim merely by being shorter.

For generation tests, hold the model, settings, tools, and input context fixed across skill conditions. Record the actual model/version and run each request independently. Human labels on existing answers can validate the evaluator; they cannot automatically score newly generated answers. Do not substitute self-authored examples for the published benchmark or claim sentence/short-answer scores establish long-document quality.

## References

[wiki-paper]: https://aclanthology.org/2022.tsar-1.5/ "Stahlberg et al. (2022): Conciseness: An Overlooked Language Task"
[wiki-data]: https://github.com/google-research-datasets/wiki-conciseness-dataset "Author release: Wiki-Conciseness"
[yap-paper]: https://arxiv.org/html/2601.00624v1 "Borisov et al. (2026): YapBench, v1"
[yap-data]: https://huggingface.co/datasets/tabularisai/yapbench_dataset "Author release: YapBench prompts and baselines"
[qa-paper]: https://link.springer.com/article/10.1007/s10579-026-09936-6 "Cortes et al. (2026): Beyond accuracy"
[qa-data]: https://github.com/eduardogc8/QA-CompletenessRelevance "Author release: long-answer human annotations"
[summ-paper]: https://aclanthology.org/2021.tacl-1.24/ "Fabbri et al. (2021): SummEval"
[summ-data]: https://github.com/Yale-LILY/SummEval "Author release: SummEval"
[concise-paper]: https://arxiv.org/html/2511.16846v1 "Ghafari et al. (2025): ConCISE"
[wikieval]: https://huggingface.co/datasets/explodinggradients/WikiEval "WikiEval source dataset"
[length-paper]: https://arxiv.org/abs/2403.19159 "Park et al. (2024): Disentangling Length from Quality in DPO"
