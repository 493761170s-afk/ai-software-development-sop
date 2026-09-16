# PROJECT_PROFILE

模板仅记录项目实例；空字段不是已批准。规则见 [母SOP](../SKILL.md) 及其控制索引。项目采用时应钉住正式版本与源提交，不静默替换已安装版本。

```yaml
PROFILE_VERSION: 4.1
BASE_SOP_VERSION: 4.1.0
BASE_SOP_SOURCE_SHA:
PROJECT_NAME:
PROJECT_MODE: NEW | EXISTING | MIGRATION
PROJECT_TYPES: []
ADOPTION_LEVEL: MVA | STANDARD | STRICT
ADOPTION_QUALITY_COVERAGE_LOCATION:
PROFILE_OVERLAY_RECORD_LOCATION:
HIGH_RISK_STRICT_SCOPES: []

HUMAN_OWNERS:
  product:
  design:
  technical:
  qa:
  release:
  incident:
  alternates_record:
DECISION_RECORD_LOCATION:
DELEGATIONS_RECORD_LOCATION:

CONSTITUTION_SOURCE:
PRODUCT_SOT:
DESIGN_SOT:
TECHNICAL_SOT:
TEST_SOT:
RELEASE_SOT:
RISK_REGISTER_LOCATION:
SPEC_KIT_MODE: METHODOLOGY_ONLY | NATIVE_NON_CANONICAL | NATIVE_CANONICAL

LIVE_TRACKER:
TRACKER_TAKEOVER_STATE: NOT_YET_STARTED | PARTIAL | ACTIVE
TRACKER_CAPABILITIES:
  hierarchy:
  dependency:
  estimate:
  resolution:
  automation:
STABLE_WORK_ID_FORMAT:
TRACKER_MAPPING_LOCATION:
PLATFORM_ADAPTERS: []
TRACKER_CLASSIFICATION_AUDIT_LOCATION:
TRACKER_ACCESS_ROUTE_RECORD_LOCATION:
TRACKER_SCHEMA_MAPPING_RECORD_LOCATION:
TRACKER_CONTENT_LANGUAGE: en | project-defined
ITERATION_MODE: TIMEBOXED | DELIVERY_BATCH | KANBAN
ITERATION_POLICY_LOCATION:
DOCUMENT_CODE_AUTHORITY_AND_SYNC_POLICY_LOCATION:

PRIMARY_PREPARATION_MODEL_RECORD:
MATERIAL_CONTRIBUTOR_MODEL_RECORD:
MODEL_IDENTITY_EVIDENCE_LOCATION:
MODEL_ALIAS_EVIDENCE_LOCATION:
SAME_PROVIDER_REVIEW_ALLOWLIST: []
INDEPENDENT_PRE_CODING_REVIEW_POLICY: REQUIRED
PRE_CODING_REVIEW_RECORD_LOCATION:
ORIGINAL_REVIEW_EVIDENCE_LOCATION:
CONTRACT_BASELINE_MANIFEST_LOCATION:
IMPACT_AND_DELTA_REVIEW_RECORD_LOCATION:

AUTH_RECORD_LOCATION:
EVIDENCE_RECORD_LOCATION:
QA_CLOSURE_RECORD_LOCATION:
DEFECT_TRIAGE_POLICY_LOCATION:
EXPERIMENT_REGISTER_LOCATION:
CONSUMER_REGISTRY_LOCATION:

REPOSITORY:
DEFAULT_BRANCH:
BRANCHING_POLICY:
ACTUAL_ACCESS_CONTROLS_RECORD:
CONTROL_GAPS_RECORD:
CI_ENTRYPOINT:
CANONICAL_VERIFY_COMMAND:
ENVIRONMENTS: [dev, test, staging, prod]
RELEASE_CHANNEL:
EMERGENCY_HOTFIX_POLICY: references-to-approved-runbook-and-core-incident-hotfix
INCIDENT_RECORD_LOCATION:
INCIDENT_TIMEBOX_POLICY_LOCATION:
EXECUTION_MODES: [HUMAN, AI, HUMAN_AI_PAIR]

RISK_FLAGS:
  multi_tenant: false
  auth_sensitive: false
  payment_or_billing: false
  personal_or_private_data: false
  destructive_migration: false
  paid_external_provider: false
  ai_core_behavior: false
  game_or_realtime: false
  data_pipeline: false
  media_processing: false
  shared_platform: false
```

## Authority与采用说明

一个人可以兼任多个Owner；登记真实姓名/身份和批准权，AI不能填作最终Owner。职责按 [decision-rights](../references/decision-rights.md)，质量按 [adoption-level-matrix](../references/adoption-level-matrix.md)，类型组合按 [profile-overlay](../references/profile-overlay.md)。只引用事实位置，不复制PRD/API/DB。

## 审查与变更

使用 [reviewer-provenance](../references/reviewer-provenance.md)记录可核验provider/model/version及编制参与者，版本未暴露写NOT_EXPOSED并附证据。allowlist不是仅写不同名称；必须有来源确认。STRICT由具名人工核验真实报告。独立审查不得改OPTIONAL/OFF。

合同清单不含可变进度和审查报告自身，避免自指失效；FULL/DELTA范围按 [review-validity](../references/review-validity.md)。

## 项目专属项

可以增加约束，不得降低母SOP、风险/交叉Profile、统一执行边界或事故门禁。EMERGENCY_HOTFIX_POLICY只引用已批准Runbook，不是自由豁免文字。记录实际分支/工具权限与缺口，不声称Skill安装自动强制权限。

风险flags为模板占位，项目接入必须逐项核验并记录依据；默认false不证明没有风险。

## Jira项目协作（采用时填写）

使用或准备采用 Jira 时，`PLATFORM_ADAPTERS` 登记 `adapters/jira/SKILL.md`，并按 [Jira Adapter](../adapters/jira/SKILL.md) 记录项目身份、Issue Type/Hierarchy、字段与允许值、Workflow/Transition、Link/Dependency、Sprint/Release、成员解析、权限和真实访问方式。未采用 Jira 的项目使用自身Tracker映射，不需要迁移平台。

项目绑定、已验证 ID/Key 与配置发现时间可以存于项目映射；PAT、API token、私钥和其他凭据只能保存安全引用。采用 Jira 管理工作、GitHub 管理代码时，明确 Jira 是 Live Tracker、GitHub 是代码/PR/CI 权威，并只维护引用关系，禁止形成第二个实时进度账本。
