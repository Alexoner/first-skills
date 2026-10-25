---
name: writing
description: Must be loaded whenever writing documentation or reporting back to the user. Produces evidence-based writing with clickable reference-style links and a linear reading structure from the high-level big picture to low-level details. Preserves original meaning, keywords, exact quotations, and requested transcriptions.
license: MIT
---

# Writing

The principle: reading experience shall be logical, linear, self-contained, minmal.

**Logical**: for problem solving solutions, always start with the purpose why, and the problem, and then introduce the high-level idea, followed by low-level details.
**self-contained**: reference, data included, easily verifiable.
**Linear**: reading must be linear experience, not back and forth jumping.

## 1. Structure

**Hierarchical top-down representation**: have separate high-level and low-level content.

**Single source of truth.** Have single place for a concept/data, link to the authoritative info instead of duplicating it across documents or within a document. Avoid causing drift and discrepancy and reconcile if any.

## 2. Methodology

**Evidence-based.** Finding evidence is first priority before writing. Never put baseless claim in the document. Distinguish findings from interpretation; disclose missing support.

## 3. Framing

**Right level of details**: Use the right level of details for writing at different altitude. For example, for wide audience abstracted writing, the internal jargons shall be summarized.

**Right set of details**: some minor details can only add distraction, in that case, you can use reference style link to the appendix. It's NOT the more details the better.

**Preserve the original meaning and keywords.** Polishing or rewording must not change the user's meaning, keywords, named principles, technical terms, or qualifications. If an edit would change meaning or keywords, or the intended meaning is unclear, explain the proposed change and clarify with the user before applying it. Keep the original wording until the user confirms. This requirement takes precedence over stylistic improvements.

**Simplify; Less is more.** avoid bloating. Remove repetition.

Examples:

- Order: purpose of a queue → how jobs move through it → retry rules and configuration.
- Preservation: keep “single source of truth” when polishing. Clarify with the user before replacing it with “shared guidance.”

## 4. Styling

**Number the sections**!

**Clickable reference-style links.** Place Markdown references near supported claims, with definitions at the end. Prefer primary sources and descriptive labels. Check the destination and whether it supports the claim.

**ASD-STE for technical details.** Use [the short local guidance](references/asd-ste100.md) for technical explanations or procedures. Respect the requested format and scope.

- Citation syntax:

  ```markdown
  ASD-STE100 addresses technical documentation. [ASD-STE100][ste]

  [ste]: https://www.asd-ste100.org/
  ```
