# First Skills

**Deep understanding. Simple methods. Honest answers.**

Portable agent skills built around first principles, clarity, and evidence—for documents, research, code, and everyday problem solving.

## Install

Install into the current project with the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add HaoTheOnly/first-skills
```

Choose a skill and agents explicitly:

```sh
npx skills add HaoTheOnly/first-skills --skill first-principles -a claude-code -a codex
```

Add `-g` to install for your user across projects. Preview available skills with `--list`.

## Codex in reusable remote environments

Install both skills globally with npm during reusable-environment preparation.
Keep skill bodies in this authoritative repository; do not vendor them into
projects or add project submodules.

Run the [preparation bootstrap](scripts/remote-codex-skills-setup.sh) as the user
who runs Codex. It installs both skills through the npm Skills CLI and adds a
managed loading block to `~/.codex/AGENTS.md` (or `$CODEX_HOME/AGENTS.md`), preserving
other instructions. The CLI version is pinned; the skill source follows this
repository's default branch at preparation time.

To avoid depending on a temporary `/workspace` file, store the bootstrap contents
in the reusable environment's preparation settings, or fetch it from a reviewed
commit of this repository during preparation. Then save and publish the reusable
environment. A script executed only in the current container does not establish
persistence across new threads. Future threads must select the published environment.

After publication, start a fresh thread in that environment. Check that both
`writing` and `first-principles` appear in skill discovery and that the global
loading block is present. Ask for a small documentation task and foundational
analysis, and verify that Codex actually reads the applicable `SKILL.md` files.
`codex debug prompt-input` can check discovery and loading instructions locally;
it does not prove that a new cloud thread inherited the published configuration.

Discovery, explicit loading, and behavior are separate checks. [Issue 7][preservation-incident]
records a failure after the skill had been read. See the official
[skill discovery][codex-skills], [AGENTS.md loading][codex-agents], and
[cloud environment][codex-cloud] documentation.

[codex-skills]: https://developers.openai.com/codex/skills/
[codex-agents]: https://developers.openai.com/codex/guides/agents-md/
[codex-cloud]: https://developers.openai.com/codex/cloud/environments/
[preservation-incident]: https://github.com/HaoTheOnly/first-skills/issues/7

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
