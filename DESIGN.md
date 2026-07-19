# Design

`paper-reading-zh` 是一个中文论文精读规则包，面向两类使用场景：

- Web Prompt Kit：给 Claude Project、ChatGPT Project 等网页端项目使用。
- Agent Skill：给 Codex、Claude Code，以及兼容 AgentSkills-style skill folder 的运行时使用。

目标不是把论文翻译成中文，而是帮助读者基于原文和可核验外部信息，按论文的主要贡献与证据结构理解问题、方法或论证、图表公式、证据强度和局限。

## Scope

默认优先服务 CS / AI / ML 论文。非 CS 论文可以读，但不强行输出 CCF 等级或工程复现建议。

适合：

- 单篇论文精读。
- 组会或技术博客式讲解。
- 公式、图表、实验结果拆解。
- 工程复现或接入可行性判断。
- 多篇论文横向比较。
- 核心主张与原文证据的逐项审计。

不适合：

- 单段英文翻译。
- 单个术语定义。
- 只生成 BibTeX。
- 只下载 PDF 或找论文链接。
- 默认全文翻译或 PPT 生成。

## Agent Compatibility

本节是支持矩阵的单一事实源。README 和 prompts 只能引用或摘要本节，不应另起一套兼容承诺。

| Tier | Runtime | Intended use | Status |
|---|---|---|---|
| Tier 1 Web | Claude Project | 网页端论文陪读、组会准备、调研 | Primary |
| Tier 1 Web | ChatGPT Project | 网页端论文陪读、组会准备、调研 | Primary |
| Tier 1 Agent | Codex | Agent Skill 安装与触发 | Primary |
| Tier 1 Agent | Claude Code | Agent Skill 安装与触发 | Primary |
| Tier 2 | ChatGPT Skills beta | 支持 Skills 的 ChatGPT 工作区 | Compatible, not first-regression-tested |
| Tier 2 | Custom GPT | ChatGPT 内的可复用 GPT 配置 | Compatible, derived from `prompts/chatgpt-project.md` |
| Tier 2 | Hermes Agent | AgentSkills-compatible skill runtime | Compatible, not first-regression-tested |
| Tier 2 | OpenClaw | AgentSkills-compatible skill runtime | Compatible, not first-regression-tested |
| Not now | Cursor rules / IDE rules | 规则格式不同 | Not supported in v0.2 |
| Not now | MCP server | 本项目不是 MCP server | Not supported in v0.2 |
| Not now | Browser extension | 交互形态不同 | Not supported in v0.2 |
| Not now | opencode | 未核验安装与触发语义 | Not supported in v0.2 |

兼容性的依据：

- Agent Skill 形态只依赖 `SKILL.md`、YAML frontmatter 和 `references/` 渐进加载，不依赖平台专属 API；`agents/openai.yaml` 只提供可选 UI 元数据。
- 当前 skill 没有脚本、外部工具调用或本地二进制依赖。
- ChatGPT Skills beta、Hermes 和 OpenClaw 的兼容性基于公开格式与能力说明；本仓 v0.2 尚未对这些入口做首轮完整实机回归。

一个运行时从 Compatible 升到 Primary，需要至少完成：

1. 安装或加载 `paper-reading-zh/`。
2. 触发深读模式、工程拆解模式、调研比较模式。
3. 验证 `references/modes.md` 与 `references/paper-types.md` 能被按需使用。
4. 验证论文类型自适应与证据审计不会破坏材料范围和防编造边界。
5. 用一篇真实论文完成一次端到端输出，并确认没有格式或证据边界漂移。

## Public Surface

公开仓建议只发布：

```text
README.md
LICENSE
DESIGN.md
CHANGELOG.md
CONTRIBUTING.md
SECURITY.md
docs/release-v0.1.1.md
docs/release-v0.1.2.md
docs/release-v0.1.3.md
docs/release-v0.1.4.md
docs/release-v0.2.0.md
docs/release-v0.2.1.md
docs/validation-2026-05-27.md
docs/validation-2026-07-10-v0.2.0.md
docs/validation-2026-07-19.md
.github/ISSUE_TEMPLATE/bug_report.yml
.github/ISSUE_TEMPLATE/paper_misread.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/workflows/validate.yml
paper-reading-zh/SKILL.md
paper-reading-zh/agents/openai.yaml
paper-reading-zh/references/modes.md
paper-reading-zh/references/paper-types.md
prompts/README.md
prompts/claude-project.md
prompts/chatgpt-project.md
evals/scenarios.json
evals/fixtures/system-measurement.md
evals/fixtures/theory-damaged-extraction.md
evals/fixtures/evidence-audit.md
scripts/check_rules.py
```

工作记录、草稿和本地验证材料不属于公开发布面。未来如果从长期开发仓发布公开版本，不建议直接把完整开发历史改成 public；更稳妥的做法是创建干净公开仓，或使用 orphan public 分支，只发布上面的公开文件。

## Modes

### 深读模式

用于单篇论文的一般精读或讲解。默认结构：

```markdown
关键词：...

一段话总结：
...

论文基本信息：
- 标题：
- venue/年份：
- 链接：
- 任务领域：

1. 核心问题与贡献
2. 方法深度解析
3. 实验与结果
4. 批判性讨论
5. 复现/应用提示（条件性省略）
```

### 工程拆解模式

用于实现、复现、工程接入或可行性判断。重点是输入输出、模块职责、数据流、训练/推理流程、关键公式、复现缺口和工程风险。

用户提供代码仓库、代码片段或实现文件时，增加公式-代码对齐：比较论文公式 / 算法步骤 / 模块描述与代码中的函数、类、张量形状、超参数。对齐结果标注为：论文明确说明、代码实现、实现与论文不一致、论文未说明。非官方代码只能作为实现参考，不能当作论文事实。不默认 clone 或分析代码仓库；只在用户提供代码或明确要求时启用。

### 调研比较模式

用于多篇论文、综述和方法比较。重点是共同问题、不同假设、方法路线、实验设置、证据强度和适用边界。

如果用户没有给出明确比较维度，先给出默认维度让用户确认或修改，再填表和分析。默认维度包括任务 / 问题、核心机制、数据集 / 场景、关键指标、规模 / 成本和开源状态。默认紧凑比较表包含论文、年份、任务/问题、核心机制、关键结果、开源状态和口径/证据强度。用户确认的维度可替换或追加为表列。

### 子开关

- 组会 / 技术博客风格：加强“问题 -> 方法 -> 验证 -> 局限”的叙事链条。
- 按图表顺序组织：按 Figure / Table / Equation / Algorithm 的出现顺序推进；优先架构图、主结果表、消融表、关键公式和算法。
- 证据审计：把核心主张对到原文锚点、证据类型、支持强度依据和未覆盖问题；缺少证据不是反证。

## Paper Types

主模式回答“用户想怎么读”，论文类型回答“材料主要靠什么结构建立贡献和证据”。v0.2 支持：

- 标准方法 / 实验。
- 系统 / 测量。
- 数据集 / benchmark。
- 理论 / 证明。
- 综述 / 立场。
- 观点 / 路线图。

先确认实际可读材料，再按主要贡献与证据结构选主类型；混合型论文可说明次要类型，但不拼接多个完整骨架。仍无法判断时不强行贴类型标签，沿用主模式并只输出材料实际支持的章节。详细边界和主体骨架见 `paper-reading-zh/references/paper-types.md`。

## Material Scope

- 只有标题、简称或模糊引用且检索到多个候选时，列出最可能的 2-3 个候选让用户确认；确认后不重复确认。
- 候选与用户上下文明显不一致时，说明不一致点，不进入深读。
- 只能得到摘要时，写“仅基于摘要”，不进入完整深读。

## Evidence Rules

- 外部事实包括 venue、年份、CCF、代码链接、官方项目页和 arXiv 元数据。未核验写“未核验”；找过但没找到写“未找到”。
- 可联网或可读取外部页面时，优先核验 arXiv、OpenReview / ACM / IEEE / proceedings、Hugging Face Papers、Semantic Scholar / DBLP、官方项目页或仓库 README。
- Figure / Table / Equation / Algorithm 编号必须来自实际原文或用户提供内容。
- 实验、测量、路线图和产品数字必须能定位到原文 Section / Table / Figure / Sidebar / 页码或具体段落。
- 跨论文、跨模型、跨版本比较时，必须检查数据集、评估协议、模型规模、训练预算、指标定义和测试 setting；不一致或未知时标注“口径不完全可比”或“口径未核验”。
- 如果数字来自摘要，写“摘要中提到”。
- 论文未说明的实现细节写“论文未说明”。
- 不写“完全解决”“全面优于”“适用于所有场景”这类绝对化表达，除非论文和证据确实支持。
- 批判性讨论必须区分论文声明、证据支持、合理推断和不确定或未覆盖。
- 证据审计的支持强度必须解释依据；材料未给出直接证据时写“未见直接证据”或“无法判断”，不把缺证据写成反证。

## Web Prompt Boundaries

Web prompt 版本和 Agent Skill 版本共享同一套阅读规则，但能力边界不同：

- Web 版不能调用本地 shell、脚本或用户机器上的工具。
- Web 版的联网核验取决于当前平台是否有 web/search 能力。
- Web 版的 PDF 图表读取能力取决于平台和模型。看不到图表视觉内容时，只能基于可读文本、caption 或用户截图解释。
- Web 版不应声称自己完成了 Agent Skill 自动触发；它只是项目说明或自定义 instructions。

## Rule Sync Matrix

规则有三个落点：Agent Skill（`SKILL.md` + `references/modes.md`）、`prompts/claude-project.md`、`prompts/chatgpt-project.md`。
本表是同步状态的单一事实源。修改任何规则文件的 PR 必须重新核对受影响的行。
标记含义：完整 = 规则全文存在；精简 = 保留约束、省略细则；裁剪 = 有意不收编（附理由）；缺失 = 待修复的漂移。

| 规则簇 | Agent Skill | claude-project | chatgpt-project | 说明 |
|---|---|---|---|---|
| 适用领域边界 | 完整 | 完整 | 完整 | 三入口均优先服务 CS / AI / ML，非 CS 不强制 CCF 或工程建议。 |
| 触发边界与澄清 | 完整 | 精简 | 精简 | Web 保留单次澄清与不触发场景。 |
| 材料范围（含标题-only 兜底） | 完整 | 完整 | 完整 | 三入口均要求无可信材料时退出深读，不用猜测或训练记忆补内容。 |
| 外部事实核验路径 | 完整 | 完整 | 完整 | 三入口均列出核验来源与证据标签。 |
| 实验数字锚点 | 完整 | 完整 | 完整 | 三入口均要求定位到原文锚点。 |
| 高影响产业声明四级标注 | 完整 | 精简 | 精简 | Web 保留四级标签、自检与不得写成独立证明的边界。 |
| 观点 / 路线图论文变体 | 完整 | 完整 | 完整 | Web 已内联识别、边界、主体骨架与高影响声明规则。 |
| PDF 抽取乱码处置 | 完整 | 完整 | 完整 | 三入口均要求说明限制且不得基于乱码重构。 |
| 跨论文口径审计 | 完整 | 完整 | 完整 | 三入口均保留两类口径标签。 |
| 公式-代码对齐 | 完整 | 完整 | 完整 | Web 已内联启用条件、对齐对象与结果标签。 |
| 数学表达规则 | 完整 | 完整 | 完整 | 三入口均解释核心符号并限制纯叙述段堆叠 LaTeX。 |
| 术语规则 | 完整 | 完整 | 完整 | 三入口均支持最多 5 个主线必需词条的短术语表。 |
| 批判性四层 | 完整 | 完整 | 完整 | Web 将证据支持写为实验或形式证据支持。 |
| 多轮追问继承 | 完整 | 完整 | 完整 | 三入口均继承论文上下文、术语表、模式、论文类型和子开关。 |
| 输出前自检 | 完整 | 完整 | 完整 | 三入口均覆盖材料、类型、证据、数学、术语、风格和章节权重。 |
| 硬约束（字数 / 关键词 / 基本信息） | 完整 | 完整 | 完整 | 三入口的数字与字段限制一致。 |
| 调研比较表骨架 | 完整 | 精简 | 精简 | Web 保留默认列和表后解释要求，不内联 Markdown 表格。 |
| 只有论文锚点时不先做预检 | 完整 | 裁剪 | 裁剪 | Agent 专属；Web 无预检工具链，不适用。 |

## Documentation Style

README 和 prompts 面向读者，不按 skill 规则文体写。文案要求：

- 直接说这是什么、给谁用、解决什么问题。
- 保留必要术语，如“证据边界”“防编造”“论文类型自适应”“证据审计”“批判性四层”“图表顺序子开关”。
- 不写“赋能”“重塑”“一站式”“革命性”“全方位”“智能化”等口号。
- 不用 emoji 和装饰性图标。
- 不为了去 AI 味删掉硬数字、字段限制、兼容性状态或证据边界。

README 可以用中文文风复查工具（如开源的 shuorenhua 规则包）做去模板化复查，但复查后必须回核：

- 关键词不超过 5 个、总结不超过 150 字、默认基本信息 4 项。
- “Primary / Compatible / not first-regression-tested / Not supported” 等兼容性措辞没有被软化。
- “未核验”“未找到”“摘要中提到”“论文未说明”等证据标签没有被改写。

## v0.1 P0/P1 Design Summary

v0.1 包含以下规则增强，已落到 `SKILL.md`、`references/modes.md` 和两份 Web prompt 中：

| ID | 要求 | 落点 |
|---|---|---|
| P0-1 | 外部事实核验路径具体化 | `SKILL.md` 执行流程步骤 6；Evidence Rules |
| P0-2 | 调研比较先确认维度 | `references/modes.md` 比较维度确认；`SKILL.md` 步骤 7 |
| P0-3 | 跨论文口径审计 | `SKILL.md` 证据规则；`references/modes.md` 比较规则 |
| P1-1 | 模糊候选确认 | `SKILL.md` 材料范围步骤 3 |
| P1-2 | 公式-代码对齐 | `references/modes.md` 工程拆解模式；`SKILL.md` 证据规则 |
| P1-3 | 比较表最小列固定 | `references/modes.md` 紧凑比较表 |

## v0.2 Design Summary

| ID | 要求 | 落点 |
|---|---|---|
| V2-1 | 按主要贡献与证据结构选择论文类型 | `SKILL.md` 步骤 4；`references/paper-types.md` |
| V2-2 | 系统、benchmark、理论、综述等使用不同主体骨架 | `references/paper-types.md`；两份 Web prompt |
| V2-3 | 证据审计可与主模式和论文类型叠加 | `references/modes.md`；两份 Web prompt |
| V2-4 | 三入口核心规则漂移检查与 CI 门禁 | `scripts/check_rules.py`；`.github/workflows/validate.yml` |
| V2-5 | 声明式回归场景与可复现合成 fixture | `evals/scenarios.json`；`evals/fixtures/` |
| V2-6 | OpenAI UI 元数据 | `paper-reading-zh/agents/openai.yaml` |

设计约束：

- 不引入多 agent 调度、固定文献流水线、traceability manifest 或 claim id；证据审计只是一张按需输出的轻量对照表。
- 不默认联网下载论文、不默认 clone 或分析代码仓库。
- 公式-代码对齐只在用户提供代码时启用。
- 比较维度确认只在用户未指定维度时触发，不增加默认追问。

## Validation Status

当前状态：

- Skill 文件格式已通过 AgentSkills 风格的 frontmatter、名称和描述校验；OpenAI UI 元数据按当前字段约束生成并通过本仓校验。
- 仓库根目录提供 `scripts/check_rules.py`，用 Python 标准库检查必要文件、触发描述、reference 链接、UI 元数据、18 个场景、三入口关键规则和 Web prompt 自包含性；GitHub Actions 在 push / PR 时自动运行。
- 已用三份可复现合成 fixture 做隔离前向测试：系统 / 测量与证据审计完整通过；理论 / 证明输出正确拒绝重构损坏公式，但调用结束状态受外部会话额度影响，记录见 `docs/validation-2026-07-10-v0.2.0.md`。
- 已用一篇真实 16 页 PDF 完成文本层最小验证，覆盖材料范围、观点 / 路线图论文变体、数字锚点、公式抽取乱码边界和未核验外部事实标签；记录见 `docs/validation-2026-05-27.md`。
- v0.1.2 仅调整数学表达默认写法，未引入新的阅读模式或证据规则变更，不需要额外端到端验证。
- v0.1.4 修复「输出前自检」与正文相互矛盾的措辞，是把规则对齐到 v0.1.2 已发布意图，不引入新的阅读或证据行为，同样不需要额外端到端验证。
- 尚未完成 Claude Project、ChatGPT Project、Codex、Claude Code 四个平台的完整端到端回归测试。

因此公开文案只写“Primary”或“Compatible”，不写“fully tested across all platforms”。

## Sources

- ChatGPT Projects: https://help.openai.com/en/articles/10169521-chatgpt-projects
- Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Agent Skills specification: https://agentskills.io/specification
- GPTs in ChatGPT: https://help.openai.com/en/articles/8554407-create-a-custom-gpt
- ChatGPT File Uploads FAQ: https://help.openai.com/en/articles/8555545-file-uploads-faq
- Claude Projects: https://support.claude.com/en/articles/9517075-what-are-projects
- Claude file uploads: https://support.claude.com/en/articles/8241126-upload-files-to-claude
- Hugging Face Papers API skill reference: https://github.com/huggingface/skills/tree/main/skills/huggingface-papers
- Hermes skills: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md
- OpenClaw skills: https://github.com/openclaw/openclaw/blob/main/docs/tools/skills.md
