# Spike / PoC 实验与正式转入

实验用于回答技术不确定性，不是绕过 Stage 1–5 的业务开发通道。

## 实验入口与隔离

实验记录至少有：问题/假设、负责人、限定范围与时限、隔离分支/目录、测试数据/目标、可用外部操作和预算、预期证据、结束处置。未授权不得访问生产、真实客户数据或付费Provider。目录/分支名称不是权限；验证生产构建/部署不包含实验代码或产物。

实验产物标 EXPERIMENTAL / NON_PRODUCTION / NON_BASELINE。默认不能合入正式集成/发布路径、不能被生产代码import、不能复制粘贴到正式模块后省略审查。隔离的实验记录可入文档，代码应留独立隔离分支/目录；任何例外隔离方式由Technical Owner批准且证明不会进入生产构建。禁止更名为工具/测试辅助就自动转正。

## 三种结项

- DISCARD：保留结论和必要证据，停用实验。
- ARCHIVE：只作参考，不作为当前需求/合同/已批准实现。
- PROMOTION_REQUESTED：使用 [EXPERIMENT_PROMOTION](../templates/EXPERIMENT_PROMOTION.md) 申请正式复用。

## 转正条件（全部满足后才允许正式集成）

1. 固定来源分支/提交、文件/产物清单及许可证/来源风险，不以“已经跑通”代替需求。
2. 映射到批准的 REQ/RULE/AC、Design、技术合同、工作项、测试/Eval；缺项先回 Stage 1–5。
3. 已有项目把该来源登记在 Baseline Audit 中为实验来源；`EXISTING`只能表示经核验纳入当前基线，实验存在本身不提供 APPROVED 权限。
4. 首次完整 Pre-Coding Review或符合 [review-validity](review-validity.md) 的增量审查通过。未批准复用范围不得由下游任务假定可用。
5. Technical Owner授权正式转入任务，执行 Stage 6 的清理/改造、代码审查、自测、安全和专项验证，并取得 MERGE_AUTH。允许经验证复用，不强制全部重写。
6. 登记最终整合提交、测试证据、去除临时配置/凭据及隔离证明；只有这一步完成才为 PROMOTED。

转入失败保持隔离。实验输出提供的信息可用于技术决策，但不能把实验代码自动认作生产正确性证据。
