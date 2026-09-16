# Work Authorization Record

状态：DRAFT / APPROVED / EXPIRED / REVOKED（空白或模板默认DRAFT）
Authorization ID / 类型：CODING_AUTH | MERGE_AUTH | RELEASE_AUTH | HOTFIX_AUTH
Executor / 模式：HUMAN | AI | HUMAN_AI_PAIR
批准人及其在PROJECT_PROFILE中的角色 / 真实批准原文或记录 / 时间：

## 对象与共同边界（所有模式必填，可由Tracker等价字段承载）

Work IDs / 合同清单版本 / 代码base branch、SHA及允许推进范围：
允许修改的模块/路径/工作类型：
明确禁止或需重新批准的模块/路径/合同/操作：
目标环境与外部目标身份：
生产/破坏性动作、付费Provider预算、真实通知、私密数据外发：
未明确允许的高风险动作默认禁止；N/A须说明动作不涉及，不能因HUMAN而跳过。

## Coding准入依据

Stage 5 Package / 原始独立Review报告 / Reviewer身份核验：
审查类型、父审查和有效范围 / 受影响PASS是否失效：
Technical Owner的PRE_CODING_GATE_PASSED记录：
当前任务是否READY、依赖是否就绪：
无有效PASS/Gate则Coding授权无效。

## 分开的操作授权

MERGE_AUTH：exact PR head、Review/CI或批准的替代证据：
RELEASE_AUTH：RC/构建摘要/配置/环境、QA收尾与产品验收：
HOTFIX_AUTH：Incident、Runbook、动作范围、时限；不替代Coding/Merge/Release：
同一次批准可逐项列明多个动作，不得由一个推断全部。

## 有效性

起效/到期/撤销条件 / 复核Owner：
合同/任务/环境实质变化、base超出允许范围、Review失效、授权撤销均需重新核验。
证据位置 / 执行回执：

本模板不能由执行者自己填写APPROVED冒充批准。规则来源：[decision-rights](../references/decision-rights.md)。
