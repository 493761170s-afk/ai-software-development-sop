# Verification Change Control — 路由索引

测试验证冻结合同，不重新定义产品。分类、L0–L4、Fix Chain、停止条件、独立复测和QA收尾由 [Stage 7](../stages/07-integration-verification/SKILL.md)统一定义。

实现/回归缺陷 → 有边界的修复；测试错误 → 有依据且需独立核验的TEST_CORRECTION；环境问题 → 修环境；需求/设计/合同/必测标准改变 → [change-control](../utilities/change-control/SKILL.md)并按 [review-validity](review-validity.md)失效旧PASS和独立重审；新想法 → Backlog。

禁止通过环境、测试纠错、Hotfix或换缺陷编号把越界修改包装成正常修复。
