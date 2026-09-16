# Jira Migration / Classification Audit

Use this when creating a Jira project from an approved plan or cleaning up an existing Jira project. The audit is a controlled migration plan, not a second live tracker.

## 1. Read before write

Record the target project, current baseline, operator/tool, permission scope, and migration authorization. Read the in-scope Jira configuration and issues with pagination/search sufficient to cover the whole target set.

Capture a pre-change snapshot of the fields needed for reconciliation, such as:

- issue ID/key and stable source ID;
- issue type and parent;
- summary and description;
- status/resolution;
- assignee/reporter where relevant;
- priority, labels, components, sprint, fix version;
- native issue links/dependencies;
- update timestamp and important custom fields.

Do not copy secrets into the audit snapshot.

## 2. Classification and coverage table

| Stable source ID / Jira key | Current semantic type | Target semantic type | Action | REQ/AC/Test coverage | Hierarchy/dependencies/release grouping | Material impact |
|---|---|---|---|---|---|---|
| | | | REUSE / UPDATE / RELINK / CREATE / PROPOSE_SPLIT / PROPOSE_MERGE / DEFER / BLOCK | | | |

Every approved requirement/AC/NFR, engineering delivery item, and required independent verification must have a destination or an explicit deferred/excluded decision.

Do not optimize for a target issue count. Several source items may validly converge into one issue, or one WBS item may split into several delivery slices, but all stable IDs, ACs, dependencies, and verification responsibilities must remain traceable.

## 3. Approval before material restructuring

Pure formatting/readability fixes may proceed only when semantics are unchanged. The following are potentially material and must be separately evaluated/approved:

- splitting or merging delivery scope;
- changing issue type in a way that changes meaning or workflow;
- changing hierarchy or dependencies;
- changing acceptance criteria or required tests;
- changing owner, priority, status, sprint/release commitment, or dates;
- deleting/recreating issues or moving them across projects.

If a material change alters the approved Stage 1–5 baseline, follow change control and independent re-review before affected coding resumes.

## 4. Idempotent execution

1. Use Stable Work/Requirement IDs as the idempotency key, not issue summary text.
2. Query Jira before create; if a matching stable ID exists, reconcile rather than duplicate.
3. If a create/update call times out or returns an uncertain result, mark `UNKNOWN_CREATE_RESULT` and query before retrying.
4. Check the issue's latest update timestamp/content before overwriting; pause on `CONCURRENT_CHANGE`.
5. Execute a representative small batch, read back the result, then continue the approved remainder.
6. Create/update issues first, verify them, then create hierarchy/dependency links, then run full reconciliation.
7. Default to preserving existing issue history; do not delete and rebuild simply because a conversion is inconvenient.

## 5. Final reconciliation

Verify:

- full source-to-Jira coverage;
- correct semantic classification;
- no duplicate stable IDs;
- hierarchy and dependency links read back correctly;
- all required fields, owners, statuses, sprint/release groupings match the approved plan;
- no unauthorized fields changed;
- issue descriptions are readable and preserve local scope/AC/boundary information;
- links to product/design/technical/test sources are valid;
- tracker takeover state is updated in `PROJECT_PROFILE`;
- project coding authorization remains whatever the pre-existing authorization record says.

A successful migration never implies `PRE_CODING_GATE_PASSED`, `CODING_AUTH`, `VERIFIED`, `ACCEPTED`, or `RELEASED`.
