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

## Codex in remote repositories

Codex discovers repository skills under `.agents/skills`. Install `writing` in
the target repository, then commit the installed skill and its supporting files
so a remote checkout has them without a sibling clone or a network download:

```sh
npx skills add Alexoner/first-skills --skill writing -a codex
```

Add this short loading instruction to that repository's root `AGENTS.md`:

```md
Before editing documentation or reporting results, read and apply
`.agents/skills/writing/SKILL.md`. Preserve the existing document's purpose,
conceptual altitude and authorized scope; review the complete diff for lost meaning.
```

For reproducible deployment, install from a reviewed checkout and record its
commit and file hashes alongside the deployed copy. Keep this repository as the
authoritative source; update the copy deliberately. Repository-local paths work
in remote checkouts; a symlink to a sibling clone does not unless its target is
also provisioned. Check the installed files before committing them.

Discovery and activation are different: the catalog exposes metadata, while an
explicit instruction directs the agent to read the full skill. Check the skill's
presence in `/skills` or a startup trace, then evaluate behavior on a preservation
case. A loaded skill is not proof of compliance. The failure reported in
[issue 7][preservation-incident] occurred after the skill had been read.

For user-wide CLI defaults, install with `-g` on the machine running Codex and
put the loading instruction in `~/.codex/AGENTS.md` using the installed user path.
A local installation does not configure a separate cloud container. Repository
files apply when the remote environment checks out the branch containing them;
cloud setup scripts are an alternative when installation cannot be checked in.
See the official [skill discovery][codex-skills], [AGENTS.md loading][codex-agents]
and [cloud environment][codex-cloud] documentation.

[codex-skills]: https://developers.openai.com/codex/skills/
[codex-agents]: https://developers.openai.com/codex/guides/agents-md/
[codex-cloud]: https://developers.openai.com/codex/cloud/environments/
[preservation-incident]: https://github.com/Alexoner/first-skills/issues/7

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
