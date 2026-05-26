# Changelog

所有值得用户注意的变化都会记录在这里。版本号遵循轻量语义版本：规则或公开文档的兼容增强走 patch，小范围行为变化走 minor，破坏安装或输出契约再考虑 major。

## v0.1.1 - 2026-05-27

开源准备版本。

- 补齐公开协作入口：`CONTRIBUTING.md`、`SECURITY.md`、Issue 模板和 PR 模板。
- 增加真实论文最小端到端验证记录：`docs/validation-2026-05-27.md`。
- 将 `README.md` 和 `DESIGN.md` 的验证状态更新到当前事实：已有真实 PDF 文本层验证，但仍未宣称全平台完整回归。
- 为从 GitHub clone 后安装 Agent Skill 增加更直接的命令示例。

## v0.1 - 2026-05-20

首个可用版本。

- 提供 Agent Skill 入口：`paper-reading-zh/`。
- 提供 Web Prompt Kit：`prompts/claude-project.md` 和 `prompts/chatgpt-project.md`。
- 支持深读、工程拆解、调研比较三种模式，以及组会 / 技术博客风格、按图表顺序组织两个子开关。
- 建立证据边界：未核验外部事实不补、实验数字需要原文锚点、图表不可读时不描述视觉细节。
- 加入 P0/P1 规则增强：外部事实核验路径、比较维度确认、跨论文口径审计、模糊候选确认、公式-代码对齐、比较表最小骨架。
