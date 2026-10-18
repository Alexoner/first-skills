# Concision instruction ablation

**Decision: keep the current writing skill unchanged.** This pilot found no additional redundancy-removal or fidelity benefit from either “be concise” or an explicit deletion rule. The result does not establish that extra guidance never helps.

## Results

Run date: 2026-10-18. Each condition produced 18 answers: six distinct drafts across three fresh runs.

| Condition | Required meaning and keywords preserved | No unnecessary repeated ideas | Mean output words |
| --- | --- | --- | --- |
| Current writing skill | 18/18 | 18/18 | 27.17 |
| Current skill + “Be concise.” | 18/18 | 18/18 | 27.11 |
| Current skill + explicit deletion rule | 18/18 | 18/18 | 26.83 |

Both reviewers assigned these outcomes and agreed on all 54 answers. The explicit rule saved six words across its 18 outputs compared with the current skill, or 0.33 words per answer. Word count alone does not establish usefulness, and no improvement appeared on the two quality criteria.

## What was tested

The hypothesis was that a targeted deletion instruction would remove more unnecessary repetition while preserving meaning, keywords, evidence, and qualifications.

The added instruction was:

> Remove sentences that repeat information already stated or contribute nothing needed for the request. Preserve meaning, keywords, evidence, and qualifications. If preservation is uncertain, retain the original.

The [six drafts](cases.json) covered a repetitive status report, protected keywords, an already-concise sentence, a policy with an emergency exception, a finding with evidence limits and a citation, and two standalone maintenance checklists. The repeated prerequisites in the last case were necessary because the checklists would be printed separately.

## Method

All conditions used the same skill at commit `f5b1038`, requests, drafts, and inherited session-agent configuration. Three fresh session subagents ran each condition. Each session handled all six cases and received no rubric or previous answers. Conditions differed only in the added instruction and their input/output paths.

The criteria and decision rule were written before outputs were examined. The [protocol](protocol.json) records the skill and local-guide hashes, conditions, and criteria. Outputs were shuffled and stripped of condition/run labels before two fresh LLM reviewers assessed fidelity and unnecessary repetition separately. They received the original requests and drafts. The root agent inspected the first repetition from each condition and the reviewers' noted equivalence case.

The [results](results.json) preserve every answer, reviewer rating, and recorded retrieval. Word counts use whitespace-separated units in the complete Markdown answer, including citation syntax and definitions. No cost or token-saving claim is made.

## Limits

This is a small, synthetic editing pilot. The six drafts share examples and concepts with the skill; they are not an independently curated benchmark. All conditions performed well, leaving little room to distinguish them. Longer real documents could expose failures absent here.

The same six drafts recur across runs, and six cases share each session. The 54 answers are not 54 independent documents. The exact model identifier, seeds, and generation parameters were not recorded. Native Claude Code and Codex CLI were not exercised. LLM reviewers can share blind spots; their agreement is not a substitute for human validation. No statistical equivalence or general reliability conclusion follows.

## Research context

[Length bias research][length] motivates separating quality from response length. [ConCISE][concise] proposes measuring removable content while checking meaning preservation. Neither validates this particular added instruction; the experiment above tests its incremental contribution in a narrow setting.

[length]: https://arxiv.org/abs/2403.19159 "Park et al.: Disentangling Length from Quality in Direct Preference Optimization"
[concise]: https://arxiv.org/html/2511.16846v1 "Ghafari et al.: ConCISE"
