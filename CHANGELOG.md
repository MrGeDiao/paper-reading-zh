# Changelog

所有值得用户注意的变化都会记录在这里。版本号遵循轻量语义版本：规则或公开文档的兼容增强走 patch，小范围行为变化走 minor，破坏安装或输出契约再考虑 major。

## v0.2.0 - 2026-07-10

论文类型自适应与证据审计版本。

- 新增论文类型层：标准方法 / 实验、系统 / 测量、数据集 / benchmark、理论 / 证明、综述 / 立场、观点 / 路线图按主要贡献与证据结构选择不同主体骨架。
- 类型判断改为先确认实际可读材料，再分类；无法可靠分类时不反复追问，也不强行套标准算法论文模板。
- 新增可叠加的“证据审计”子开关，输出核心主张、原文锚点、证据类型、支持强度依据和未覆盖问题，并明确“缺少证据不是反证”。
- Agent Skill、Claude Project prompt、ChatGPT Project prompt 补齐观点 / 路线图、高影响产业声明、PDF 抽取乱码、无可信材料退出、非官方代码和跨论文口径等核心规则。
- 将详细论文类型规则拆到 `paper-reading-zh/references/paper-types.md`，保持主 `SKILL.md` 的渐进加载；frontmatter 触发描述从 586 个字符压缩到 144 个字符。
- 新增 `paper-reading-zh/agents/openai.yaml`，为支持该元数据的 OpenAI 产品提供显示名称、短描述和默认提问。
- 新增 18 个声明式回归场景、3 份可复现合成 fixture 和无第三方依赖的 `scripts/check_rules.py`，检查 frontmatter、reference、UI 元数据、三入口关键行为与 Web prompt 自包含性；GitHub Actions 在 push / PR 时自动运行。
- 仓库自带校验全部通过；系统 / 测量、理论 / 证明和证据审计三组隔离前向测试结果见 `docs/validation-2026-07-10-v0.2.0.md`。
- 新增 ChatGPT Skills beta 的兼容说明和 GitHub Release skill 压缩包；该入口尚未完成首轮实机回归。

## v0.1.4 - 2026-07-01

文档一致性修补，不改变已发布的阅读规则行为。

- 修复 v0.1.2 遗留的自检与正文矛盾：`paper-reading-zh/SKILL.md` 及两份 Web prompt 的「输出前自检」原“公式是否全部使用 LaTeX”改为“公式与多符号表达式是否使用 LaTeX；叙述段的单个变量是否未被强行包成行内公式”，避免严格执行自检时把叙述里的裸变量重新包回行内公式。
- 数学规则反例文本从 `$x$`、`$y$` 更新为 `\(x\)` 或 `$x$`，与 v0.1.2 的行内公式新默认写法一致（`paper-reading-zh/SKILL.md` 及两份 Web prompt 三处同步）。
- 触发词“可行性判断”同步到两份 Web prompt 的深读意图列表，与 SKILL.md 及各自工程拆解模式的措辞对齐。
- `.github/ISSUE_TEMPLATE/bug_report.yml` 的版本示例改为版本无关写法，不再随发版过时。
- `DESIGN.md` 去除对公开读者无出处、不可复现的内部工具名（`quick_validate.py`、裸 `shuorenhua`），并移除 v0.1.3 引入的 Maintenance Provenance 段，改为可核验的表述。
- README 版本标识更新到 `v0.1.4`，并去掉“版本与文档”里随发版过时的单行版本说明。

## v0.1.3 - 2026-06-17

文档规划和维护溯源版本。

- 在 `DESIGN.md` 中补充维护溯源说明，明确本次更新采用 `tri-collab` 式本地维护工作流；它不是 `paper-reading-zh` 的运行时依赖或用户安装步骤。
- 新增 `docs/release-v0.1.3.md`，记录本次文档更新的范围、决策依据和已知限制。
- 更新 README 版本标识和仓库结构。
- 本版本不修改 `paper-reading-zh/SKILL.md`、`paper-reading-zh/references/modes.md` 或 Web Prompt Kit；阅读模式、证据规则和兼容矩阵均无变化。

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
