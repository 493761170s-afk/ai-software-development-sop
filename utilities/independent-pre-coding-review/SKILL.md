---
name: independent-pre-coding-review
description: Stage 1–5完成后的强制不同模型只读全面审查；复审按影响闭包FULL或DELTA执行，核验原始身份/报告、质量矩阵、跨阶段一致性，BLOCKER/MAJOR清零才出PASS。
---

# Independent Pre-Coding Review

首次本期基线必须全面审Stage 1–5；DELTA不是首次审查捷径。本Skill审项目基线，审Skill库本身的Issue报告不自动给予任何项目Coding许可。

## 1. Reviewer与只读性

执行 [reviewer-provenance](../../references/reviewer-provenance.md)：核验编制参与模型和Reviewer真实标识/来源，不得仅凭自述或名称差异；仅换会话、Agent或Thinking档位无效。Reviewer不得实质编制本轮被审范围；只读审查，不修改合同后宣布自审通过。

身份或来源无法确认：IDENTITY_UNVERIFIED / REVIEW_EVIDENCE_UNVERIFIED，Gate保持阻塞。缺访问能力应明确列未读资料，不可从摘要脑补全面审查。

## 2. Review Package

PROJECT_PROFILE及Owner/采用矩阵/Profile交叉表；Stage 1目标/Scope/Actors/风险；Stage 2 PRD/FRD/用例/规则/AC/NFR；Stage 3 IA/流程/交互/设计版本；Stage 4架构/数据/API/Event/File/安全/Provider/ADR及高风险验证；Stage 5本期完整WBS/工作项/依赖/Tracker结构快照/Test Plan；双向追溯、全部未知项/延期/风险。

附合同内容版本清单/hash、源Repo SHA、外部设计/Tracker快照、编制参与者。DELTA另附父完整审查、未决Finding、语义diff、影响闭包、排除依据和消费者证据。范围/模式按 [review-validity](../../references/review-validity.md) 判定；报告写入本身不改变合同基线。

## 3. 全面审查维度

| 维度 | 必查内容 |
|---|---|
| Stage 1 | 用户/调用方、可验证目标、Scope/Out of Scope、依赖证据、类型/风险、决策责任 |
| Stage 2 | 全部本期功能的Requirement/AC、业务/状态/访问规则、异常/NFR、无隐含未决假设 |
| Stage 3 | 从入口到结果的用户/调用流程、状态/权限/异常/恢复、术语与文案；Figma不扩Scope，无UI仍有行为设计 |
| Stage 4 | 架构适配而非过度设计，数据/接口/事件/文件/AI/媒体合同，安全/租户/并发/事务/幂等/迁移/恢复/可观测性；第三方证据，PROPOSED不冒充APPROVED |
| Stage 5 | Milestone/Module/Feature/页面/API/DB/测试任务可执行，不过粗/不过碎；真实依赖、Owner、AC/测试/边界、Tracker接管、人工/AI均无需猜需求 |
| Cross-Stage | Requirement/Rule/AC → Design → Contract → Work Item → Required Test以及反向合法来源；覆盖共享消费者和Profile交叉风险 |
| Exception Paths | 实验不能自动转正、Hotfix不绕审查、CR失效和重审链、P0/P1复测与测试纠错责任 |
| Quality | 对照 [adoption-level-matrix](../../references/adoption-level-matrix.md) 检验内容，不按文件数/标题数给PASS |

DELTA仍检查影响范围覆盖上述各维度及与未变部分交界，不能只看几行diff就宣布全项目通过。首次需逐项给出读取和覆盖记录。

## 4. Findings与Verdict

每条Finding：稳定ID、BLOCKER/MAJOR/MINOR/NOTE、来源文件/章节/版本、问题/风险、具体失败场景、受影响IDs/模块、Owning Stage、阻塞性、建议动作。BLOCKER和MAJOR必须解决；MINOR/NOTE保留Owner/处置，不为了找问题而创造新需求。

只有 BLOCKER=0、MAJOR=0、无未解决跨阶段矛盾和目标Shadow SOT、覆盖及来源证据可核验，Reviewer才可明确 `PRE_CODING_REVIEW_PASS`；否则 `PRE_CODING_REVIEW_FAIL`。无法核验的审查不是可用PASS，不能使用“基本通过”或用人类风险接受豁免严重Finding。

## 5. 修订复审

FAIL → Finding所属Stage修订 → 更新权威产物/关联任务和测试 → 按影响规则FULL/DELTA复审。保留所有历史Finding，不通过换模型/新报告隐藏未解决问题。连续复审无收敛时由Owner处理有证据的分歧或重新确认范围，不凭审查轮次强制给PASS。

PASS有效范围与失效条件只由review-validity定义；同一基线无需无意义重复全面阅读。

## 6. 留存与放行

使用 [Review Record](../../templates/INDEPENDENT_PRE_CODING_REVIEW.md)，保留原始报告、模型来源、包清单、覆盖、Finding、轮次、父报告、最终Verdict和适用IDs。Technical Owner核验后记录PRE_CODING_GATE_PASSED，再单独签发工作授权。

本次Skill修改的编制方不能把自己的检查记录写成独立模型PASS；SOP候选待外部复审时如实标PENDING。
