# Contributing

谢谢你愿意改进 `paper-reading-zh`。这个项目的核心不是让回答更长，而是让中文论文精读更可靠：材料范围清楚、外部事实可核验、实验数字有锚点、看不到的图表不编造。

## 可以贡献什么

- 修正规则里不清楚或容易误触发的地方。
- 补充真实论文验证案例，尤其是摘要-only、PDF 图表不可读、标题模糊、多论文比较等边界场景。
- 改进 Web Prompt Kit 和 Agent Skill 的一致性。
- 报告某篇论文被读错、venue/代码链接被编造、图表或实验数字被错误引用的案例。

## 修改规则时的同步要求

本仓有两个入口：Agent Skill 和 Web Prompt Kit。改其中一边时，请同步检查另一边。

- Agent Skill：`paper-reading-zh/SKILL.md`、`paper-reading-zh/references/modes.md`
- Web Prompt Kit：`prompts/claude-project.md`、`prompts/chatgpt-project.md`
- 设计事实源：`DESIGN.md`

如果只改 README 或维护文件，说明不影响运行规则即可。

## 提交前自检

请至少检查：

- 是否没有扩大平台兼容承诺，例如把未回归的平台写成 fully tested。
- 是否保留“未核验”“未找到”“摘要中提到”“论文未说明”等证据标签。
- 是否没有把内部讨论、私有路径、未授权论文内容或 API key 放进公开文件。
- 如果改了输出结构，是否补充或更新了一个最小验证案例。

## Pull Request 建议

PR 里请说明：

- 改了哪个入口：Agent Skill、Web Prompt Kit、文档，或三者都有。
- 影响哪个模式：深读、工程拆解、调研比较、按图表顺序，或仅维护文档。
- 用什么论文或场景做过验证；如果没有验证，请直说原因。

项目偏好小而可审的改动。不要把未来路线图、私人讨论稿或大段未验证承诺混进同一个 PR。
