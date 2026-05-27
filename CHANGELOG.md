# Changelog

所有值得用户注意的变化都会记录在这里。版本号遵循轻量语义版本：规则或公开文档的兼容增强走 patch，小范围行为变化走 minor，破坏安装或输出契约再考虑 major。

## v0.1.2 - 2026-05-27

规避 Codex Desktop 等客户端对行内 dollar-style LaTeX 渲染不稳定的问题。

- 行内短公式默认从 `$...$` 改为 `\(...\)`；仅在当前平台明确支持 dollar-style 时才回退 `$...$`，且要求两侧保留 ASCII 空格或标点边界。
- 单个变量出现在中文叙述中时，优先用中文术语或普通符号（`x`、`y`），减少 `$x$` 这类容易漏渲染的裸行内公式。
- 核心希腊字母符号示例从 `$\tau$` 改为 `\(\tau\)`，与新默认写法一致。
- 以上变更同步到 `paper-reading-zh/SKILL.md`、`prompts/claude-project.md` 和 `prompts/chatgpt-project.md`。
- 行间公式仍使用 `$$...$$`，未改动。

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
