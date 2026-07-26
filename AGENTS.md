# AGENTS

Use `CONTRIBUTING.md` as the canonical workflow contract.

## Repo Profile

- Type: lightweight content/fork repository
- Primary artifacts: n8n template JSON files and indexing docs
- Policy posture: minimal process, practical guardrails

## Required Flow

1. Work from a branch (never directly on `main` for non-trivial tasks).
2. Tie non-trivial work to a GitHub issue with a milestone.
3. Use `Backlog` when no thematic milestone applies.
4. Keep CI and policy additions lightweight.

## Source Of Truth

GitHub is the live source of truth for issue state, milestones, PR status, and checks.

## CI Action Failure & Guardrail Rules

- On any CI/Action failure, extract logs via `gh run view <run_id> --log-failed`, identify root cause, and implement pre-flight prevention.
- Run `python3 .github/scripts/validate_contribution_guardrails.py` locally to verify PR metadata prior to pushing branches.
