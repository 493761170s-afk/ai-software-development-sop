---
name: software-development-sop
description: 通用传统软件开发生命周期与工程治理。Stage 1–5完成且另一个独立模型全面审查通过后才允许正式Coding；人工/AI共用产物、任务与授权边界，支持SaaS、Web、服务、AI、游戏、数据、媒体等项目；采用Jira时路由项目协作建模、Issue模板与安全迁移规则。
---

# Software Development SOP — 4.1.0

## 1. 角色与规则归属

保留传统研发环节，用AI承担执行劳动，用经批准的上游产物限制下游行为。本Skill编排流程，不拥有项目的产品/API/DB/设计/任务事实。

本文件是生命周期与Engineering Constitution唯一权威；专项执行规则由下列文件拥有，阶段Skill和模板引用，不自行复制另一套规则。

| 控制 | 唯一执行规则 |
|---|---|
| 决策责任、人工批准、统一授权 | [decision-rights](references/decision-rights.md) |
| 各阶段质量下限与采用强度 | [adoption-level-matrix](references/adoption-level-matrix.md) |
| 首次全面审查、复审与结论 | [independent-pre-coding-review](utilities/independent-pre-coding-review/SKILL.md) |
| 身份与真实审查来源 | [reviewer-provenance](references/reviewer-provenance.md) |
| 合同基线、影响闭包、FULL/DELTA与失效 | [review-validity](references/review-validity.md) |
| 多Profile及交叉风险 | [profile-overlay](references/profile-overlay.md) |
| 实验隔离与正式转入 | [experiment-promotion](references/experiment-promotion.md) |
| 生产止损/热修复 | [incident-hotfix](utilities/incident-hotfix/SKILL.md) |
| Jira项目协作建模、Issue模板与安全迁移 | [jira-project-collaboration](adapters/jira/SKILL.md) |

## 2. Engineering Constitution — 不可覆盖

1. **传统SDLC为主，AI为执行资源。** 保留产品、设计、技术、开发、QA、验收、运维职责，不为AI开快捷通道。
2. **Stage 1–5强制。** 所有正式项目Coding前完成项目定义、需求、体验、技术与详细任务规划。采用级别只调深度，不跳阶段。
3. **独立模型审查强制。** 首次完整Stage 1–5基线必须由另一个非编制模型全面只读审查；自审、换会话/档位、摘要或局部抽查不能替代。BLOCKER/MAJOR清零且真实明确PASS才可放行。
4. **一事实一权威。** Product、Design、Technical Contract、Tracker、Code/Test Evidence各司其职，禁止Shadow Spec/Plan/Task Ledger。
5. **一个Live Tracker。** 规划文件保存批准基线，不双边维护进度。
6. **Stable Work ID独立于Tracker Key。** 需求/任务/测试可追溯性不绑定某平台编号。
7. **先批准和审查，再实现。** 正式执行只能实现通过审查的Requirement、Design、Contract及Work Item；EXISTING不是自动批准。
8. **执行者不得扩边界。** 人工、AI、PAIR均受同一Scope、允许/禁止修改和操作权限约束；越界立即BOUNDARY_EXCEEDED并转影响分析/变更控制。
9. **Bug与CR分离。** 修复实现偏离已批准标准是Bug；缺标准、规则改变和新想法回上游，不靠猜测修代码。
10. **测试完整性不可牺牲。** 禁止删/弱化测试、skip、错误snapshot或Mock真实必测路径来制造Green；真实测试纠错按Stage 7记录依据并独立复核。
11. **候选与证据精确。** 测试证据绑定SHA/构建/配置/环境；变更使受影响证据失效。代码候选不同于Stage 1–5合同基线。
12. **Merge≠Acceptance≠Release。** CI、Review、Tracker状态都不能自己扩大授权。
13. **状态外置。** 任务边界、授权、审查原文、候选和证据不能只存在聊天记忆；模板空值不算通过。
14. **人工/AI同流程。** 所有模式授权字段一致，可用同一Tracker卡承载；高风险独立审查/复测不得自签。一个人可兼任多个Owner，AI不得伪造或给自己签授权。
15. **既有项目复用有效历史。** Baseline Audit解决缺失、过期和冲突，不为形式重写；冻结旧版本不自动批准新开发。
16. **局部阻塞必须可证明。** 仅经影响闭包和Reviewer确认排除的范围可沿有效旧PASS继续；未知消费者不可当无影响。
17. **实质变更使PASS失效。** Scope、需求/AC/NFR、行为、技术合同、工作边界/依赖、必测标准改变，受影响范围必须先独立FULL/DELTA重审，再恢复Coding。
18. **例外名称不提供豁免。** EXPERIMENTAL、HOTFIX、TEST_CORRECTION和HUMAN标签都不能绕过上述规则。新代码不允许先上线再补Stage 1–5审查。

Project Profile/Adapter不能覆盖本节。Markdown规则不是技术权限，项目必须如实记录实际控制手段及缺口。

## 3. 八阶段与准入状态

```text
STAGE_1_PROJECT_DEFINED
→ STAGE_2_REQUIREMENTS_READY
→ STAGE_3_DESIGN_READY
→ STAGE_4_TECH_READY
→ STAGE_5_PRE_CODING_PACKAGE_READY
→ INDEPENDENT_PRE_CODING_REVIEW
→ PRE_CODING_REVIEW_PASS
→ PRE_CODING_GATE_PASSED
→ 明确的任务分配 / CODING_AUTH
→ STAGE_6_IMPLEMENTED
→ STAGE_7_VERIFIED
→ Stage 8：ACCEPTED → RELEASE_READY → RELEASED
```

审查是5和6之间的Gate，不新增Stage 9。PACKAGE_READY是编制完成；REVIEW_PASS是独立审查结果；GATE_PASSED是Technical Owner核验身份/基线/结果后的准入记录；三者都不是工作授权本身。

### Pre-Coding Hard Gate

目标本期Release/明确范围必须满足：Stage 1–5及质量矩阵通过；Scope/AC/设计或无UI调用行为明确；关键技术合同已批准；WBS、依赖和必测集合可执行；唯一Tracker已承接目标任务；全部直接依赖Ready；未知项有Owner与影响ID；真实不同模型全面审查或有效增量继承、BLOCKER/MAJOR=0；审查与当前合同基线匹配且无未审实质变化；Technical Owner记录Gate；工作项有真实分配/授权。

首次不能只审一个页面而宣称整个项目准备完毕。允许先定义有限本期范围，但必须明确排除项与公共依赖，并完整走1–5及独立审查；后续范围按变更控制纳入。

未通过只允许获准的调研、只读分析、隔离Spike/PoC；遵守实验记录和转入规则，不能把探索性代码直接当正式功能。

## 4. 项目接入

创建或更新项目自己的 [PROJECT_PROFILE](templates/PROJECT_PROFILE.md)：钉住SOP版本和源提交、NEW/EXISTING/MIGRATION、类型组合、采用强度、具名Owner、各SOT、Tracker能力/映射、授权/审查/测试证据位置、分支/CI/环境与事故策略。

EXISTING/MIGRATION先做 [Baseline Audit](templates/PRE_CODING_BASELINE_AUDIT.md)：标明CANONICAL/REFERENCE/DEPRECATED/UNKNOWN，核验历史代码和实验来源；有效产物复用、缺失补齐、冲突收敛，再组成完整送审包。Adapter示例不证明项目事实、安装状态或已获批准。

MVA/STANDARD/STRICT按质量矩阵执行；高风险和Profile必需项不得降级。多个Profile按并集与交叉控制合成，不能最后加载者覆盖。角色和批准人按decision-rights落盘，允许一个人兼任。

## 5. 独立审查与变更

执行 [独立审查Skill](utilities/independent-pre-coding-review/SKILL.md)，报告使用 [Review Record](templates/INDEPENDENT_PRE_CODING_REVIEW.md)。不接受无法核验身份、不可读取资料或编制模型代写的PASS。

[change-control](utilities/change-control/SKILL.md)必须联动review-validity：先确定语义差异和消费者闭包、失效旧PASS、更新上游、独立复审；局部更改不无脑全仓重读，影响无法封闭则扩大到FULL。普通实现提交或Tracker进度变化不自动重审合同。

## 6. Spec Kit与任务账本

默认 `SPEC_KIT_MODE=METHODOLOGY_ONLY`；借用Constitution/Specify/Clarify/Plan/Tasks/Analyze方法，输出回项目SOT。不默认init或生成第二套.specify；原生写入默认NON_CANONICAL，只有项目显式声明NATIVE_CANONICAL并消除双权威后才改变。

native implement/converge不得绕过Tracker、独立审查和授权。新发现任务先进入变更/规划，不自动实现。正式执行期Tracker是唯一状态/负责人/依赖来源；卡片引用合同而不重新定义API/DB。Stable Work ID作导入幂等键，UNKNOWN_CREATE_RESULT先查重，不盲重建。能力不足按 [tracker-governance](references/tracker-governance.md)如实降级。

采用或准备采用 Jira 时，Stage 2 需求落卡、Stage 5 Tracker 接管以及后续批量创建、重分类或迁移之前，必须读取 [Jira Adapter](adapters/jira/SKILL.md)，先发现目标项目真实的 Issue Type、字段、Workflow、层级、依赖和 Sprint/Release 配置，再执行分类审查与映射。WBS章节不能机械变成Issue或Sprint；需求分解、工程依赖和交付归属分别建模。该适配不改变母SOP Gate，也不自动授权编码、合并、验收或发布。

## 7. 执行与最小读取集

HUMAN、AI、PAIR共用 [工作项](templates/WORK_ITEM.md)和 [授权](templates/AUTHORIZATION.md)。可连续完成已授权任务集合，不要求每个Issue停一次；遇到真实阻塞、范围/权限变化、审查失效或Mission完成才停。权限不因执行模式改变。

普通任务只读：PROJECT_PROFILE、当前工作项及关联Requirement/Design/Contract、受影响模块、Tracker依赖、代码base/candidate、相关测试、有效审查和授权。首次接入/首次全面审查/无法封闭的大变更读完整基线；DELTA读影响集与交界，不例行全仓扫描。

## 8. 路由与完成

需求→Stage 2；体验/交互→3；技术/安全/数据/Provider→4；WBS/依赖→5；实现缺陷→6；测试/环境/复测→7；验收/发布→8。范围/合同变化→change-control；重复失败→root-cause-debug；追溯缺口→requirement-traceability；实验转入→experiment-promotion；生产P0→incident-hotfix。

Stage 7必须有QA收尾证据，不把“修复者自测通过”当独立验收。只有Stage 8生产确认和收尾完成才是RELEASED。CODE_COMPLETE、CI_GREEN、REVIEW_PASS、TRACKER_DONE、VERIFIED、ACCEPTED均不得包装为已发布。
