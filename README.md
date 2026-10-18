# First Skills

**Deep understanding. Simple methods. Honest answers.**

Portable agent skills built around first principles, clarity, and evidence—for documents, research, code, and everyday problem solving.

## Install

Install into the current project with the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add Alexoner/first-skills
```

Choose a skill and agents explicitly:

```sh
npx skills add Alexoner/first-skills --skill first-principles -a claude-code -a codex
```

Add `-g` to install for your user across projects. Preview available skills with `--list`.

## Skills

| Skill | Use it for |
| --- | --- |
| [first-principles](skills/first-principles/SKILL.md) | Unpacking complex ideas, testing assumptions, and finding the simplest explanation or approach supported by evidence. |
| [writing](skills/writing/SKILL.md) | Evidence-based explanations and documents, with clickable references and a progression from the big picture to technical details. |

Example requests:

- “Use first-principles to explain why this process is slow.”
- “Use first-principles to simplify this proposal while preserving its assumptions and caveats.”
- “Use first-principles to assess the argument in this report.”
- “Use writing to revise this report: explain the big picture first, support claims, and link the references.”

## Principles

- **Go to the foundations.** Identify the mechanisms and constraints that explain the result.
- **Make complexity understandable.** Preserve the distinctions that affect correctness.
- **Earn confidence.** Separate evidence, inference, assumptions, and unknowns.
- **Be honest about limits.** Never invent sources, measurements, verification, or certainty.
- **Keep skills focused.** Add guidance that improves decisions; remove unnecessary ceremony.
- **Simplify before expanding.** Consider removal or consolidation before adding instructions, abstractions, tools, or process steps. Preserve the constraints that matter.

Skills follow the open [Agent Skills specification](https://agentskills.io/specification). The Skills CLI handles installation for supported agents; discovery and activation depend on the agent. Skills provide task instructions, not an always-active system prompt or a guarantee of correct output.

## Contribute

See [development.md](development.md) for authoring guidance and research references, [the core skill proposal](docs/core-skills.md) for the initial design, and [CONTRIBUTING.md](CONTRIBUTING.md) to contribute. This collection starts small and grows from demonstrated needs.

## License

[MIT](LICENSE).
