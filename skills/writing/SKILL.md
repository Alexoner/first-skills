---
name: writing
description: Writes or revises factual explanations, documentation, and reports with evidence, clickable references, and a clear progression from the big picture to details. Use for substantive factual prose; preserve exact quotations and requested transcriptions.
license: MIT
---

# Writing

Give the reader a clear, supported explanation they can read once, in order.

Start with the purpose, main conclusion, or system overview. Explain the essential relationships next. Introduce implementation details, exceptions, and supporting material after their context. Define an unfamiliar term before relying on it. Keep each paragraph focused and connect it to the preceding idea.

Support consequential factual claims with inspected evidence. Preserve the source's scope and uncertainty; distinguish findings from your interpretation. If support is missing, say so or remove the claim. Never invent sources or strengthen a claim to make the prose smoother.

Use clickable Markdown reference-style citations near the supported claim, with definitions collected at the end. Prefer primary sources and descriptive link labels. Check that definitions resolve to the intended source; a working link alone does not verify a claim.

Keep each maintained fact or rule in one authoritative location. Link to that source instead of copying it into several documents or skills. Identify which source governs when texts conflict. Keep necessary summaries brief and check them against the source when it changes.

For technical explanations or procedures, read [the ASD-STE100 guidance](references/asd-ste100.md). Simplify by removing repetition and unnecessary detail while preserving meaning and qualifications. Respect the requested format and scope.

Examples:

- Order: purpose of a queue → how jobs move through it → retry rules and configuration.
- Reuse: keep retry limits in the configuration reference; link there from the overview and runbook.
- Citation syntax:

  ```markdown
  ASD-STE100 addresses technical documentation. [ASD-STE100][ste]

  [ste]: https://www.asd-ste100.org/
  ```
