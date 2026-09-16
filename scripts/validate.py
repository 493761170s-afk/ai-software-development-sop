#!/usr/bin/env python3
"""Validate the public AI Software Development SOP repository.

Uses only the Python standard library so contributors and CI can run it without
installing project dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

INSTALL_PATHS = [
    "SKILL.md",
    "docs/QUICK_START.md",
    *[f"stages/{n:02d}-{slug}/SKILL.md" for n, slug in [
        (1, "project-definition"),
        (2, "requirements-engineering"),
        (3, "product-experience-design"),
        (4, "technical-design"),
        (5, "development-planning"),
        (6, "development-execution"),
        (7, "integration-verification"),
        (8, "acceptance-release"),
    ]],
    "utilities/independent-pre-coding-review/SKILL.md",
    "utilities/change-control/SKILL.md",
    "utilities/incident-hotfix/SKILL.md",
    "utilities/requirement-traceability/SKILL.md",
    "utilities/root-cause-debug/SKILL.md",
    "references/adoption-level-matrix.md",
    "references/decision-rights.md",
    "references/executor-model.md",
    "references/experiment-promotion.md",
    "references/profile-overlay.md",
    "references/reviewer-provenance.md",
    "references/review-validity.md",
    "references/spec-kit-integration.md",
    "references/tracker-governance.md",
    "references/verification-change-control.md",
    "templates/PROJECT_PROFILE.md",
    "templates/PRE_CODING_BASELINE_AUDIT.md",
    "templates/WORK_ITEM.md",
    "templates/AUTHORIZATION.md",
    "templates/HANDOFF.md",
    "templates/INDEPENDENT_PRE_CODING_REVIEW.md",
    "templates/CHANGE_REQUEST.md",
    "templates/INCIDENT_HOTFIX.md",
    "templates/DEFECT_RECORD.md",
    "templates/TEST_PLAN.md",
    "templates/TEST_CLOSURE.md",
    "templates/RELEASE_CANDIDATE.md",
    "templates/TECHNICAL_DESIGN.md",
    "templates/INTERACTION_SPEC.md",
    "templates/TRACEABILITY_MATRIX.md",
    "templates/EXPERIMENT_PROMOTION.md",
    "templates/FIX_CHAIN.md",
    "profiles/saas.md",
    "profiles/web-app.md",
    "profiles/admin-system.md",
    "profiles/mobile-app.md",
    "profiles/desktop-app.md",
    "profiles/backend-service.md",
    "profiles/ai-product.md",
    "profiles/game.md",
    "profiles/data-pipeline.md",
    "profiles/media-processing.md",
    "profiles/automation-tool.md",
    "profiles/shared-platform.md",
    "adapters/README.md",
    "adapters/jira/SKILL.md",
    "adapters/jira/MODELING_RULES.md",
    "adapters/jira/ISSUE_TEMPLATES.md",
    "adapters/jira/MIGRATION_AUDIT.md",
]

REPOSITORY_PATHS = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "manifest.txt",
    "scripts/validate.py",
    ".github/workflows/validate.yml",
]

REQUIRED_PATHS = REPOSITORY_PATHS + INSTALL_PATHS
ALLOWED_PUBLIC_ADAPTERS = {"jira"}
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
SENSITIVE_PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github-token": re.compile(r"\bgh(?:p|o|u|s|r)_[A-Za-z0-9]{20,}\b"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "bearer-token": re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{24,}\b", re.IGNORECASE),
}

# Construct these at runtime so the public repository does not itself contain
# the disallowed vendor/platform names as contiguous text.
FORBIDDEN_PUBLIC_PLATFORM_TERMS = [
    ("regional-platform-1", "".join(("yun", "xiao"))),
    ("regional-platform-2", "".join(("proj", "ex"))),
    ("regional-platform-3", "".join(("code", "up"))),
    ("regional-platform-4", "".join(("ali", "yun"))),
    ("regional-platform-5", "".join(("alibaba ", "cloud"))),
    ("regional-platform-6", "".join((chr(0x4E91), chr(0x6548)))),
    ("regional-platform-7", "".join((chr(0x963F), chr(0x91CC), chr(0x4E91)))),
]


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        files.append(path)
    return sorted(files)


def check_required_paths(errors: list[str]) -> None:
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).exists():
            errors.append(f"missing required path: {relative}")


def read_manifest(errors: list[str]) -> list[str]:
    manifest = ROOT / "manifest.txt"
    if not manifest.exists():
        errors.append("missing public install manifest: manifest.txt")
        return []

    entries: list[str] = []
    for raw_line in manifest.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        entries.append(line)

    if len(entries) != len(set(entries)):
        errors.append("manifest.txt contains duplicate paths")
    return entries


def check_manifest(errors: list[str]) -> None:
    entries = read_manifest(errors)
    expected = set(INSTALL_PATHS)
    actual = set(entries)

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        errors.append(f"manifest.txt missing install paths: {', '.join(missing)}")
    if extra:
        errors.append(f"manifest.txt contains unapproved install paths: {', '.join(extra)}")

    for relative in entries:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"manifest path does not exist: {relative}")
        elif not path.is_file():
            errors.append(f"manifest entry is not a file: {relative}")


def check_public_adapters(errors: list[str]) -> None:
    adapters = ROOT / "adapters"
    actual = {p.name for p in adapters.iterdir() if p.is_dir()}
    unexpected = sorted(actual - ALLOWED_PUBLIC_ADAPTERS)
    if unexpected:
        errors.append(f"unreviewed public adapter directories: {', '.join(unexpected)}")


def check_canonical_version(errors: list[str]) -> None:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if "Software Development SOP — 4.1.0" not in skill:
        errors.append("SKILL.md does not declare canonical version 4.1.0")
    if "PRE_CODING_REVIEW_PASS" not in skill:
        errors.append("SKILL.md is missing the independent pre-coding review gate")


def check_public_text_policy(files: list[Path], errors: list[str]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if EMAIL_RE.search(text):
            errors.append(f"email address found in public text file: {relative}")
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"sensitive pattern ({label}) found in: {relative}")
        folded = text.casefold()
        for label, needle in FORBIDDEN_PUBLIC_PLATFORM_TERMS:
            if needle.casefold() in folded:
                errors.append(f"forbidden public platform term ({label}) found in: {relative}")


def normalize_link(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1].strip()
    if " \"" in raw:
        raw = raw.split(" \"", 1)[0]
    elif " '" in raw:
        raw = raw.split(" '", 1)[0]
    return unquote(raw)


def check_markdown_links(files: list[Path], errors: list[str]) -> None:
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = normalize_link(match.group(1))
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target_without_anchor = target.split("#", 1)[0]
            if not target_without_anchor:
                continue
            resolved = (path.parent / target_without_anchor).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"relative link escapes repository in {path.relative_to(ROOT)}: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"broken relative link in {path.relative_to(ROOT)}: {target}"
                )


def main() -> int:
    errors: list[str] = []
    files = iter_text_files()

    check_required_paths(errors)
    check_manifest(errors)
    check_public_adapters(errors)
    check_canonical_version(errors)
    check_public_text_policy(files, errors)
    check_markdown_links(files, errors)

    if errors:
        print("VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"VALIDATION: PASS ({len(files)} text files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
