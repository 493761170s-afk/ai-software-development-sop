---
name: change-control
description: 对Scope、规则、设计行为、技术合同、NFR、工作边界和必测标准的变更进行影响分析、Owner批准、旧PASS失效及独立重审，阻止开发/测试/热修复阶段静默扩范围。
---

# Change Control

所有执行模式、实验转入和事故修复均适用。Owning Source保存事实，CR保存变更决策，不创建第二份产品规格。

## 1. 分类与入口

Scope、Requirement/Rule、Design Behavior、Contract（API/DB/Event/File/AI输出/Provider）、NFR、Release Pull-in、WBS/Dependency/Work Boundary、Required Tests变化都要先评估实质影响。纯Experience Tweak不是自动豁免：文案可能改变用户承诺，按钮位置可能改变流程。

能证明只是实现违反原合同则登记Defect；没有可引用正确标准时先登记Gap，不能让Coding者自己补规则。口头批准须记录真实原文与上下文，未记录不能直接开写。

## 2. 执行顺序

CR登记 → 语义diff和影响闭包 → 暂停受影响/未知消费者 → 有权Owner决定批准/拒绝/延期 → 更新拥有事实的Stage 1–5产物及其WBS/测试 → 明确独立重审 → 新PASS和Gate核验 → 重新授权相应工作。

批准权见 [decision-rights](../../references/decision-rights.md)；影响算法、FULL/DELTA及非实质变更证据见 [review-validity](../../references/review-validity.md)。确认实质变更时立即标记旧PASS在影响范围INVALIDATED；尚未实施的变更可以拒绝/延期，但必须保留决定和范围恢复依据。

## 3. 不可省略的独立重审

上述实质变化必须调用 [independent-pre-coding-review](../independent-pre-coding-review/SKILL.md)。Product/Technical Owner批准CR不等于Reviewer PASS；原编制模型自审不算重审。先重审再开始受影响正式Coding，禁止“热修复先上、若干小时后补CR/重审”。

无父基线、影响无法封闭、关键资料不可读或Reviewer要求时用FULL；DELTA必须提供父报告、全部未决Finding、源内容diff、影响与排除证据及交叉Profile/消费者验证。未受影响范围不能只靠修改者口头声明。

## 4. 输出

使用 [CHANGE_REQUEST](../../templates/CHANGE_REQUEST.md)：变更原因/价值、分类、来源ID、影响集合与未知项、Owner决定、排期/依赖/风险、失效测试和Review、重审类型/身份/原始报告、新PASS、授权恢复范围。若拒绝或延期，维持原合同，不把建议偷偷放进本期缺陷。
