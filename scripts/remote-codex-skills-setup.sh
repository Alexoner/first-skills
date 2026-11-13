#!/usr/bin/env bash
set -euo pipefail

# Run during reusable-environment preparation, as the user who runs Codex.
npx --yes skills@1.8.1 add HaoTheOnly/first-skills \
  --skill writing first-principles --agent codex --global --yes

python3 - <<'PY'
import os
from pathlib import Path
home = Path.home()
root = Path(os.environ.get('CODEX_HOME', home / '.codex'))
root.mkdir(parents=True, exist_ok=True)
path = root / 'AGENTS.md'
start = '<!-- first-skills:begin -->'
end = '<!-- first-skills:end -->'
block = f'''{start}
## First Skills

Before writing documentation or reporting results, read and apply
`{home}/.agents/skills/writing/SKILL.md` and its relevant linked references.
For foundational analysis, testing assumptions, or simplifying complex ideas,
read and apply `{home}/.agents/skills/first-principles/SKILL.md`.
If either skill is missing, rerun the reusable environment's npm preparation.
Preserve the user's authorized scope and the original document's meaning.
{end}'''
text = path.read_text() if path.exists() else ''
if start in text:
    if text.count(start) != 1 or text.count(end) != 1 or text.index(end) < text.index(start):
        raise SystemExit('Malformed first-skills instruction block; refusing to overwrite')
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    text = before + block + after
else:
    if end in text:
        raise SystemExit('Unmatched first-skills end marker')
    text = text.rstrip() + ('\n\n' if text.strip() else '') + block + '\n'
path.write_text(text)
for name in ('writing', 'first-principles'):
    skill = home / '.agents/skills' / name / 'SKILL.md'
    if not skill.is_file():
        raise SystemExit(f'Missing installed skill: {skill}')
print(f'Installed both skills and loading instructions: {path}')
PY
