# paper-reading-zh

给 AI 加一套论文阅读的证据规则：未核验的不补，读不到的不编，比较前先对口径。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-v0.4.0-green.svg)](./CHANGELOG.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![LINUX DO](https://img.shields.io/badge/LINUX%20DO-Community-blue.svg)](https://linux.do)

An evidence-rule pack for AI-assisted paper reading. Docs and outputs are in Chinese by design.

`paper-reading-zh` 是一个中文论文精读规则包，面向 Codex、Claude Code、Claude Project 和 ChatGPT Project。它不是论文翻译器，也不是文献管理器；它的目标是让 AI 先判断材料和论文类型，再基于可定位证据解释结论，少一点顺滑猜测。

- **证据边界**：venue、年份、CCF、代码链接未核验就写“未核验”；实验数字必须锚定原文 Table / Figure 或具体段落。
- **防顺滑编造**：公式抽取乱码不硬补，图表读不到不描述，只能读到摘要时明确写“仅基于摘要”。
- **跨论文口径审计**：比较多篇论文前先检查数据集、指标定义、模型规模、训练预算和测试 setting。
- **论文类型自适应**：算法、系统/测量、数据集/benchmark、理论/证明、综述/立场、观点/路线图使用不同主体骨架。
- **证据审计**：可把核心主张逐项对到原文锚点、证据类型、支持强度和未覆盖问题。
- **双入口复用**：同一套规则同时提供 Agent Skill（CLI / Agent 环境）和 Web Prompt Kit（网页端项目）。

## 和直接把论文丢给 AI 的区别

经常用 AI 读论文的人大多见过这些行为：查不到 venue 就补一个像样的，只读到摘要却写出全文精读，两篇论文口径不同也直接判胜负。这套规则要求在这些地方说明依据和限制：

| 场景 | 无规则的典型行为 | 本规则下的输出 |
|---|---|---|
| venue / 代码链接查不到 | 凭印象补一个 | 写“未核验”；找过没找到写“未找到” |
| 只能读到摘要 | 当作读完整篇开始精读 | 写“仅基于摘要”，先问是否继续轻量解读 |
| 引用实验数字 | 复述时丢失出处 | 锚定到原文 Table / Figure 或段落，定位不到就不写 |
| 公式抽取乱码 | 凭记忆重构公式 | 说明 PDF 抽取异常，只解释上下文可确认的含义 |
| 多篇论文比较 | 按分数直接排名 | 先对数据集 / 指标 / 规模口径，不可比就标注“口径不完全可比” |
| 理论、benchmark 或路线图论文 | 一律硬套“方法 / 实验 / 结果” | 按主要贡献与证据结构选择论文类型；无法判断时不强套模板 |
| 用户要求证据审计 | 只给笼统的“有实验支持” | 列出主张、锚点、证据类型、支持强度依据和未覆盖问题 |

左列是常见失败模式的示意，不是对某个具体产品的实测记录；右列是规则的硬性要求。

## 输出长什么样

默认输出是不超过 3500 中文字的中等深读。关键词（不超过 5 个）、一段话总结（不超过 150 字）和论文基本信息（标题 / venue/年份 / 链接 / 任务领域 4 项）保持稳定；主体会按论文类型调整，不再把系统、理论、benchmark 或路线图论文硬塞进同一骨架。

证据标注落在输出里是这样的（依据一篇真实验证过的 16 页路线图论文改写的示意节选，完整记录见 [docs/validation-2026-05-27.md](./docs/validation-2026-05-27.md)）：

```text
论文基本信息：
- 标题：A Time Scaling Theory for Multi-Layer Electronic Systems
- venue/年份：未核验
- 链接：未找到
- 任务领域：多层电子系统的时间缩放理论（产业路线图）

……
- LogicFolding 在固定工艺节点带来 55% 密度提升、41% 能效提升（摘要 / page 1，论文内部声明）
- 2026 到 2035 年硬件集成增长预计大于 100 倍（page 1 / Sidebar B，作者预测）
- 第 4-5 页公式 PDF 抽取乱码：不基于乱码重构公式，只解释上下文可确认的含义
```

## 适合谁

适合有 CS / AI / ML 基础、需要快速进入不熟悉方向的读者：

- 准备组会，需要把一篇论文讲清楚。
- 想从工程复现角度判断方法能不能落地。
- 要比较多篇论文，但不想把不同数据集、指标和模型规模混成一个结论。
- 经常用 AI 读论文，希望输出少一点猜测，多一点材料范围和证据标签。

## 平台支持

| 使用方式 | 适合场景 | 状态 |
|---|---|---|
| Claude Project | 网页端论文精读 | Primary |
| ChatGPT Project | 网页端论文精读 | Primary |
| ChatGPT Skills beta | 支持 Skills 的 ChatGPT 工作区 | Compatible, not first-regression-tested |
| Codex | CLI / Agent 环境 | Primary |
| Claude Code | CLI / Agent 环境 | Primary |
| Custom GPT | ChatGPT 可复用 GPT | Compatible |
| Hermes Agent | AgentSkills-compatible 运行时 | Compatible, not first-regression-tested |
| OpenClaw | AgentSkills-compatible 运行时 | Compatible, not first-regression-tested |

Primary = 第一优先维护和验证的平台；Compatible = 按规则形态预期可用，但尚未完成首轮完整回归测试。完整兼容矩阵和升级条件见 [DESIGN.md](./DESIGN.md#agent-compatibility)。

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

**ChatGPT Skills beta**

如果你的 ChatGPT 工作区已经提供 Skills 上传入口，可以上传 GitHub Release 附带的 `paper-reading-zh-v0.4.0.zip`。该入口仍处于 beta，本项目尚未完成首轮 ChatGPT Skills 实机回归；没有该入口时继续使用上面的 ChatGPT Project prompt。

Web 版的 PDF 图表读取和联网核验能力由平台决定，详见[已知限制](#已知限制)；读不到时，规则要求先说明限制，再基于可读文本回答。

### Agent Skill 安装

```bash
git clone https://github.com/MrGeDiao/paper-reading-zh.git
cd paper-reading-zh
```

下面拷贝的是仓库内的 `paper-reading-zh/` 子目录（skill 本体），不是仓库根目录。

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

重启会话后试一句 `精读这篇论文：https://arxiv.org/abs/xxxx.xxxxx`。给出论文锚点（链接 / PDF / 标题）和阅读要求时自动触发；只给其中一样，会先问一次补齐另一样再继续。有论文时，「看看这篇」直接按深读处理；只说「帮我看看论文」而没有具体论文时，会先问是哪篇。

升级到新版本时，先删除 skills 目录下旧的 `paper-reading-zh/` 再重新拷贝；对已存在的目标目录直接 `cp -R` 不会覆盖旧版，只会嵌套出冗余的 `paper-reading-zh/paper-reading-zh/`。

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

Hermes 和 OpenClaw 需要保留完整目录结构（包含 `references/modes.md`、`references/paper-types.md` 和可选 UI 元数据），不要用单文件 raw URL 安装。它们的兼容路径尚未完整回归测试。

</details>

## 阅读模式

| 模式 | 适合的问题 | 示例提问 |
|---|---|---|
| 深读模式 | 单篇论文精读 / 讲解 | `精读这篇论文` |
| 工程拆解模式 | 实现、复现、工程接入 | `从工程复现角度拆一下` |
| 调研比较模式 | 多篇论文比较、调研 | `比较这几篇论文` |

模式由提问意图自动判断，不确定时默认深读，不需要背命令；也可以直接点名模式。主模式之外，规则还会按材料的主要贡献与证据结构选择论文类型：

- **标准方法 / 实验**：算法、模型、训练方法或技术机制，主要靠实验和消融验证。
- **系统 / 测量**：系统架构、真实部署、trace、采样和有效性威胁。
- **数据集 / benchmark**：数据构建、标注、划分、指标、泄漏、许可和维护。
- **理论 / 证明**：假设、定理、引理、证明依赖和适用范围。
- **综述 / 立场**：文献选择、分类框架、论证链、分歧和作者偏向。
- **观点 / 路线图**：趋势、产业假设、预测和高影响内部声明。

无法可靠判断类型时，不反复追问，也不强套标准算法论文模板，只保留当前材料实际支持的章节。三个子开关可以叠加：

- **组会 / 技术博客风格**（如 `讲给组会新人听`）：加强“问题 -> 方法 -> 验证 -> 局限”的叙事链条。
- **按图表顺序组织**（如 `按图表顺序讲`）：按 Figure / Table / Equation / Algorithm 的出现顺序推进。
- **证据审计**（如 `逐项核对哪些结论被实验支持`）：输出核心主张、原文锚点、证据类型、支持强度依据和未覆盖问题。

这些选项可以组合使用。比如「比较两篇 benchmark，按表格顺序讲」，仍以比较对象、材料范围和一句话结论开头；正文按各篇的表格顺序分析，不重复输出两份单篇深读。明确要求工程拆解时，benchmark 也会保留工程接入判断。

## 证据规则

这套规则最看重的是边界，而不是把回答写满。

- **外部事实**：venue、年份、CCF、代码链接、官方项目页必须核验。可联网时按优先级核验 arXiv、OpenReview / ACM / IEEE / proceedings、Hugging Face Papers、Semantic Scholar / DBLP、官方项目页或仓库 README；未核验写“未核验”，找过但没找到写“未找到”。
- **实验数字**：提升幅度、参数量、指标值必须能定位到原文 Table / Figure 编号或具体段落。数字只来自摘要时写“摘要中提到”。
- **实现细节**：论文没有说明的实现细节写“论文未说明”。工程拆解模式下，公式-代码对齐只在用户提供代码时启用。
- **跨论文比较**：检查数据集、评估协议、模型规模、训练预算、指标定义和测试 setting。不一致或未知时标注“口径不完全可比”或“口径未核验”。
- **图表与公式**：没有可读原文或用户提供的视觉内容时，不描述图表元素、坐标、曲线或趋势。
- **证据审计**：缺少证据时写“未见直接证据”或“无法判断”；缺少证据不是反证，也不会自动证明主张错误。
- **多轮追问**：可以沿用当前上下文中仍可核对的前轮原文；只有上轮回答或对话摘要时，需要重新读取原文或说明缺口。训练记忆不能充当材料来源。
- **PDF 读取范围**：按工具实际返回的页码或片段说明材料范围。读了前 11 页，就不能因为文件共有 15 页而声称读完全文。

## 已知限制

- v0.4.0 最终版完成了 Codex 11/18、Claude Code 8/18 个主用例；两处首轮发现的实质问题已复测，剩余用例因额度限制未完成最终版验证，部分已完成输出仍有格式偏差。首轮与最终版结果分开记录，见 [v0.4.0 验证记录](./docs/validation-2026-09-15-v0.4.0.md)。Claude Project、ChatGPT Project 因未登录而未实测，尚不能声称全平台完整回归。
- 历史验证包括真实 PDF 文本层测试、v0.2.0 合成材料测试和 v0.2.1 明确标为未实测的 Web 场景核对，入口见 [DESIGN 验证状态](./DESIGN.md#validation-status)。v0.3.0 的 Codex 首轮为 12 项中 11 项通过；模型认出知名论文后用训练记忆冒充已读全文的失败记录继续保留，见 [v0.3.0 验证记录](./docs/validation-2026-08-15.md)。本轮未复现，不代表以后一定不会发生。
- Web 版不能调用本地工具；外部事实核验取决于当前平台是否可联网。
- PDF 图表读取能力由平台和模型决定；读不到时退化为基于文本、caption 或用户截图的解释。
- Markdown 数学渲染由客户端决定；部分客户端对行内 `$...$` 的渲染可能不稳定，规则会优先使用行内 `\(...\)` 或普通符号/中文术语兜底。
- 公式-代码对齐只在用户提供代码时启用，不默认 clone 或分析代码仓库。
- 这个项目不是文献管理器，也不默认生成 PPT、BibTeX 或全文翻译。

## 反馈论文被读错

如果发现规则没拦住编造：venue 被补出来了、看不见的图表被描述了、实验数字没有锚点，请用 [paper_misread issue 模板](https://github.com/MrGeDiao/paper-reading-zh/issues/new?template=paper_misread.yml)反馈，附论文锚点和出错输出。这类案例会直接变成规则的回归用例。

## FAQ

**输出会不会到处都是“未核验”，显得啰嗦？**
默认是不超过 3500 字的中等深读，证据标签只出现在确实无法核验的字段上。可联网的环境会先按优先级核验，核验到了就写真实值。

**为什么不做成脚本、MCP server 或自动下载论文的工具？**
有意的设计约束：安装到运行时的 `paper-reading-zh/` skill 本体没有执行脚本和外部依赖，在任何能读文本的平台上都可用，也不引入“默认联网抓取”带来的版权与编造风险。仓库根目录的 `scripts/check_rules.py` 只用于维护和发布校验，不是用户运行依赖。完整设计约束见 [DESIGN.md](./DESIGN.md)。

**非 CS / AI 论文能用吗？**
可以。材料范围和证据边界照常生效，但不会强行输出 CCF 等级或工程复现建议。

## 版本与文档

变更记录见 [CHANGELOG.md](./CHANGELOG.md)，各版本发布说明见 [docs/](./docs/)。设计口径、兼容矩阵和公开文件清单见 [DESIGN.md](./DESIGN.md)，贡献方式见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 致谢

本项目认可并感谢 [LINUX DO](https://linux.do) 社区。

## License

MIT
