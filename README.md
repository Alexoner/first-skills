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

Keep this repository authoritative; do not copy skill bodies into another
repository's tracked source. A remote project can reference a reviewed commit
as a Git submodule and expose its writing skill through a relative symlink:

```sh
git submodule add https://github.com/Alexoner/first-skills.git .agents/first-skills
git -C .agents/first-skills checkout REVIEWED_COMMIT
mkdir -p .agents/skills
ln -s ../first-skills/skills/writing .agents/skills/writing
git add .gitmodules .agents/first-skills .agents/skills/writing
```

Replace `REVIEWED_COMMIT` with the chosen commit. Commit the dependency reference
and link, not copies of `SKILL.md`, its references or license. Update by reviewing
a new upstream revision and advancing the submodule pointer.

In the remote environment's setup script, initialize the dependency:

```sh
git submodule update --init --recursive .agents/first-skills
```

Add a root `AGENTS.md` instruction to read and apply
`.agents/skills/writing/SKILL.md` before documentation work or reporting. If the
file is missing, initialize the submodule before proceeding. Codex supports
symlinked skill directories; the checkout and symlink must exist in the machine
running it. Verify platform symlink support when provisioning a different host.

Check `/skills` or startup context for discovery, then evaluate actual behavior.
Discovery and explicit loading do not guarantee compliance: [issue 7][preservation-incident]
records a failure after the skill had been read. See the official
[skill discovery][codex-skills], [AGENTS.md loading][codex-agents] and
[cloud environment][codex-cloud] documentation. A user-wide CLI installation
with `-g` applies to that machine; it does not configure another cloud container.

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
