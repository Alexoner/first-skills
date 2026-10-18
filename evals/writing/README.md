# Writing skill smoke test

Run date: 2026-10-17 (America/Vancouver). These are initial behavioral observations, not a benchmark or evidence of reliability across agents.

## Setup

Two fresh session subagents received the same seven [requests](cases.json). One read the writing skill and any relevant local resources. The baseline did not receive the skill or repository instructions. Each answered all seven cases in a single session, with instructions to treat them independently; cases were not isolated into separate sessions.

The agents inherited the session model; its exact identifier was not recorded. These runs did not execute native Claude Code or Codex CLI. The [rubric](rubric.json) was written before examining the answers and was not supplied to either agent. Answers were manually reviewed against it. Hypothetical URLs are fixtures, not fetched sources or claims about real studies.

The execution cases used the skill's current body and local ASD-STE guide. Its description was subsequently expanded to include reporting back to the user; a separate fresh-session activation check covers that change.

## Observations

| Case | With skill | Baseline |
| --- | --- | --- |
| Keywords | Preserved “single source of truth” and “may reduce drift.” | Also preserved both. |
| Meaning | Kept the original qualified claim and explained the evidence limit. | Kept the qualified claim, changing “help” to “benefit.” |
| Ambiguity | Asked what stops and retained the original pending clarification. | Also asked what stops. |
| Structure | Led with the queue's purpose, then behavior, then configuration. | Led with worker behavior; included purpose afterward. |
| Evidence | Used the supplied findings and reference-style citation; stated the limit on error-reduction claims. | Also used the findings and a reference-style citation without inventing an error rate. |
| Single source of truth | Linked both documents to the maintained setting without copying its numeric value; used one reference definition. | Also avoided copying the value; repeated the URL in inline links. |
| Routine technical procedure | Produced four separate instructions in the supplied order. | Preserved the order in one sentence containing all four actions. |

The skill run recorded only three file reads: the skill, cases, and short local ASD-STE guide. It recorded no PDF download or web retrieval. The baseline recorded only the cases file. The full standard was downloaded separately during authoring to verify the selected rules, not during these execution tests.

Inspect [with-skill.json](with-skill.json) and [baseline.json](baseline.json) for the actual answers and recorded retrievals. Paths in these files identify the original run locations; the fixtures and results are preserved here for review.

## Reporting activation check

A separate fresh subagent received only the updated skill catalog entry and a request to report supplied work facts: a configuration key was renamed, two callers were updated, a targeted test passed, and the full suite was not run. It loaded the writing skill and local ASD-STE guide. Its answer preserved all four facts without claiming that the full suite passed. No PDF retrieval was recorded. See [report-activation.json](report-activation.json).

This checks discovery from supplied metadata in this session harness. It does not verify automatic loading in another agent product or independently establish that the hypothetical work occurred.

## Limits and reruns

One run per condition provides little evidence about stochastic failures. Tool retrievals are agent-recorded, not independently instrumented network traces. There is no token or latency comparison, formal STE assessment, or native-agent discovery test. The seven cases do not prove that every proposed meaning change will trigger clarification.

For a rerun, use fresh sessions with the same cases and tools. Give one condition the skill and keep the other free of it. Hide the rubric and previous answers until outputs are saved. Judge meaning, citations, and ordering from the outputs; inspect actual tool traces when available. Add held-out cases and native-agent runs before making stronger claims.
