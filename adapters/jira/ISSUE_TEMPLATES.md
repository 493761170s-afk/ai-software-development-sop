# Jira Issue Content Templates

These are readable content layouts, not a replacement for Jira's structured fields or the repository templates. Use Jira fields for assignee, priority, status, sprint, fix version, components, labels, and other configured metadata; keep the description focused on the information a contributor needs to understand the issue.

## A. Requirement / Story

### Context and user/caller goal
Who needs the capability, in what situation, and what outcome should become possible?

### Scope
What behavior is included, and what is explicitly out of scope?

### Flow, rules, and exceptions
Describe the important normal path plus state, permission, validation, failure, and partial-success behavior where applicable.

### Acceptance criteria
- `AC-...`: precondition → action → observable result.
- Include relevant NFR thresholds or constraints only when they come from the approved project baseline.

### References and traceability
Stable Requirement/Story IDs, Design/Interaction source, Product SOT, related engineering/QA items.

## B. Engineering Task

### Goal and deliverable
What concrete artifact or behavior will this issue deliver?

### Scope and boundaries
Allowed modules/paths/operations, explicit exclusions, and any contract that must not be changed.

### Inputs and dependencies
Approved requirement/AC, design, technical contract, predecessor result, environment or provider prerequisites.

### Completion criteria and required tests
What locally observable result proves the work is complete? Which unit/integration/contract/E2E/security/performance or profile-specific tests are required?

### Execution constraints and references
Stable Work ID, real work authorization, base branch/SHA, risk/data/budget boundaries, reviewer requirements.

### Delivery evidence
PR/MR, candidate SHA, local/CI verification, review and QA evidence. Fill only after the evidence exists.

## C. Independent QA / Verification Task

### Verification goal
Which requirements, ACs, risks, integrations, or release conditions are independently verified?

### Candidate, environment, and data
Exact candidate SHA/build, configuration, environment, roles/accounts, test-data version, and real-vs-mock dependency rules.

### Scenarios and expected results
For each scenario: precondition, action, expected result, evidence location.

### Failure routing
Create/link a defect for implementation deviation; route missing/changed standards through clarification or change control. Do not rewrite expected results to match current behavior.

## D. Bug

### Impact and severity
Who/what is affected and why the severity/priority is appropriate?

### Reproduction
Candidate/version, environment/config, data conditions, exact steps.

### Expected vs actual
Cite the approved AC/rule/contract for expected behavior, then describe the observed result.

### Evidence and relationships
Origin requirement/work item, logs/screenshots/traces, related PR/commit when it exists, Fix Chain ID where applicable.

### Fix and retest
Root cause, fix candidate, self-test, independent retest owner/evidence, regression results, QA closure.

## E. Epic / Capability Group

Use only when the target Jira project has an appropriate parent/capability type and the grouping has a real outcome.

### Outcome
The coherent capability or release result this group represents.

### Included requirements and delivery items
List stable IDs and native child/related issues.

### Completion definition
What must be delivered and verified before the group is considered complete? Do not equate all child issues being closed with product acceptance or release.
