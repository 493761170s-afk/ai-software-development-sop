# Contributing

Thanks for helping improve AI Software Development SOP.

## What belongs here

Contributions should improve reusable software-development governance for human developers, AI coding agents, or mixed teams. Good contributions include:

- clearer lifecycle or gate semantics;
- stronger requirement, design, technical, testing, or release controls;
- reusable templates;
- project-type profiles;
- tracker/platform adapters that do not weaken the mother SOP;
- validators and examples that make adoption easier.

Project-specific business facts, credentials, customer data, internal repository URLs, and private incident evidence do **not** belong in this public repository.

## Before opening a pull request

1. Read `SKILL.md` and the files you intend to change.
2. State whether the change is wording-only, compatible capability, or governance-semantic.
3. Preserve the separation between lifecycle rules and platform/project adapters.
4. Do not create a second source of truth for an existing control.
5. Update links/templates/references affected by the change.
6. Run `python scripts/validate.py`.

## Versioning

- Patch: wording/template correction without gate changes.
- Minor: compatible profile, adapter, template, or workflow capability.
- Major: changes to authorization, testing, release, or pre-coding gate semantics.

## Pull request description

Please include:

- problem and failure scenario;
- files/control areas affected;
- whether existing adopters need migration;
- verification performed;
- any behavior intentionally left unchanged.

## Review expectations

Changes to the Engineering Constitution, independent review rules, authorization semantics, test-integrity rules, incident/hotfix path, or release gates require especially strict review because they can alter downstream project safety.

## License

By contributing, you agree that your contribution is licensed under Apache-2.0 as described in `LICENSE`.
