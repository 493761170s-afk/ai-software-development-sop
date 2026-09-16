---
name: jira-project-collaboration
description: Map approved requirements and detailed development plans into Jira while preserving one live tracker, stable IDs, source-of-truth boundaries, review gates, and human authorization. Covers issue classification, project-schema discovery, readable issue content, links/dependencies, sprint or release grouping, and safe migration.
---

# Jira Project Collaboration Adapter

## Scope and authority

Use this adapter when Jira is the project's live execution tracker or is being adopted as that tracker. It maps approved Stage 2 requirements and Stage 5 work items into Jira; it does **not** make Jira the authoritative PRD, design, API/DB contract, test specification, or release authority unless the project explicitly declares those facts there.

The mother [`SKILL.md`](../../SKILL.md) remains authoritative for lifecycle gates, independent review, change control, testing, and authorization.

## Read order

1. [`MODELING_RULES.md`](MODELING_RULES.md) — decide what each item means before creating issues.
2. [`ISSUE_TEMPLATES.md`](ISSUE_TEMPLATES.md) — render requirement, engineering, QA, and defect issues so humans can read them directly.
3. [`MIGRATION_AUDIT.md`](MIGRATION_AUDIT.md) — classify, import, relink, or clean up an existing Jira project safely.

## Discover the real Jira configuration first

Before any bulk write, read the target project's current configuration and capabilities. At minimum determine:

- project identity and project type;
- configured issue types and hierarchy/parent rules;
- required and optional fields plus allowed values;
- workflows, statuses, and transitions;
- assignee/user resolution rules;
- issue-link types and dependency capabilities;
- boards, sprints, releases/fix versions, components, labels, and custom fields that the project actually uses;
- permissions and automation/write capabilities available to the current account or tool.

Do not assume every Jira project has the same Epic/Story/Task/Bug hierarchy, fields, workflow, estimation scheme, or sprint model. A visible status list is not proof that every transition is legal.

## Execution path

```text
read approved project baseline + current Jira configuration
→ classify source requirements/work/tests/defects
→ build stable-ID ↔ Jira-key mapping
→ plan create/update/link operations
→ verify permission and required-field coverage
→ execute a small representative batch
→ read back values, hierarchy, links, status and ownership
→ execute the approved remainder
→ full reconciliation and audit
```

Existing valid issues should be reused. Do not delete and recreate a project merely to make it match a template.

## Stable IDs and source-of-truth rules

Jira keys are tracker identifiers, not requirement or work-item identity. Keep stable requirement/work/test IDs in a project-approved custom field, label, or structured issue section and maintain a mapping in the project profile or approved audit artifact.

Issue descriptions may summarize the local goal, scope, acceptance criteria, boundaries, and references, but must not silently redefine Product, Design, Technical Contract, or Test SOT content.

## Git and code integration

If code lives in GitHub or another Git host, Jira remains the live work tracker while code, PR/MR, CI, and release evidence stay in their own authoritative systems. Link real PR/MR and commit identifiers when available. Do not claim a native development integration exists unless the project has actually configured and verified it.

## Safety and idempotency

- Search by stable ID before creating an issue.
- If create/update results are uncertain, record `UNKNOWN_CREATE_RESULT`, query Jira, and reconcile before retrying.
- Detect concurrent edits before overwriting issue content or fields.
- Preserve issue history; correct mistakes with explicit updates rather than rewriting audit history.
- Bulk type changes, hierarchy changes, status changes, reassignment, deletion, or cross-project moves require explicit scope and approval.
- A successful API response is not completion; read the target issue back and verify the intended fields and relations.

Jira import or cleanup never grants `CODING_AUTH`, `MERGE_AUTH`, `ACCEPTANCE`, or `RELEASE_AUTH`; those remain governed by the mother SOP.
