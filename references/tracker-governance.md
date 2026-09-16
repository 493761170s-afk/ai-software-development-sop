# Tracker Governance

## 唯一 Live Tracker

执行期只允许一个系统拥有实时状态、负责人和依赖。

Planning baseline、Spec Kit tasks 草稿、GitHub 历史 Issue、文档中的 checkbox 都不能在 Tracker Takeover 后继续充当进度账本。

## Capability Matrix

Tracker 可能没有完整 Jira 能力：

| Capability | Jira | GitHub Issues | Local/Other | Degrade rule |
|---|---|---|---|---|
| hierarchy | often | limited | varies | flat tasks + parent label/link |
| dependencies | link | manual/link | varies | explicit blocked-by field |
| estimates | field | custom/manual | varies | keep estimate in planning baseline |
| resolution | yes | close state | varies | map to status category |
| automation | rich | actions | varies | manual gate check |

缺能力不代表不合规，但必须诚实记录损失映射。

## 云效 Projex 适配

能力表只提供降级思路，不是各平台当前 API 能力保证。项目必须实际读取配置与工具 schema，区分工具未暴露、权限不足和资源未配置。

使用云效时，创建/导入/批量重分类/中文化先执行[云效项目协作适配器](../adapters/yunxiao/SKILL.md)的分类审查。需求分解、依赖、迭代归属分别建模；WBS 层级不直接等于 Tracker 对象树。中文卡片保留必要合同约束，不复制全量规格。

项目可以选择 GitHub 规划与 Codeup 开发，也可以保持原平台组合，但必须明确各类事实唯一权威、生效基线和变更方向；执行进度仍只有一个 Live Tracker。新规划草稿不能覆盖已生效合同，Codeup 开发后不能再以整仓镜像覆盖代码。

## Import Idempotency

Stable Work ID 是幂等键。创建结果不确定时标记 `UNKNOWN_CREATE_RESULT`，先搜索/对账，再决定补建。来源 WBS 一项拆为多卡时，先建立可追溯且唯一的切片标识与映射，不能让不同交付切片共享同一幂等键。写前检查并发修改，写后回读；稳定映射和审计快照不得变成第二份实时任务账本。
