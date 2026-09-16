# AI Software Development SOP

A stage-gated software development lifecycle for AI coding agents, with requirements, design, technical contracts, independent review, implementation, verification, and release governance.

> **Current release line:** 4.1.x  
> **Canonical workflow:** [`SKILL.md`](SKILL.md)  
> **中文说明:** [`README.zh-CN.md`](README.zh-CN.md)

## Why this exists

AI coding agents can write code quickly, but speed does not remove the need for product scope, acceptance criteria, interaction design, architecture, data/API contracts, test strategy, change control, or release authority.

This project keeps those traditional software-engineering controls and uses AI primarily as an execution resource. The central rule is simple:

**Do not start formal product coding until Stage 1–5 are complete, an independent non-authoring model has reviewed the pre-coding baseline, the material findings are resolved, and a human owner has explicitly authorized the work.**

The workflow is designed for human developers, AI agents, and mixed human/AI teams using the same artifacts, work-item boundaries, evidence, and authorization model.

## Lifecycle

```text
Stage 1  Project Definition
Stage 2  Requirements Engineering
Stage 3  Product / Experience Design
Stage 4  Technical Design
Stage 5  Development Planning & Detailed WBS

         Independent Pre-Coding Review
         Owner Gate + explicit Coding Authorization

Stage 6  Development Execution
Stage 7  Integration & Verification
Stage 8  Acceptance / Release / Operations
```

The independent review is a gate between Stage 5 and Stage 6. It is not a ninth stage and it is not a substitute for human authorization.

## Core principles

- Traditional SDLC first; AI is an executor, not an uncontrolled product owner.
- One authoritative source for each kind of fact; no shadow specifications or duplicate task ledgers.
- One live tracker for execution status.
- Stable requirement/work/test IDs remain independent of Jira, GitHub Issues, or other tracker keys.
- Requirements, behavior, API/DB/event/file/AI/provider contracts, NFRs, task boundaries, and required tests cannot be silently changed during coding.
- Bugs and change requests are different workflows.
- Tests may not be weakened, skipped, or rewritten merely to manufacture a green build.
- Evidence is tied to an exact candidate, configuration, environment, and test scope.
- Merge, verification, acceptance, and release are separate decisions.
- `EXPERIMENTAL`, `HOTFIX`, `HUMAN`, or `TEST_CORRECTION` labels do not create governance bypasses.

See [`SKILL.md`](SKILL.md) for the normative engineering constitution.

## What is included

- Eight stage skills under [`stages/`](stages/)
- Project-type profiles under [`profiles/`](profiles/)
- Change-control, review, incident/hotfix, traceability, and debugging utilities under [`utilities/`](utilities/)
- Reusable project, work-item, test, release, and review templates under [`templates/`](templates/)
- Supporting governance references under [`references/`](references/)
- Optional tracker/platform adapters under [`adapters/`](adapters/)

## Quick start

1. Read [`SKILL.md`](SKILL.md).
2. Copy or install this repository into the location your coding agent actually reads.
3. Create a project-owned `PROJECT_PROFILE` from [`templates/PROJECT_PROFILE.md`](templates/PROJECT_PROFILE.md).
4. For an existing project, run a baseline audit using [`templates/PRE_CODING_BASELINE_AUDIT.md`](templates/PRE_CODING_BASELINE_AUDIT.md).
5. Complete Stage 1 → Stage 5 for the explicitly bounded release or workstream.
6. Run the independent pre-coding review using [`utilities/independent-pre-coding-review/SKILL.md`](utilities/independent-pre-coding-review/SKILL.md).
7. Record the owner gate and explicit coding authorization before Stage 6.
8. Execute, verify, accept, and release with exact evidence and change control.

More detail: [`docs/QUICK_START.md`](docs/QUICK_START.md).

For a complete installation, use [`manifest.txt`](manifest.txt) as the required public skill payload. Repository CI verifies that the manifest matches the approved install set, every listed file exists, internal links resolve, sensitive patterns are absent, and only reviewed public platform adapters are present.

## Project types

Profiles can be combined. The current suite includes SaaS, web apps, admin/backoffice systems, mobile apps, desktop apps, backend services, AI products, games, data pipelines, media processing, automation tools, and shared platforms.

Multiple profiles compose by **union plus explicit conflict resolution**. Loading a later profile does not erase controls from an earlier one.

## Spec Kit

The default integration mode is `METHODOLOGY_ONLY`: reuse useful Constitution / Specify / Clarify / Plan / Tasks / Analyze methods while keeping the project's existing canonical documents and live tracker authoritative. This avoids creating a second hidden source of truth.

See [`references/spec-kit-integration.md`](references/spec-kit-integration.md).

## Platform adapters

Adapters are optional and must not change the mother SOP's governance gates. The first public adapter covers Jira issue modeling, readable issue content, and safe migration/reconciliation. The core tracker rules also support GitHub Issues and other systems through capability mapping and explicit degradation rules.

See [`adapters/README.md`](adapters/README.md).

## Status and versioning

This public repository starts from the 4.1.x workflow line. The public history is intentionally clean and does not import private project history or private project-specific adapters.

Semantic versioning is used for the workflow suite:

- **Patch:** wording/template corrections that do not change gates.
- **Minor:** compatible capability or adapter additions.
- **Major:** changes to authorization, testing, release, or pre-coding gate semantics.

See [`CHANGELOG.md`](CHANGELOG.md).

## Public roadmap

The first public maintenance cycle is tracked in [Issue #1](https://github.com/shinnslab/ai-software-development-sop/issues/1). Public roadmap items must remain reusable, vendor-neutral, and backed by real maintenance or adoption evidence.

## Contributing

Issues and pull requests are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md) first.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
