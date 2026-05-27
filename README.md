# paper-reading-zh

给 AI 加一套论文阅读的证据规则：未核验的不补，读不到的不编，比较前先对口径。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-v0.1.2-green.svg)](./CHANGELOG.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![LINUX DO](https://img.shields.io/badge/LINUX%20DO-Community-blue.svg)](https://linux.do)

本项目认可并感谢 [LINUX DO](https://linux.do) 社区。

`paper-reading-zh` 是一个中文论文精读规则包，面向 Codex、Claude Code、Claude Project 和 ChatGPT Project。它不是论文翻译器，也不是文献管理器；它的目标是让 AI 读论文时少一点顺滑猜测，多一点可复查的证据标注。

- **证据边界**：venue、年份、CCF、代码链接未核验就写“未核验”；实验数字必须锚定原文 Table / Figure 或具体段落。
- **防顺滑编造**：公式抽取乱码不硬补，图表读不到不描述，只能读到摘要时明确写“仅基于摘要”。
- **跨论文口径审计**：比较多篇论文前检查数据集、指标定义、模型规模、训练预算和测试 setting。
- **双入口复用**：同一套规则同时适配 Agent Skill 和 Web Prompt Kit，覆盖 CLI / Agent 环境与网页端项目。

## 适合谁

适合有 CS / AI / ML 基础，需要快速进入不熟悉方向的读者：

- 准备组会，需要把一篇论文讲清楚。
- 想从工程复现角度判断方法能不能落地。
- 要比较多篇论文，但不想把不同数据集、指标和模型规模混成一个结论。
- 经常用 AI 读论文，希望输出少一点猜测，多一点材料范围和证据标签。

非 CS 论文也可以读。规则会保留材料范围和证据边界，但不会强行输出 CCF 等级或工程复现建议。

## 平台支持

| 使用方式 | 适合场景 | 状态 |
|---|---|---|
| Claude Project | 网页端论文精读 | Primary |
| ChatGPT Project | 网页端论文精读 | Primary |
| Codex | CLI / Agent 环境 | Primary |
| Claude Code | CLI / Agent 环境 | Primary |
| Custom GPT | ChatGPT 可复用 GPT | Compatible |
| Hermes Agent | AgentSkills-compatible 运行时 | Compatible, not first-regression-tested |
| OpenClaw | AgentSkills-compatible 运行时 | Compatible, not first-regression-tested |

完整兼容矩阵和升级条件见 [DESIGN.md](./DESIGN.md#agent-compatibility)。

## 快速开始

### Web 用法

**Claude Project**

1. 新建 Claude Project。
2. 将 [prompts/claude-project.md](./prompts/claude-project.md) 粘贴到 Project instructions。
3. 上传论文 PDF，或粘贴论文链接 / 标题 / 摘要。
4. 提问：`精读这篇论文`、`按图表顺序讲`、`从工程复现角度拆一下`。

**ChatGPT Project**

1. 新建 ChatGPT Project。
2. 将 [prompts/chatgpt-project.md](./prompts/chatgpt-project.md) 粘贴到 Project instructions。
3. 上传论文 PDF，或粘贴论文链接 / 标题 / 摘要。
4. 提问：`精读这篇论文`、`比较这几篇论文`、`讲给组会新人听`。

Web 版的 PDF 图表读取能力由平台和模型决定；联网核验取决于当前平台是否有 web/search 能力。读不到时，规则要求先说明限制，再基于可读文本回答。

### Agent Skill 安装

从 GitHub clone 后安装：

```bash
git clone https://github.com/MrGeDiao/paper-reading-zh.git
cd paper-reading-zh
```

**Codex**

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R paper-reading-zh "${CODEX_HOME:-$HOME/.codex}/skills/"
```

**Claude Code**

```bash
mkdir -p "$HOME/.claude/skills"
cp -R paper-reading-zh "$HOME/.claude/skills/"
```

重启会话后，当你提供论文锚点并表达深读意图时自动触发。

<details>
<summary>Hermes Agent / OpenClaw 安装</summary>

**Hermes Agent**

```bash
mkdir -p "$HOME/.hermes/skills"
cp -R paper-reading-zh "$HOME/.hermes/skills/"
```

**OpenClaw**

```bash
mkdir -p "$HOME/.agents/skills"
cp -R paper-reading-zh "$HOME/.agents/skills/"
```

Hermes 和 OpenClaw 需要保留完整目录结构（包含 `references/modes.md`），不要用单文件 raw URL 安装。它们的兼容路径尚未完整回归测试。

</details>

## 阅读模式

| 模式 | 适合的问题 | 输出重点 |
|---|---|---|
| 深读模式 | 单篇论文精读 / 讲解 | 问题、贡献、方法机制、实验和局限 |
| 工程拆解模式 | 实现、复现、工程接入 | 数据流、模块职责、缺失细节、工程风险 |
| 调研比较模式 | 多篇论文比较、调研 | 任务假设、方法路线、证据强度、适用边界 |

可叠加子开关：

- **组会 / 技术博客风格**：加强“问题 -> 方法 -> 验证 -> 局限”的叙事链条。
- **按图表顺序组织**：按 Figure / Table / Equation / Algorithm 的出现顺序推进。

## 证据规则

这套规则最看重的是边界，而不是把回答写满。

- **外部事实**：venue、年份、CCF、代码链接、官方项目页必须核验。未核验写“未核验”，找过但没找到写“未找到”。可联网时按优先级核验 arXiv、OpenReview / ACM / IEEE / proceedings、Hugging Face Papers、Semantic Scholar / DBLP、官方项目页或仓库 README。
- **实验数字**：提升幅度、参数量、指标值必须能定位到原文 Table / Figure 编号或具体段落。数字只来自摘要时写“摘要中提到”。
- **实现细节**：论文没有说明的实现细节写“论文未说明”。工程拆解模式下，公式-代码对齐只在用户提供代码时启用。
- **跨论文比较**：检查数据集、评估协议、模型规模、训练预算、指标定义和测试 setting。不一致或未知时标注“口径不完全可比”或“口径未核验”。
- **图表与公式**：没有可读原文或用户提供的视觉内容时，不描述图表元素、坐标、曲线或趋势。

## 默认输出示例

```text
精读这篇论文：https://arxiv.org/abs/xxxx.xxxxx
```

默认输出结构：

- 关键词（不超过 5 个）
- 一段话总结（不超过 150 字）
- 论文基本信息：标题 / venue/年份 / 链接 / 任务领域
- 核心问题与贡献
- 方法深度解析
- 实验与结果
- 批判性讨论

只能读到摘要时，会明确写“仅基于摘要”，不会假装读完整篇。

## 项目状态

当前版本：`v0.1.2`

已有能力：

- 三种阅读模式和两个子开关。
- Agent Skill 和 Web Prompt Kit 双入口。
- Claude Project、ChatGPT Project、Codex、Claude Code 四个 Primary 平台。
- 外部事实核验路径、比较维度确认、跨论文口径审计。
- 模糊候选确认、公式-代码对齐（需用户提供代码）、调研比较表最小骨架。

验证状态：

`v0.1.1` 已完成一次真实 PDF 文本层最小验证，记录见 [docs/validation-2026-05-27.md](./docs/validation-2026-05-27.md)。这次验证使用一篇 16 页 PDF，覆盖材料范围说明、观点 / 路线图论文变体、实验和产业数字锚点、公式抽取乱码边界，以及 venue / CCF / 官方代码未核验时不补事实。

这不是所有平台的完整端到端回归。Claude Project、ChatGPT Project、Codex、Claude Code 仍会受到各自 PDF 读取、联网和上下文能力影响。

## 已知限制

- 尚未覆盖每个平台的完整端到端回归测试。
- Web 版不能调用本地工具；外部事实核验取决于当前平台是否可联网。
- PDF 图表读取能力由平台和模型决定；读不到时退化为基于文本、caption 或用户截图的解释。
- Markdown 数学渲染由客户端决定；部分客户端对行内 `$...$` 的渲染可能不稳定，规则会优先使用行内 `\(...\)` 或普通符号/中文术语兜底。
- 公式-代码对齐只在用户提供代码时启用，不默认 clone 或分析代码仓库。
- 这个项目不是文献管理器，也不默认生成 PPT、BibTeX 或全文翻译。

## 仓库结构

```text
paper-reading-zh/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── README.md
├── LICENSE
├── DESIGN.md
├── SECURITY.md
├── docs/
│   ├── release-v0.1.1.md
│   ├── release-v0.1.2.md
│   └── validation-2026-05-27.md
├── paper-reading-zh/
│   ├── SKILL.md
│   └── references/
│       └── modes.md
└── prompts/
    ├── README.md
    ├── claude-project.md
    └── chatgpt-project.md
```

## 设计说明

设计口径、兼容矩阵和证据规则的完整说明见 [DESIGN.md](./DESIGN.md)。

## License

MIT
