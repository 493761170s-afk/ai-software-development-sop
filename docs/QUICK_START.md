# Quick Start

This guide explains how to adopt AI Software Development SOP without creating duplicate project authorities.

## 1. Pin the workflow

Choose a release/tag or exact commit and record it in the target project's `PROJECT_PROFILE`.

Do not silently replace an installed workflow copy. Treat upgrades as explicit project changes.

## 2. Install where the agent actually reads

The exact path depends on the coding tool. A common pattern is:

```text
.agents/skills/software-development-sop/
```

Copy the complete suite, not just the root `SKILL.md`, because the mother skill routes into stages, utilities, profiles, references, and templates.

Verify that your actual AI coding tool can discover/read the installed files. File placement alone is not proof that a tool loaded nested skills.

## 3. Create the project profile

Start from `templates/PROJECT_PROFILE.md` and fill in real project facts:

- project mode: NEW / EXISTING / MIGRATION;
- adoption level: MVA / STANDARD / STRICT;
- project-type profile combination;
- product, design, technical, QA, and release owners;
- canonical documents and live tracker;
- repository/branch/CI/environment controls;
- review evidence location;
- authorization evidence location;
- test evidence location;
- incident/hotfix policy;
- actual technical controls and known gaps.

A blank template is not approval.

## 4. Existing projects: audit before rewriting

Use `templates/PRE_CODING_BASELINE_AUDIT.md`.

Classify existing artifacts as:

- `CANONICAL`
- `REFERENCE`
- `DEPRECATED`
- `UNKNOWN`

Then follow:

```text
inventory → reuse → update → converge → fill gaps → freeze
```

Do not rewrite correct historical documents merely to match a template.

## 5. Complete Stage 1–5

For the explicitly bounded release/workstream:

1. Project Definition
2. Requirements Engineering
3. Product / Experience Design
4. Technical Design
5. Development Planning & Detailed WBS

Use the selected project profiles to add risk-specific requirements. Combined profiles use the union of required controls plus explicit cross-profile checks.

## 6. Independent pre-coding review

A different non-authoring model must review the complete first baseline. A new chat with the same authoring model, a renamed agent, or a different thinking setting is not sufficient independence.

The reviewer checks the exact baseline and records BLOCKER / MAJOR / MINOR / NOTE findings. Formal coding remains blocked until BLOCKER and MAJOR findings are closed and the reviewer produces a valid PASS for the current baseline.

## 7. Owner gate and coding authorization

Review PASS does not authorize coding by itself.

The technical owner verifies:

- reviewer provenance;
- reviewed baseline identity;
- findings closure;
- current baseline still matches the review;
- tracker takeover/dependencies;
- no unreviewed material changes.

Then record the pre-coding gate. Specific work still needs assignment/authorization and an explicit boundary.

## 8. Stage 6–8

Stage 6 implements only authorized work-item scope.

Stage 7 verifies the exact candidate, separates defects from change requests, protects test integrity, performs required independent retest, and records QA closure.

Stage 8 performs product acceptance, release readiness, release authorization, production verification, observation, and closeout.

## 9. Material changes after PASS

If scope, requirements, acceptance criteria, user-visible behavior, NFRs, technical contracts, dependencies/work boundaries, or required tests materially change:

1. stop affected coding;
2. run change control;
3. compute the impact/consumer closure;
4. update the owning canonical artifact;
5. invalidate the affected old review PASS;
6. perform FULL or bounded DELTA independent re-review;
7. restore authorization only after the new gate is valid.

Normal implementation commits and tracker progress changes do not automatically invalidate a contract review.

## 10. Do not confuse status words

```text
PACKAGE_READY != REVIEW_PASS
REVIEW_PASS   != GATE_PASSED
GATE_PASSED   != CODING_AUTH
CI_GREEN      != VERIFIED
VERIFIED      != ACCEPTED
ACCEPTED      != RELEASED
```

Keeping these states separate is a core purpose of the SOP.
