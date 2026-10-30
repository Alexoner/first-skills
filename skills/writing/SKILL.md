---
name: writing
description: Must be loaded whenever writing documentation or reporting back to the user. Produces evidence-based writing with clickable reference-style links and a linear reading structure from the high-level big picture to low-level details. Preserves original meaning, keywords, exact quotations, and requested transcriptions.
license: MIT
---

# Writing

Purpose of writing: **The writing should make it easy for people to read and understand the information, NOT to dump your brain memory.**

The principle: reading experience shall be logical, linear, succinct, self-contained, minmal-effort.

**Logical**: for problem solving solutions, always start with the purpose why, and the problem, and then introduce the high-level idea, followed by low-level details.
**self-contained**: reference, data included, easily verifiable.
**Linear**: reading must be linear experience, not back and forth jumping.

**DO NOT REPEAT YOURSELF**: redundancy is a **DEFECT**, which undermines creditability and makes the writing hard to be reviewed. Writing is for people to read. If people can't read it, it's pointless.
By repeating yourself over and over and being verbose, you kill the reading intent of people.
Have single source of truth, instead of duplicating it across documents or within a document. Avoid causing drift and discrepancy and reconcile if any.
If your doc is hard to read, due to verbosity, bad formating, confusing words, then this whole doc is worthless as no one will read it.

## 1. Structure

**Hierarchical top-down representation**: have separate high-level and low-level content.

**COHERENT**: content must form logical connection, organized structurally.

**DO NOT add your INNER MONOLOGUE**: DO NOT add the user's instruction or your "editorial thinking" on how to write this document. That's distraction. The doucment should focus on the original topic, not "HOW TO DO PROPER WRITING".

**Separate the main focus and reference like minor details, past related but discarded approach**: Appendix is a very good place for these supplementary content that isn't required to convey the message of the doc, but for the sake of completeness the information can be organized there as "REFERENCE".

## 2. Evidence-based

**Be precise**: verified accurate numbers > qualitative description. When adding details with numbers, you must make sure it serves the purpose of doc, and be extremely cautious not to introduce factual mistake.
**Evidence-based.** Finding evidence is first priority before writing. Never put baseless claim in the document. Distinguish findings from interpretation; disclose missing support.

## 3. Succinct and altitude

**Critical information be highlighted**: for high-level writing, the critical information must be explicit, and not buried by minor details. Pay extra attention to diagram labeling, title, bullet points, ...

**Right level of details**: Use the right level of details for writing at different altitude. For example, for wide audience abstracted writing, the internal jargons shall be summarized.

**Right set of details**: some minor details can only add distraction, in that case, you can use reference style link to the appendix. It's NOT the more details the better. By having irrelavant or unnecessary minor details, you make it easy to introduce factual mistakes in data.

**Less is more**: remember what's the *most important* information that has to be delivered to the reader? can you do that while demanding less reading from the readers?

Bad example:

```
Parent EVALUATE assesses the combined outcome against the parent’s acceptance conditions; parent PLAN uses those findings to decide what remains. Completed or passing children alone do not establish parent completion.
```

Reason: evaluate is done against the accentance critiera is already covered above in the same doc, and here the critical info is that recursive child is fed to parent, which will make decisions.

Good Example:

```
Parent EVALUATE assesses the combined outcome and decides what remains.
```

**Preserve the original meaning and keywords.** Polishing or rewording must not change the user's meaning, keywords, named principles, technical terms, or qualifications. If an edit would change meaning or keywords, or the intended meaning is unclear, explain the proposed change and clarify with the user before applying it. Keep the original wording until the user confirms. This requirement takes precedence over stylistic improvements.

**Simplify**: make the document easy to understand, not overwhelmed with jargons that make no logical sense. True understanding means simple words are enough.

Examples:

- Order: purpose of a queue → how jobs move through it → retry rules and configuration.
- Preservation: keep “single source of truth” when polishing. Clarify with the user before replacing it with “shared guidance.”

## 4. Styling

**Number the sections**!

**Save words**: for example, "make choices" is bad, just use simple verb term "choose".

**Clickable reference-style links.** Place Markdown references near supported claims, with definitions at the end. Prefer primary sources and descriptive labels. Check the destination and whether it supports the claim.
But DO NOT add excessive links when the source is right close to the usage.

**ASD-STE for technical details.** Use [the short local guidance](references/asd-ste100.md) for technical explanations or procedures. Respect the requested format and scope.

- Citation syntax:

  ```markdown
  ASD-STE100 addresses technical documentation. [ASD-STE100][ste]

  [ste]: https://www.asd-ste100.org/
  ```
