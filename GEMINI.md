# GEMINI

Read and follow `CONTRIBUTING.md` first.

For non-trivial changes:
1. Reuse/create a GitHub issue.
2. Ensure a milestone is assigned (`Backlog` if no fit).
3. Create a branch before editing.

Keep process and CI lightweight for this content-focused repository.
GitHub is the live source of truth.

## CI Action Failure & Guardrail Rules

- On any CI/Action failure, extract logs via `gh run view <run_id> --log-failed`, identify root cause, and implement pre-flight prevention.
- Run `python3 .github/scripts/validate_contribution_guardrails.py` locally to verify PR metadata prior to pushing branches.
