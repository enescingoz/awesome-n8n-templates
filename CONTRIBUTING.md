# CONTRIBUTING

Thanks for helping improve this repository of n8n templates.

This is a lightweight content repo. Keep process and automation practical:
- prefer small, focused pull requests
- avoid introducing heavy CI or policy overhead
- preserve upstream usability for template contributors

## Canonical Workflow

Use GitHub as the live source of truth for:
- issues and milestones
- pull requests and review state
- workflow/check run status
- releases

If markdown notes and GitHub disagree, GitHub wins.

For non-trivial changes:
1. Find an existing issue or open a new one.
2. Ensure the issue has a milestone.
3. Use `Backlog` when no thematic milestone fits.
4. Create a branch before editing.

Canonical branch format:

```text
<actor>/<type>/<scope>/<task>-<id>
```

Examples:
- `codex/chore/shared/lightweight-repo-contribution-workflow-1`
- `user/docs/readme/add-telegram-links-42`

## Shorthand Prompts

- `start <task>`: issue + milestone + branch, then begin work
- `record it`: commit current changes
- `publish it`: push current branch
- `propose it`: open or update the PR
- `land it`: squash-merge the PR after checks + approval
- `ship it`: commit + push + PR
- `finish it`: commit + push + PR + merge
- `finish it for #<id>`: full-flow shorthand tied to an issue

## Scope Guardrails

- This repo mainly stores templates and metadata content.
- Keep CI checks lightweight and fast.
- Do not add heavyweight test matrices or strict gating unless clearly necessary.
- Keep naming and category changes consistent with existing structure.

## PR Expectations

Every PR should include:
- linked issue (`Closes #...` or `Refs #...`)
- short summary of what changed
- quick validation notes (what was checked locally)
- note if any files were moved/renamed

## Local Validation

Run lightweight checks before opening a PR:

```bash
python .github/scripts/validate_contribution_guardrails.py
```
