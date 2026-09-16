# 决策权、职责与授权

本文件是职责和批准权的唯一规则来源；模板只记录实例。适用 HUMAN、AI、HUMAN_AI_PAIR。

## 角色不是人数

PROJECT_PROFILE 必须实名指定 Product、Design、Technical、QA、Release Owner，并指定缺席时的替代人。一个人可以兼任全部角色；不得编造团队成员或把模型名称填成最终负责的人。AI 可以编制、执行、审查、提出建议，但不能自行签发或修改授予自己的权限。

| 决策 | 最终批准责任 | 必需输入 | 留存位置 |
|---|---|---|---|
| 项目范围、需求/AC、业务规则冻结 | Product Owner | Stage 1–2 产物、未决项 | 产品决策记录 |
| 用户/调用行为与设计冻结 | Design Owner；改变产品含义还需 Product Owner | Stage 3、需求映射 | 设计批准记录 |
| 技术合同/架构冻结 | Technical Owner | Stage 4、风险与替代方案 | 技术决策记录 |
| 计划与任务范围 | Technical Owner，产品优先级由 Product Owner 确认 | WBS、依赖、测试要求 | 唯一 Tracker / 计划基线 |
| CR | 对被改事实有权的 Owner；跨域会签 | 影响分析、被影响审批 | CR |
| PRE_CODING_GATE_PASSED | Technical Owner | 独立模型真实 PASS、当前基线、Stage 1–5 质量矩阵 | Gate 记录 |
| CODING_AUTH / 任务分配 | Technical Owner | 有效 Gate、READY 工作项 | 授权记录或包含等价字段的 Tracker 卡 |
| MERGE_AUTH | Technical Owner / 明确委派的维护者 | exact head、代码审查、自测/CI、修改边界 | PR |
| STAGE_7_VERIFIED | QA Owner | 复测、回归、TEST_CLOSURE | QA 签核 |
| 产品验收 / UAT 风险接受 | Product Owner / 指定业务代表 | 验收场景、真实结果、遗留风险 | 验收记录 |
| RELEASE_AUTH | Release Owner | 已验收 RC、构建摘要、恢复方案、QA 证据 | 发布授权 |
| HOTFIX_AUTH | 指定 Incident Owner + Release Owner | 事故、操作边界、时限、恢复方案 | INCIDENT_HOTFIX |

兼任角色可以由同一个人完成一次明确签署，但须列明签署的角色、动作、范围和依据。独立审查、P0/P1 独立复测不能因此改为自审。STRICT 的发布必须有独立技术/QA证据加人工批准，不强制第二名员工，也不把另一个模型当作法律/业务风险责任人。

## 授权不等于一个勾选框

所有模式使用同一最小授权记录：批准人及其角色、真实批准来源、时间、授权类型、Work IDs、合同基线、base SHA、允许/禁止路径和操作、目标环境、有效期/失效条件、必要的预算和数据边界。可直接用具备这些字段的 Tracker/PR 记录，不再复制第二份账本。

AI 可以把用户真实批准原文链接登记为记录，不能自己生成一句“Owner 已批准”。草稿字段和模板中的 APPROVED/PASS 字样不构成授权。范围、合同、环境或权限变化即需重新核验。批量授权可覆盖明确任务集合，不得写成“自行处理整个项目”。

CODING_AUTH、MERGE_AUTH、ACCEPTANCE、RELEASE_AUTH、HOTFIX_AUTH 分开判断。同一批准可以明确列出多个动作，不能从其中一个推断其他动作。没有风险依据不得接受未解决的 P0、安全/租户隔离失败或关键 AC 失败；审查 BLOCKER/MAJOR 不可由 Owner 直接豁免成 Pre-Coding PASS。

## 真实执行限制

Markdown 是工作规则，不是技术访问控制。安装 Skill 不会自动创建分支保护、撤销写权限或阻止 AI 使用工具。项目必须记录实际可用的 PR/分支权限、保护规则、凭据范围和检查方式；不足处标记控制缺口，不声称已自动强制。AI 只读审查可借助只读令牌/无写工具会话；无法技术隔离时保留操作记录并在审查结束比较基线。
