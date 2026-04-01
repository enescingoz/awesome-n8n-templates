#!/usr/bin/env python3
"""Lightweight repository contribution guardrail checks."""

from __future__ import annotations

from pathlib import Path
import sys


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    failures: list[str] = []

    required_files = [
        "CONTRIBUTING.md",
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        ".github/copilot-instructions.md",
        ".github/pull_request_template.md",
        ".github/CODEOWNERS",
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/ISSUE_TEMPLATE/template_submission.yml",
        ".github/ISSUE_TEMPLATE/content_request.yml",
        ".github/workflows/contribution-guardrails.yml",
    ]

    for rel_path in required_files:
        if not (repo_root / rel_path).exists():
            failures.append(f"Missing required file: {rel_path}")

    def read_text(rel_path: str) -> str:
        path = repo_root / rel_path
        if not path.exists():
            return ""
        return path.read_text(encoding="utf-8")

    contributing = read_text("CONTRIBUTING.md")
    if "GitHub as the live source of truth" not in contributing:
        failures.append("CONTRIBUTING.md must declare GitHub as the live source of truth.")
    if "<actor>/<type>/<scope>/<task>-<id>" not in contributing:
        failures.append("CONTRIBUTING.md must define canonical branch naming format.")
    if "Backlog" not in contributing:
        failures.append("CONTRIBUTING.md must mention Backlog milestone fallback.")

    readme = read_text("README.md")
    if "GitHub is the live source of truth" not in readme:
        failures.append("README.md must include source-of-truth language.")

    pr_template = read_text(".github/pull_request_template.md")
    if "Linked Issue" not in pr_template:
        failures.append("PR template must include a linked issue section.")
    if "validate_contribution_guardrails.py" not in pr_template:
        failures.append("PR template must include local guardrail validation checkbox.")

    codeowners = read_text(".github/CODEOWNERS").strip()
    if not codeowners:
        failures.append(".github/CODEOWNERS cannot be empty.")

    issue_form_paths = [
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/ISSUE_TEMPLATE/template_submission.yml",
        ".github/ISSUE_TEMPLATE/content_request.yml",
    ]
    for rel_path in issue_form_paths:
        content = read_text(rel_path)
        if "Backlog" not in content:
            failures.append(f"{rel_path} must reference Backlog milestone usage.")

    if failures:
        print("Contribution guardrail validation failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Contribution guardrail validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
