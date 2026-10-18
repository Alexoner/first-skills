# Contributing

Propose skills that turn deep understanding into clear, reliable practice across documents, research, code, and other domains.

Read [development.md](development.md) for research-backed authoring guidance, examples, and the evaluation approach.

## Add or change a skill

1. Identify a concrete task and the decisions the skill should improve.
2. Create `skills/<skill-name>/SKILL.md` with YAML `name` and `description` fields. Match the name to the directory and use lowercase letters, digits, and hyphens.
3. Describe when the skill applies. Keep instructions concise and specific enough to guide useful decisions.
4. Add scripts, references, or assets only when they serve a real need. Link supporting references from the skill and keep dependencies explicit.
5. Try realistic requests, including a case with missing or contradictory evidence. Record the agent and version, request, observed behavior, and limitations in your pull request. Do not claim checks you did not run.

Follow the [Agent Skills specification](https://agentskills.io/specification). Keep the core portable; document any agent-specific behavior.

## Review criteria

- Does the skill capture a useful mechanism or method beyond generic advice?
- Does simplification preserve relevant constraints and uncertainty?
- Can the agent distinguish evidence from inference and unsupported claims?
- Are sources, scripts, and examples accurate and attributable?
- Does the skill respect the user's scope and existing authorization?

Keep private data and credentials out of contributions. Attribute external material and confirm its license permits redistribution.
