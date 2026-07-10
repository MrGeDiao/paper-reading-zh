# Web Prompt Kit

这个目录给不使用 CLI/Agent 的读者准备。把对应文件粘贴到 Claude Project 或 ChatGPT Project 的 instructions，再上传论文 PDF 或粘贴论文链接即可。

| 文件 | 用途 |
|---|---|
| `claude-project.md` | Claude Project instructions |
| `chatgpt-project.md` | ChatGPT Project instructions；文末包含 Custom GPT 补充说明 |

Custom GPT 用法见 `chatgpt-project.md` 文末；项目不单独维护一份 GPT 专用 prompt。

这些文件不是 AgentSkills 自动触发文件。它们不会调用本地工具，也不会自动读取 `paper-reading-zh/references/modes.md` 或 `paper-reading-zh/references/paper-types.md`；必要规则和类型骨架已经展开在 prompt 内。

Web 版和 Agent Skill 版共享同一套证据边界：

- 只基于可读材料回答。
- 只能得到摘要时，必须写“仅基于摘要”。
- 未核验外部事实写“未核验”，找过但没找到写“未找到”。
- 能联网时，按优先级核验 arXiv、OpenReview / ACM / IEEE、Hugging Face Papers、Semantic Scholar / DBLP 等。
- 跨论文 / 跨模型比较时，检查口径一致性；不一致时标注“口径不完全可比”或“口径未核验”。
- 论文未说明的实现细节写“论文未说明”。
- 看不到图表视觉内容时，不描述图表元素、坐标、曲线或趋势。
- 系统、benchmark、理论、综述和路线图等按主要贡献与证据结构选择类型，不硬套标准算法论文骨架。
- 证据审计输出核心主张、原文锚点、证据类型、支持强度依据和未覆盖问题；缺少证据不是反证。

如果要修改这些 prompt，请同步检查 `paper-reading-zh/SKILL.md`、`paper-reading-zh/references/modes.md` 和 `paper-reading-zh/references/paper-types.md`，并运行 `python3 scripts/check_rules.py`，避免 Web 版和 Agent 版行为漂移。
