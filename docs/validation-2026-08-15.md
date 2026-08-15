# Validation 2026-08-15 (v0.3.0 trigger regression)

本记录是 `docs/trigger-regression-cases.md` 的首轮实机回归结果，覆盖 v0.3.0 的触发边界与输出契约改动。它不是论文精读正文；验证用 PDF 不作为本仓库发布资产。

## Environment

- 平台：Codex CLI 0.147.0，`codex exec` 非交互模式，macOS。
- 模型：`gpt-daybreak-blue-latest`，reasoning effort high（仓库所有者本机配置）。
- 沙箱：C1-C12 使用 `--sandbox workspace-write`（文件可写、无网络，`curl` 实测 `Could not resolve host`）；C9 复测系列使用 `--sandbox read-only` 于空目录。
- Skill 安装：将本仓 `paper-reading-zh/` 复制到 `~/.codex/skills/paper-reading-zh`（替换前已备份旧版）。
- 材料：arXiv 1706.03762 v7《Attention Is All You Need》PDF（实下载，15 页文本层完好）；合成乱码抽取文本（含损坏的 Equation 3/4、错位 Table 1、无图像的 Figure 2/3 caption）；C9 另用从该 PDF 实抽并清理的摘要文本。
- 触发判定证据：`--json` 事件流中是否出现读取 `~/.codex/skills/paper-reading-zh/SKILL.md` / `references/*.md` 的命令（下表「加载」列），加上最终消息的行为形态。

环境限制（如实记录）：

- Claude Code CLI 在本机的登录态失效，无法非交互修复，本轮未能作为第二个 Primary 平台执行；Claude Code 侧仅验证了新 frontmatter 在其 skill 列表中完整展示（826 字符未截断）。
- Codex 在本机多 skill 环境（8 个 skill）下提示 "Skill descriptions were shortened to fit the skills context budget"，探测确认本 skill description 被截短到 250 字符以内：单边入口短语、意图词表与排除列表在路由层不可见，路由主要依赖开头的「中文论文精读工作流。Use when the user provides a paper anchor …」，精细边界靠触发后加载的 SKILL.md 正文兜底。本轮 12 个用例的行为均由正文规则正确接管，但 description 截断是平台预算行为，随用户安装的 skill 数量变化。

## Results

| 用例 | 输入要点 | 加载 | 实际首步行为 | 判定 |
|---|---|---|---|---|
| C1 纯 PDF 零附言 | 仅 PDF 路径 | 是 | 澄清一次：「深度精读 / 工程实现拆解 / 主张与证据审计 / 与其他模型比较」 | 通过 |
| C2 PDF+看看这篇 | 泛化动词 | 是（含 modes.md） | 直接进入默认深读，无澄清；材料范围声明 15 页实读，关键词 5 个、总结单段、基本信息 4 项，数字锚定 Table 1 / Figure 1-5 | 通过 |
| C3 模糊标题+精读 | 「scaling laws 那篇」 | 是 | 列出 2 个候选（Kaplan 2020 / Chinchilla 2022）让用户确认，未进入深读 | 通过 |
| C4 总结+PDF | 总结意图 | 是 | 轻量档位：只输出关键词、一段话总结、基本信息 4 项，未展开第 1-5 节 | 通过 |
| C5 按论文实现 | 产物型请求 | 是 | 给出压缩要点（公式、掩码、数值稳定 softmax）后让位编码，产出可运行 `self_attention.py`，未写六节报告 | 通过 |
| C6 纯翻译 | 单句英文 | 否 | 直接翻译，未进入精读流程 | 通过 |
| C7 仅 BibTeX | BibTeX+PDF | 是 | 只输出 BibTeX 与版本建议，未进入精读流程 | 通过 |
| C8 比较三篇 | 三个标题 | 是（含 modes.md） | 调研比较模式：先给比较维度清单请用户确认后再展开 | 通过 |
| C9 只有摘要+精读 | 实抽摘要文本 | 是 | 见下节：知名论文记忆冒充材料，三轮复现 | 未通过 |
| C10 乱码抽取+按图表 | 合成损坏文本 | 是（含 modes.md） | 按 Equation/Figure/Table 顺序推进；声明「Equation 3/4、Table 1 损坏」「符号已损坏，不能可靠还原」；venue/链接写「材料未提供」；推断处标「合理推断」 | 通过 |
| C11 PDF+讲给组会新人 | 组会子开关 | 是（含 modes.md） | 深读+组会风格：叙事链条、Q/K/V 直觉化讲解，前置块与硬约束保持 | 通过 |
| C12 能不能落地 | 可行性意图 | 是 | 工程拆解模式：落地结论（Top-K 精排器）、复现缺口（排序损失、延迟方案标注「不是论文原方案」）、`O(n^2 d)` 锚定 Table 1、代码可用性写「未联网核验」 | 通过 |

备注：

- C3 在断网环境下候选与链接来自模型知识，属于「待用户确认的候选提议」形态；链接未核验。
- C7 的 skill 正文被读取后按排除规则退出，与「完全不路由」存在差异，源于上述 description 截断；最终行为符合排除场景要求。BibTeX 字段来自模型知识，本用例只判定「不进入精读流程」。
- C8 给出的维度为语义改编（研究问题、架构、训练目标与数据、任务适配、实验证据、规模成本），未逐字使用规则默认六维度，判定按「先给维度并请确认」的行为形态通过，记为轻微漂移。
- C9 首跑（workspace-write，测试目录内存在同论文 PDF）被环境污染：模型主动发现并实读了本地 PDF 后正常深读，该跑不计入判定，用例改在空目录 read-only 复测。

## C9 失败记录与修正循环

复测环境：空目录、`--sandbox read-only`、无网络。三次运行事件流均显示模型仅读取 skill 文件、未读取任何论文材料。

1. 第 1 次（规则修正前）：输出「材料范围：基于 arXiv v7 全文与 NIPS 2017 正式论文」并展开完整深读，给出 Equation 1、Section 3.2.1 等记忆锚点。未通过。
2. 修正 A（commit `Bar training memory from claimed material scope`）：三入口材料范围新增总则「训练记忆不是可读材料……不要声称已读全文」，输出前自检同步强化。复测仍声称「已核对 arXiv v7 全文」。未通过。
3. 修正 B（commit `Treat recognized papers without fetched text as abstract-only`）：三入口「只能得到摘要」条目锁死判定入口（「即使认出论文并记得其内容，也按只能得到摘要处理」）。复测仍声称「已读取 arXiv v7 全文」。未通过。
4. 对照组 C9S：同环境改用一段合成论文摘要（模型不可能有训练记忆）。输出「目前只有摘要，无法做完整精读……或者确认我先做『仅基于摘要』的轻量解读」，行为完全符合摘要兜底。通过。

结论：摘要兜底机制本身工作正常（C9S）；未通过的失败模式特定于「超高知名度论文触发训练记忆冒充已读材料」，在被测模型上经两轮规则措辞强化仍复现，定性为模型层已知限制而非规则缺失。两条新增规则保留（对遵循材料声明更严格的模型有效，且为其他场景提供总则依据）；不再为单一模型行为继续堆叠规则文本。

## Result

- 12 个固化用例全部完成实测：11 个通过，C9 未通过（已知限制，附三跑记录与对照组证据）。
- v0.3.0 新增行为全部得到正向验证：单边锚点触发并澄清一次（C1）、泛化阅读动词直入深读（C2）、总结轻量档位（C4）、产物型请求分流（C5）、维度确认（C8）。
- 本轮仅覆盖 Codex 单平台；Claude Code、Claude Project、ChatGPT Project 的同清单回归仍为仓库所有者待办。
