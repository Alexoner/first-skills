---
name: writing
description: Writes or revises evidence-based explanations, documentation, and reports with clickable reference-style links and a linear reading structure from the high-level big picture to low-level details. Use for substantive factual prose; preserve exact quotations and requested transcriptions.
license: MIT
---

# Writing

**Preserve the original meaning and keywords.** Polishing or rewording must not change the user's meaning, keywords, named principles, technical terms, or qualifications. If an edit would change meaning or keywords, or the intended meaning is unclear, explain the proposed change and clarify with the user before applying it. Keep the original wording until the user confirms. This requirement takes precedence over stylistic improvements.

**Linear reading structure: from high-level big picture to low-level details.** Start with purpose and the main conclusion or overview. Explain relationships before implementation details and exceptions. Define unfamiliar terms before using them; connect each focused paragraph to the preceding idea.

**Evidence-based.** Support consequential factual claims with inspected evidence. Preserve its scope and uncertainty. Distinguish findings from interpretation; disclose missing support. Never invent sources or strengthen claims for smoother prose.

**Clickable reference-style links.** Place Markdown references near supported claims, with definitions at the end. Prefer primary sources and descriptive labels. Check the destination and whether it supports the claim.

**Single source of truth.** Link to the authoritative fact or rule instead of duplicating it across documents or skills and causing drift. Identify the governing source when texts conflict. Check necessary summaries against it when it changes.

**Simplify; avoid bloating. Less is more when it comes to instructions.** Remove repetition and unnecessary detail while preserving meaning and qualifications.

**ASD-STE for technical details.** Read [the ASD-STE100 guidance](references/asd-ste100.md) for technical explanations or procedures. Respect the requested format and scope.

Examples:

- Order: purpose of a queue → how jobs move through it → retry rules and configuration.
- Preservation: keep “single source of truth” when polishing. Clarify with the user before replacing it with “shared guidance.”
- Citation syntax:

  ```markdown
  ASD-STE100 addresses technical documentation. [ASD-STE100][ste]

  [ste]: https://www.asd-ste100.org/
  ```
