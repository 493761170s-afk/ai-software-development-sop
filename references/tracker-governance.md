# Tracker Governance

## 唯一 Live Tracker

执行期只允许一个系统拥有实时状态、负责人和依赖。

Planning baseline、Spec Kit tasks 草稿、历史 Issue、文档中的 checkbox 都不能在 Tracker Takeover 后继续充当进度账本。

## Capability Matrix

Tracker 能力不同，不能把 Jira 的字段或层级假定成所有工具的最低能力：

| Capability | Jira | GitHub Issues | Other tracker | Degrade rule |
|---|---|---|---|---|
| hierarchy | project-configured | limited/configurable | varies | flat items + explicit parent/reference |
| dependencies | issue links/configured relations | links/manual conventions | varies | explicit blocked-by field/reference |
| estimates | field/configuration dependent | custom/manual | varies | keep estimate in approved planning baseline |
| resolution/workflow | workflow configured | open/closed + project fields | varies | explicit mapping to lifecycle category |
| automation | available, project dependent | Actions/automation | varies | manual gate check with persisted evidence |

缺能力不代表不合规，但必须诚实记录损失映射。

## Jira Adapter

能力表只提供降级思路，不是某个 Jira 项目的实际配置保证。使用 Jira 时，创建、导入、批量重分类、调整层级或迁移前读取 [Jira Adapter](../adapters/jira/SKILL.md)，先发现实际 Issue Type、字段、Workflow、Transition、Hierarchy、Link、Sprint/Release 和权限配置，再执行映射与回读验证。

需求分解、工程依赖、迭代/发布归属分别建模；WBS层级不直接等于 Jira Issue 层级。Issue内容保留必要目标、Scope、AC、边界和来源，但不复制整篇规格。

## Tracker 与代码托管分工

项目可以使用 Jira 管理工作、GitHub 管理代码，也可以采用其他组合。必须明确 Product/Design/Technical Contract/Tracker/Code/Test Evidence 各自唯一权威、生效基线和变更方向；执行进度仍只有一个 Live Tracker。

Tracker中的草稿或评论不能自动覆盖已批准合同。代码PR/MR或提交引用Tracker Key时，只建立追溯关系，不把代码状态自动解释为需求已验收或已发布。只有项目实际配置并验证过的原生集成才可报告为原生关联。

## Import Idempotency

Stable Work ID 是幂等键。创建结果不确定时标记 `UNKNOWN_CREATE_RESULT`，先搜索/对账，再决定补建。来源 WBS 一项拆为多卡时，先建立可追溯且唯一的切片标识与映射，不能让不同交付切片共享同一幂等键。写前检查并发修改，写后回读；稳定映射和审计快照不得变成第二份实时任务账本。
