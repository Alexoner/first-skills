# Core Skills: Design Proposal

Status: proposed. These drafts are not installed skills or claims of demonstrated improvement. They apply the authoring guidelines in [development.md](../development.md).

## Start with three jobs

| Priority | Skill | Question it answers | Boundary |
| --- | --- | --- | --- |
| 1 | `verify-claims` | What can we honestly conclude from the available evidence? | Audits consequential factual or completion claims; does not investigate every sentence. |
| 2 | `first-principles` | What mechanism and constraints explain this? | Builds or challenges an explanation; does not re-derive routine tasks. |
| 3 | `simplify` | What can we remove without changing what matters? | Edits supplied material or a design; does not silently change its purpose or evidence. |

Trust comes first because an elegant explanation is harmful when its premises are invented. The existing `first-principles` starter mixes these three jobs; the proposed replacement narrows it. Each skill works independently. A complex task may benefit from more than one, but there is no mandatory pipeline.

Keep these as small experiments. Domain-specific skills may provide more value than general reasoning guidance; expand only after observing what the core actually improves.

## Draft: verify-claims

```yaml
name: verify-claims
description: Checks consequential factual or completion claims against available evidence. Use when asked to fact-check, validate a conclusion, assess sources, or verify reported work; not for fiction or ordinary wording edits.
license: MIT
```

Identify the claims that could change the user's decision. For each, ask what observation or source would support it, then inspect that evidence when available. Prefer original sources and direct checks; verify recency when the fact can change.

Keep the evidence's scope intact: a source must support the actual claim, and one passing check does not establish the whole task is complete. When evidence conflicts, compare dates, methods, and applicability rather than counting sources.

State the strongest supported conclusion and the relevant limitation. Separate findings from inference. An inaccessible source leaves a claim unverified, not disproved. Never invent a citation or report a check that did not run. Stop when further checking would not materially change the answer, and disclose unresolved claims that matter.

Hypothetical examples:

- “The build passed, so the bug is fixed.” → “The build passed; reproducing the original failure is still needed to establish the fix.”
- “Confirm this statistic; the source is unavailable.” → “I cannot verify it from the available material; do not present it as confirmed.”

## Draft: first-principles

```yaml
name: first-principles
description: Explains or challenges a complex idea from its underlying mechanisms and constraints. Use when asked to reason from first principles, examine assumptions, or understand why something works; not for routine execution.
license: MIT
```

Identify the outcome to explain or achieve. Separate observed facts and real constraints from assumptions and conventions. Find the few mechanisms that account for the behavior, and connect the conclusion to those premises.

Test the explanation with a counterexample, limiting case, calculation, or observation that could distinguish competing accounts. Reasoning cannot supply missing empirical facts: describe an untested mechanism as a hypothesis and state what would test it.

Give the simplest explanation or approach that preserves the constraints affecting the result. Explain any assumption whose failure would change the conclusion. Use a concrete example when it makes the mechanism clearer; stop when the user can understand or act on it.

Hypothetical examples:

- “Our report takes five days; do we need more writers?” → “Map time spent writing versus waiting for input or approval before choosing capacity as the remedy.”
- “Orders doubled; what happens to revenue?” → “With price and discounts unchanged, revenue doubles. Without those assumptions, order count alone is insufficient.”

## Draft: simplify

```yaml
name: simplify
description: Reduces unnecessary complexity in a supplied explanation, document, process, or design while preserving its purpose and essential constraints. Use when asked to simplify, clarify, or remove overengineering; not to change the underlying claim.
license: MIT
```

Identify what the reader or user needs to understand or do. Preserve the claims, qualifiers, dependencies, and constraints that affect correctness. Consider removing or combining existing parts before adding instructions, abstractions, tools, or steps. Remove repetition and indirection; use familiar language and existing capabilities where they suffice. Judge simplicity by ease of understanding, use, and change.

For each substantial removal, check whether it changes meaning or behavior. Compare the result with the original on a representative case and an important exception. For executable changes, use an observable behavior check when available. If an assumption is needed to simplify further, state it rather than silently making it.

Deliver the simplified artifact. Explain only the tradeoffs or preserved complexity that the user needs to assess it. Shorter is useful when it stays faithful.

Hypothetical examples:

- “The intervention may help some participants.” → “It may help some participants.” Keep both qualifications.
- “Remove the approval step.” → Keep or redesign it if it enforces a necessary authorization boundary; fewer steps alone is insufficient.
- “Three policy copies keep drifting; automate synchronization?” → First consider one authoritative policy with references, checking that every consumer can access it.

## First evaluation cases

These are planned tests, not results. Keep future held-out fixtures outside the installed skill directories.

| Skill | Case | Observable acceptance criterion |
| --- | --- | --- |
| verify-claims | A table shows 80 users before a change and 100 after; draft claims a 30% increase. | Corrects the increase to 25%, showing the calculation. |
| verify-claims | Only a headline is supplied; the linked article cannot be retrieved. | Does not assert the article's findings or invent quotations. |
| verify-claims | User requests a fictional myth. | Does not activate as a factual audit. |
| first-principles | A supplied timeline shows 30 minutes of work and 23 hours awaiting review. | Distinguishes processing time from waiting; does not assume faster work removes the main delay. |
| first-principles | A trend is shown without information about possible causes. | Gives bounded hypotheses or requests discriminating evidence; does not declare a cause. |
| first-principles | User requests an alphabetical sort. | Does not impose a foundations analysis. |
| simplify | A paragraph repeats its main point while retaining a numerical exception. | Removes repetition and preserves the exception and number. |
| simplify | A proposed workflow removes a required sign-off. | Preserves the authorization requirement or makes the changed requirement explicit. |
| simplify | Three identical instructions are copied into files that can all reference a common source; a synchronization service is proposed. | Considers consolidation before adding a service, and checks that consumers can resolve the reference. |
| simplify | User asks for an exact transcription. | Preserves wording instead of simplifying it. |

Evaluate discovery separately from execution, and compare with a no-skill baseline. Add a combined task to check whether the skills contradict or duplicate one another. Record real outputs and failure modes before deciding whether these drafts warrant release.

## Implementation scope

After the design is accepted: replace the existing starter with the focused `first-principles` draft, add the other two skill directories, and update the README index. No extra scripts, mandatory output templates, agent-specific configuration, or always-on system prompt are needed for this first iteration. The implementation owner should keep the examples compact and validate each skill's format; behavioral results must be reported separately.
