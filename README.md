# paper-reading-zh

中文论文精读规则包：把论文 PDF、arXiv / OpenReview / ACM / IEEE 链接、论文标题或多篇论文列表，变成有证据边界的中文深读输出。

## 这是什么

`paper-reading-zh` 是一组可复用的论文精读规则，有两种入口：

- **Agent Skill** — 放进 Codex、Claude Code 或其他兼容 AgentSkills 的运行时，自动触发。
- **Web Prompt Kit** — 粘贴到 Claude Project 或 ChatGPT Project 的 instructions，网页端即可使用。

两种入口共享同一套证据边界和阅读规则。目标不是翻译论文，而是帮读者讲清问题、方法机制、图表公式、实验验证和局限；不编造未核验的 venue、CCF、代码链接和实验数字。

## 适合谁

有 CS / AI / ML 大领域基础，需要快速精读不熟悉的小方向论文的读者。典型场景：

- 单篇论文精读或组会准备。
- 从工程复现角度拆解论文。
- 多篇论文横向比较和调研。

非 CS 论文也可以读，但不强行输出 CCF 等级或工程复现建议。

## 平台支持

| 使用方式 | 适合谁 | 状态 |
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

**Claude Project：**

1. 新建 Claude Project。
2. 将 [prompts/claude-project.md](./prompts/claude-project.md) 粘贴到 Project instructions。
3. 上传论文 PDF，或粘贴论文链接 / 标题 / 摘要。
4. 提问：`精读这篇论文`、`按图表顺序讲`、`从工程复现角度拆一下`。

**ChatGPT Project：**

1. 新建 ChatGPT Project。
2. 将 [prompts/chatgpt-project.md](./prompts/chatgpt-project.md) 粘贴到 Project instructions。
3. 上传论文 PDF，或粘贴论文链接 / 标题 / 摘要。
4. 提问：`精读这篇论文`、`比较这几篇论文`、`讲给组会新人听`。

Web 版的 PDF 图表读取能力由平台和模型决定；联网核验取决于当前平台是否有 web/search 能力。读不到时，规则要求先说明限制再基于可读文本回答，不会假装看到了内容。

### Agent Skill 安装

从 GitHub clone 后安装：

```bash
git clone https://github.com/MrGeDiao/paper-reading-zh.git
cd paper-reading-zh
```

**Codex：**

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R paper-reading-zh "${CODEX_HOME:-$HOME/.codex}/skills/"
```

**Claude Code：**

```bash
mkdir -p "$HOME/.claude/skills"
cp -R paper-reading-zh "$HOME/.claude/skills/"
```

重启会话后，当你提供论文锚点并表达深读意图时自动触发。

**Hermes Agent：**

```bash
mkdir -p "$HOME/.hermes/skills"
cp -R paper-reading-zh "$HOME/.hermes/skills/"
```

**OpenClaw：**

```bash
mkdir -p "$HOME/.agents/skills"
cp -R paper-reading-zh "$HOME/.agents/skills/"
```

Hermes 和 OpenClaw 需要保留完整目录结构（包含 `references/modes.md`），不要用单文件 raw URL 安装。它们的兼容路径尚未完整回归测试。

## 三种模式

| 模式 | 适合的问题 | 输出重点 |
|---|---|---|
| 深读模式 | 单篇论文精读 / 讲解 | 问题、贡献、方法机制、实验和局限 |
| 工程拆解模式 | 实现、复现、工程接入 | 数据流、模块职责、缺失细节、工程风险 |
| 调研比较模式 | 多篇论文比较、调研 | 任务假设、方法路线、证据强度、适用边界 |

可叠加子开关：

- **组会 / 技术博客风格**：加强“问题 -> 方法 -> 验证 -> 局限”的叙事链条。
- **按图表顺序组织**：按 Figure / Table / Equation / Algorithm 的出现顺序推进。

## 证据边界

这套规则的核心约束：

- venue、年份、CCF、代码链接、官方项目页必须核验；未核验写“未核验”，找过但没找到写“未找到”。
- 可联网时，按优先级核验 arXiv、OpenReview / ACM / IEEE / proceedings、Hugging Face Papers、Semantic Scholar / DBLP、官方项目页或仓库 README。
- 具体实验数字、提升幅度、参数量、指标值必须能定位到原文 Table / Figure 编号或具体段落。
- 如果数字只来自摘要，必须写“摘要中提到”。
- 跨论文、跨模型、跨版本比较时，检查数据集、评估协议、模型规模、训练预算、指标定义和测试 setting；不一致或未知时标注“口径不完全可比”或“口径未核验”。
- 论文没有说明的实现细节写“论文未说明”，不用合理猜测补齐。
- 没有可读原文或用户提供的视觉内容时，不描述图表元素、坐标、曲线或趋势。

## v0.1 主要能力

基础能力：

- 三种阅读模式和两个子开关。
- 证据边界和防编造规则。
- Agent Skill 和 Web Prompt Kit 双入口。
- Claude Project、ChatGPT Project、Codex、Claude Code 四个 Primary 平台。

P0/P1 规则增强（v0.1 包含）：

- **外部事实核验路径**：明确 arXiv、OpenReview、Hugging Face Papers、Semantic Scholar / DBLP 等核验优先级，而非只说“需要核验”。
- **比较前确认维度**：调研比较模式下，如果用户没有给出明确比较维度，先给默认维度（任务、核心机制、数据集、关键指标、规模/成本、开源状态）让用户确认。
- **跨论文口径审计**：跨论文 / 跨模型 / 跨版本比较时，检查数据集、评估协议、模型规模等是否一致；不一致时降低结论强度。
- **模糊候选确认**：只给标题或简称且检索到多个候选时，列出 2-3 个候选让用户确认，避免读错论文。
- **公式-代码对齐**：工程拆解模式下，用户提供代码时，对齐论文公式 / 算法与代码中的函数、类、张量形状；区分“论文明确说明 / 代码实现 / 不一致 / 论文未说明”。
- **调研比较表最小骨架**：默认紧凑比较表包含论文、年份、任务/问题、核心机制、关键结果、开源状态和口径/证据强度。

## 验证状态

`v0.1.1` 已增加一次真实 PDF 文本层最小验证，记录见 [docs/validation-2026-05-27.md](./docs/validation-2026-05-27.md)。这次验证覆盖了材料范围说明、观点 / 路线图论文变体、实验和产业数字锚点、公式抽取乱码边界，以及 venue / CCF / 官方代码未核验时不补事实。

这不等于所有平台的完整端到端回归。Claude Project、ChatGPT Project、Codex、Claude Code 仍会受到各自 PDF 读取、联网和上下文能力影响。

## 默认输出示例

```text
精读这篇论文：https://arxiv.org/abs/xxxx.xxxxx
```

输出结构：

- 关键词（不超过 5 个）
- 一段话总结（不超过 150 字）
- 论文基本信息：标题 / venue/年份 / 链接 / 任务领域
- 核心问题与贡献
- 方法深度解析
- 实验与结果
- 批判性讨论

只能读到摘要时，会明确写“仅基于摘要”，不会假装读完整篇。

## 已知限制

- v0.1.1 已做一次真实 PDF 文本层最小验证，但还没有覆盖每个平台的完整端到端回归测试。当前主要验证的是规则结构、Agent Skill 文件格式、Web prompt 的可迁移性和证据边界的最小真实样例。
- Web 版不能调用本地工具；外部事实核验取决于当前平台是否可联网。
- PDF 图表读取能力由平台和模型决定；读不到时退化为基于文本、caption 或用户截图的解释。
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

`tasks/` 是私有开发过程稿，不在公开发布范围内。

## 设计来源

这个项目来自一组中文论文阅读提示词、Linux.do 论文阅读讨论，以及 Codex / Claude Code 的多轮设计评审。设计口径和兼容矩阵见 [DESIGN.md](./DESIGN.md)。

## License

MIT
