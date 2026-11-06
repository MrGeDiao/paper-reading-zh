# Design

这份文档记录 `paper-reading-zh` 的设计口径：规则放在哪、支持哪些平台、哪些事有意不做、验证做到了哪一步。面向维护者和贡献者；使用方法见 [README](./README.md)。

## 目标与范围

帮有大领域基础的中文读者，基于原文和可核验的外部信息，讲清论文的问题、方法或论证、图表公式、证据强度和局限。不是翻译器，也不是文献管理器。

默认优先服务 CS / AI / ML 论文。非 CS 论文可以读，但不强行输出 CCF 等级或工程复现建议。

适合：单篇精读、组会或技术博客式讲解、公式图表和实验拆解、工程复现与接入判断、多篇横向比较、核心主张与原文证据的逐项审计。

不适合：单段翻译、单个术语定义、只生成 BibTeX、只找或下载论文、默认全文翻译、生成 PPT。

## 规则放在哪

| 文件 | 作用 |
|---|---|
| `paper-reading-zh/SKILL.md` | 规则主入口：触发边界、材料范围、外部事实核验、证据规则、输出契约、自检。**规则以这里为准。** |
| `paper-reading-zh/references/modes.md` | 三个主模式和三个子开关的完整模板，按需读取 |
| `paper-reading-zh/references/paper-types.md` | 六种论文类型的识别原则、适用边界和主体骨架，按需读取 |
| `paper-reading-zh/agents/openai.yaml` | 可选 UI 元数据（Codex） |
| `prompts/project-instructions.md` | 网页端精简版，Claude Project 和 ChatGPT Project 共用，自包含，不超过 8000 字符 |

v0.5.0 之前网页端有 Claude、ChatGPT 两份 prompt，内容差异只有四处平台措辞，却要靠一张三列同步矩阵维护。现在合成一份，平台差异改写成“当前平台能否联网 / 能否看到图像”的条件句。

### 三层读法

- 主模式回答“用户想怎么读”：深读、工程拆解、调研比较。决定前置块和任务目标。
- 论文类型回答“材料靠什么建立贡献和证据”：标准方法 / 实验、系统 / 测量、数据集 / benchmark、理论 / 证明、综述 / 立场、观点 / 路线图。调整主体重点。
- 子开关调整组织方式：组会 / 技术博客风格、按图表顺序、证据审计，可叠加。

比较模式叠加类型或按图表时，仍保留“比较对象与材料范围 + 一句话结论”，不恢复单篇深读模板。深读附加节“复现/应用提示”的省略条件不限制工程拆解的“工程接入判断”。

### Web 版裁剪项

网页版保留全部约束，只省略细则。以下是有意不同步到网页版的内容：

| 规则 | 网页版 | 理由 |
|---|---|---|
| 只有论文锚点时不先做预检 | 不收 | 网页端没有预检工具链 |
| 直接写代码时的产物型分流 | 不收 | 网页端没有编码流程 |
| 触发边界与澄清 | 精简 | 保留单次澄清和不触发场景 |
| 高影响产业声明四级标注 | 精简 | 保留四级标签、自检和“不得写成独立证明” |
| 调研比较表骨架 | 精简 | 保留默认列和表后解释，不内联 Markdown 表格 |

其余规则（材料范围、训练记忆禁令、外部事实核验路径、数字锚点、乱码处置、比较口径、公式-代码对齐、论文类型骨架、证据审计、数学与术语、批判性四层、多轮继承、硬约束、轻量档位、自检）在两边完整存在。`scripts/check_rules.py` 检查两边的关键规则词是否一致，改规则时请同时更新这张表。

## 平台支持

| 级别 | 平台 | 状态 |
|---|---|---|
| Agent | Codex | Primary |
| Agent | Claude Code | Primary |
| Web | Claude Project | Primary |
| Web | ChatGPT Project | Primary |
| 兼容 | ChatGPT Skills beta | Compatible, not first-regression-tested |
| 兼容 | Hermes Agent、OpenClaw 等 AgentSkills 运行时 | Compatible, not first-regression-tested |
| 不支持 | Cursor rules、MCP server、浏览器扩展、opencode | Not supported |

Primary = 优先维护和验证；Compatible = 按格式预期可用，但没做过首轮完整回归。Agent Skill 只依赖 `SKILL.md`、YAML frontmatter 和 `references/` 渐进加载，没有脚本、外部工具调用或二进制依赖，这是兼容性判断的依据。

一个运行时从 Compatible 升到 Primary，至少要：

1. 安装或加载 `paper-reading-zh/`。
2. 触发深读、工程拆解、调研比较三个模式。
3. 确认 `references/modes.md` 与 `references/paper-types.md` 能按需读到。
4. 确认论文类型自适应和证据审计不破坏材料范围与防编造边界。
5. 用一篇真实论文跑完一次端到端输出，没有格式或证据边界漂移。

## 有意不做的事

- 不做脚本、MCP server 或自动下载论文的工具。skill 本体在任何能读文本的平台上都可用，也不引入默认联网抓取带来的版权和编造风险。`scripts/check_rules.py` 只用于维护，不是运行依赖。
- 不引入多 agent 调度、固定文献流水线、traceability manifest 或 claim id。证据审计只是一张按需输出的对照表。
- 不默认 clone 或分析代码仓库。公式-代码对齐只在用户提供代码时启用。
- 比较维度确认只在用户没给维度时触发，不增加默认追问。
- 默认输出不超过 3500 中文字。这限制的是交付篇幅，不是推理深度；改它需要一次版本决策。

## 验证现状

- `scripts/check_rules.py` 用标准库检查必要文件、触发描述、reference 链接、UI 元数据、声明式场景、两个入口的关键规则、网页版自包含与长度，以及仓库内相对链接。GitHub Actions 在 push 和 PR 时运行。它只核对文本，不等于模型行为实测。
- 行为实测记录在 [`docs/validation/`](./docs/validation/)，人工回归清单在 [`evals/trigger-cases.md`](./evals/trigger-cases.md)，声明式场景在 `evals/scenarios.json`。
- v0.4.0 在 Codex、Claude Code 上两轮跑 C1–C18：最终版 Codex 11/18、Claude Code 8/18 个主用例完成验证，其余受额度限制未验证，部分输出仍有格式偏差。
- 已知限制：模型认出知名论文后，可能用训练记忆冒充已读全文。v0.3.0 在 Codex 上经两轮规则修正仍复现过，v0.4.0 未复现，不代表以后不会发生。
- Claude Project、ChatGPT Project 还没有真实平台实测（v0.2.1 的三个 Web 场景只有预期记录）。

所以公开文案只写 Primary 或 Compatible，不写 “fully tested across all platforms”。

## 文档风格

README 和网页版 prompt 面向读者，不按 skill 规则文体写：

- 直接说这是什么、给谁用、解决什么问题。
- 保留必要术语，如“证据边界”“论文类型自适应”“证据审计”“批判性四层”。
- 不写“赋能”“重塑”“一站式”“革命性”“全方位”“智能化”等口号，不用 emoji 和装饰性图标。
- 不为了读起来顺删掉硬数字、字段限制、兼容性状态或证据边界。
- 示例必须来自真实运行，注明模型、版本和日期；可以节选，不改写内容。

用文风工具（如 [说人话](https://github.com/MrGeDiao/shuorenhua)）复查后，回核三件事：关键词不超过 5 个、总结不超过 150 字、基本信息默认 4 项；Primary / Compatible / not first-regression-tested / Not supported 没被软化；“未核验”“未找到”“摘要中提到”“论文未说明”等证据标签没被改写。

## 发版

CHANGELOG 的版本条目就是 GitHub Release 正文，不再单独写 `docs/release-*.md`。Release 标题格式 `paper-reading-zh vX.Y.Z - <主题>`，附件是仓库内 `paper-reading-zh/` 目录打成的 zip。改规则必须跑 `python3 scripts/check_rules.py`。

## Sources

- Agent Skills specification: https://agentskills.io/specification
- ChatGPT Projects: https://help.openai.com/en/articles/10169521-chatgpt-projects
- Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- ChatGPT File Uploads FAQ: https://help.openai.com/en/articles/8555545-file-uploads-faq
- Claude Projects: https://support.claude.com/en/articles/9517075-what-are-projects
- Claude file uploads: https://support.claude.com/en/articles/8241126-upload-files-to-claude
- Hugging Face Papers API skill reference: https://github.com/huggingface/skills/tree/main/skills/huggingface-papers
- Hermes skills: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md
- OpenClaw skills: https://github.com/openclaw/openclaw/blob/main/docs/tools/skills.md
