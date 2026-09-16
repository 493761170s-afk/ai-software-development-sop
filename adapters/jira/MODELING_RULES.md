# Jira Modeling Rules

Use these rules after reading the project's current Jira configuration. The names Epic, Story, Task, Bug, Sub-task, Sprint, Component, and Fix Version are common Jira concepts, but only use types and fields that actually exist in the target project.

## 1. Classify by meaning before choosing an issue type

| Semantic object | What it should answer | Typical Jira representation when available |
|---|---|---|
| Requirement / user capability | Who needs what result, in which context, and how is it accepted? | Story or project-specific requirement type |
| Capability group / large outcome | Which approved requirements jointly deliver one explainable outcome? | Epic or parent work item |
| Engineering work item | What concrete implementation or engineering artifact will be delivered and verified? | Task, Story, or project-specific engineering type |
| Independent QA / verification work | Which ACs or risks are independently verified and what evidence is produced? | Task, test issue type, or project-specific QA type |
| Defect | Where does an implemented candidate deviate from an approved baseline? | Bug |
| Delivery grouping | Which work belongs to a timebox or release target? | Sprint, Fix Version, Epic, or another configured grouping |

Never create a product requirement merely because an engineering task needs a parent. Infrastructure, CI, security hardening, migrations, and shared technical work may remain engineering items linked to the approved architecture/NFRs they support.

## 2. Requirements are not implementation checklists

A requirement issue should retain:

- stable Requirement/Story/AC IDs;
- actor or caller;
- context and trigger;
- desired result;
- important rules and states;
- observable acceptance criteria;
- scope and explicit exclusions;
- references to the authoritative product/design sources.

Implementation steps, file paths, database migrations, unit-test commands, and deployment actions belong in engineering work items unless they are themselves approved product or system constraints.

## 3. Engineering work items are delivery slices

A work item should have one coherent output that can be implemented, reviewed, and verified without guessing. Include:

- Stable Work ID;
- requirement/AC references;
- design and technical-contract references;
- in-scope and out-of-scope boundaries;
- inputs, outputs, dependencies, and blockers;
- assignee/execution mode;
- required tests and evidence;
- allowed/forbidden change boundaries;
- estimate/priority where the project uses them.

Do not split into ten-minute microtasks, but do not hide a state machine, tenant boundary, payment flow, AI pipeline, migration, or cross-system integration inside a single vague task.

## 4. Keep three relationship dimensions separate

```text
product decomposition: capability/requirement → delivery items
engineering dependency: work/defect → blocked-by / blocks / related dependency
release grouping: issues → sprint / fix version / epic / project-defined batch
```

Use Jira parent/child or issue links only when the configured project supports the intended semantics. A URL pasted into a description is a reference, not proof of a native relationship.

Dependency links should explain what result is required before the dependent item can proceed. A frozen API/contract may allow parallel implementation even when another code task is incomplete.

## 5. Stable IDs are independent of Jira keys

Jira key changes caused by moves or project reorganization must not destroy traceability. Store stable IDs in a project-approved custom field, label, or structured issue section and maintain a stable-ID ↔ Jira-key mapping.

When one WBS item must be split into multiple Jira issues, assign unique delivery-slice IDs before creation. Never reuse one idempotency key across distinct issues.

## 6. Workflows and transitions

Do not infer a legal transition from the list of visible statuses. Read the actual workflow/transition capabilities available to the current account or tool. Respect required fields, validators, permissions, and project-specific resolution semantics.

`Done` in Jira does not automatically mean `VERIFIED`, `ACCEPTED`, or `RELEASED` under the SOP. Map Jira statuses to lifecycle meanings explicitly in `PROJECT_PROFILE`.

## 7. Sprints, releases, and Kanban

Choose the project's delivery mode deliberately:

- `TIMEBOXED`: use real sprints with approved goal, dates, and entry/exit expectations.
- `DELIVERY_BATCH`: group work by a release/fix version, epic, or another configured batch without inventing fake sprint dates.
- `KANBAN`: continuous flow may legitimately have no sprint; record WIP and release/acceptance rules instead.

Do not create placeholder sprints just to make the board look complete, and do not treat every milestone as a sprint.

## 8. Defects and changes

A Jira Bug must cite the approved expected behavior, candidate/environment, reproducible actual behavior, severity, priority, evidence, fix owner, and retest plan. If no approved expectation exists, route the item to requirement/design/contract clarification or change control instead of inventing a bug standard.

Changing scope, ACs, contracts, dependencies, or required tests is a Change Request even if the request arrives through a Jira comment or issue edit. Follow the mother SOP's change-control and re-review rules before affected coding resumes.
