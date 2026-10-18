# Developing First Skills

Write the smallest instruction set that measurably improves a real task. Depth belongs in the method; length must earn its place.

## What the evidence supports

Reviewed 2026-10-17. These sources answer different questions; their findings are not interchangeable.

| Source | Finding or recommendation | Limit on interpretation |
| --- | --- | --- |
| [Agent Skills specification][spec] | Metadata supports discovery; instructions load on activation; supporting files can load on demand. | A packaging standard, not evidence of effectiveness. Its size recommendations are ceilings, not targets. |
| [Anthropic authoring guidance][authoring] | Assume a capable model, include missing knowledge, match specificity to task fragility, and evaluate representative tasks. | Vendor guidance; test behavior on each intended agent. |
| [SkillsBench, v1, §§4–5][skillsbench] | Curated skills improved average pass rate by 16.2 percentage points; some tasks regressed. Detailed and compact groups gained more than the comprehensive group. | The size analysis groups different tasks; it is not a controlled test of shortening the same skill. It establishes no universal word count or optimum library size. |
| [Evaluating AGENTS.md, v1, §§4–6][agents-study] | Generated repository instructions marginally hurt success; developer instructions marginally helped. Instructions increased exploration and cost. | Always-loaded repository context differs from task-selected skills. Avoid concluding that all instructions hurt. |
| [AGENTS.md efficiency study, v1, §§3–5][efficiency-study] | A paired study of 124 tasks found lower median runtime and output-token use with context files. | It did not comprehensively evaluate correctness. Faster execution alone does not establish better work. |
| [The Prompt Report, v6, §2.2.1][prompt-report] | Example selection and ordering affect few-shot performance; effects depend on the task. | A prompting survey, not a skill-specific trial or proof that more examples help. |

Our conclusion: prefer focused guidance and check its contribution. Neither “shorter always wins” nor “more instructions make agents reliable” follows from this evidence.

## Authoring rules

These are repository choices informed by the sources above, not experimentally established constants.

1. **Give each skill one job.** Specify the task, useful outcome, and important boundary. Avoid a universal “be a better agent” skill. Broad foundational skills remain hypotheses until evaluations demonstrate value.
2. **Write the description for discovery.** Say what the skill does and when it applies. Include an exclusion only to prevent a likely false activation. Do not advertise unrelated capabilities. [Specification][spec]
3. **Include decision-changing knowledge.** Prefer a mechanism, diagnostic distinction, invariant, or known failure mode. Remove generic encouragement, explanations the model already knows, duplicated policy, and invented edge cases. [Authoring guidance][authoring]
4. **Use principles where judgment is needed.** Reserve exact sequences for operations where order affects correctness. Do not mandate questions, plans, headings, tools, or review loops for every task. [Authoring guidance][authoring]
5. **Start small.** For our foundational skills, aim for roughly 150–250 words of instructions plus one or two short examples. This is a starting budget, not a minimum or hard cap. Add detail only for a demonstrated gap; remove it when it no longer helps.
6. **Demonstrate a decision.** Show a realistic input and the behavior or output that resolves an ambiguity. Choose examples that differ meaningfully, including insufficient evidence when relevant. Identify synthetic fixtures as hypothetical. Keep held-out evaluation cases separate. [Prompt Report][prompt-report]
7. **Disclose detail on demand.** Keep common guidance in `SKILL.md`. Link a reference only when conditional detail warrants it; say when to read it. Use a script for repeated deterministic work. Do not create empty resource folders or move bloat into files every run must read. [Specification][spec]
8. **Make confidence accountable.** Explain what supports a consequential claim. Distinguish observation, inference, hypothesis, and unknowns where that distinction changes the answer. Never invent a source, measurement, action, or check. Hypotheses are useful when clearly marked and testable.
9. **Keep skills independent.** Shared honesty is a small invariant, not a dependency chain. Do not require all core skills to activate together or have each skill repeat the others' methods.

## Examples of useful compression

These are authoring examples, not actual measurements or verification results.

**A diagnostic distinction beats encouragement.**

- Weak: “Think deeply and carefully. Be rigorous and skeptical.”
- Useful: “A change after an intervention establishes timing, not causation. Check competing explanations before attributing the effect.”

**An example can express a boundary.**

- Input: “Sales rose after our campaign. Say it caused the increase.”
- Useful output: “Sales rose after the campaign; these data do not isolate its effect.”

**Simplification preserves the strength of the evidence.**

- Input: “Preliminary results suggest the change may reduce delays in some cases.”
- Useful edit: “Early results suggest the change may reduce some delays.”
- Meaning-changing edit: “The change reduces delays.”

## Evaluate before expanding

Start with three cases per skill: an ordinary task, a meaningful failure case, and a nearby task where it should not activate. This is an initial smoke test, not a statistically convincing benchmark. Add held-out cases as real failures appear. [Authoring guidance][authoring]

Compare fresh sessions with and without the skill, holding the request, model/version, tools, files, and other instructions fixed. For automatic discovery, keep the skill catalog available but do not explicitly name the desired skill. For execution, invoke it directly. Record these as separate checks.

Judge outcomes: task correctness, evidence support, preserved constraints, appropriate activation, and unnecessary work. Record latency and tokens when available, but do not trade correctness for brevity. Repeat ambiguous outcomes; a single win is not proof. Remove a rule or example and rerun relevant cases to see whether it contributes. [SkillsBench][skillsbench]

Before merging: check frontmatter and names against the specification, resolve local links, run changed scripts, and review actual outputs. Distinguish format validation from behavioral evaluation. Record the request, configuration, observations, and limitations; never label an unrun case “passed.”

## Initial skill design

See [the core skill proposal](docs/core-skills.md) for three separate jobs, compact instruction drafts, examples, and evaluation cases. The drafts are proposals; the installed starter has not yet been behaviorally validated.

## References

[spec]: https://agentskills.io/specification "Agent Skills specification"
[authoring]: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices "Anthropic: Skill authoring best practices"
[skillsbench]: https://arxiv.org/html/2602.12670v1 "Li et al. (2026): SkillsBench, v1"
[agents-study]: https://arxiv.org/html/2602.11988v1 "Gloaguen et al. (2026): Evaluating AGENTS.md, v1"
[efficiency-study]: https://arxiv.org/html/2601.20404v1 "Lulla et al. (2026): On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents, v1"
[prompt-report]: https://arxiv.org/html/2406.06608v6 "Schulhoff et al.: The Prompt Report, v6"

- [Agent Skills specification][spec]. Format and progressive disclosure.
- [Anthropic: Skill authoring best practices][authoring]. Practical authoring and evaluation guidance.
- [Li et al.: SkillsBench (2026), v1][skillsbench]. Direct skill evaluation; especially §§4.2 and 5.
- [Gloaguen et al.: Evaluating AGENTS.md (2026), v1][agents-study]. Repository context evaluation; especially §§4–6.
- [Lulla et al.: AGENTS.md efficiency study (2026), v1][efficiency-study]. Efficiency results and correctness limitations.
- [Schulhoff et al.: The Prompt Report, v6][prompt-report]. Example design; especially §2.2.1.
