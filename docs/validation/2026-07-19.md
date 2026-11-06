# Validation 2026-07-19 — v0.2.1 Web entry parity

本记录描述更新后 Web prompt 的规则文本预期行为。由于当前执行环境无法访问真实 Claude Project 或 ChatGPT Project 会话，下面三个场景均明确标记为“未实测”，不构成平台验证通过的声明。

## Claude Project：标题-only 检索失败

### Material

- 入口：`prompts/claude-project.md`
- 输入：只提供真实论文标题 `A Time Scaling Theory for Multi-Layer Electronic Systems`。
- 环境前提：Claude Project 当前无法核验原文或元数据，用户未上传 PDF、正文或摘要。

### Expected

- 说明当前信息缺口并退出深读。
- 不基于常识或训练记忆补论文内容。
- 不编造 venue、作者、图表、公式、实验数字或代码链接。

### 实际行为

未实测。以上仅为 `prompts/claude-project.md` 材料范围规则所要求的预期行为。

### Result

未实测；不判定 PASS 或 FAIL。

### 剩余风险

真实 Claude Project 仍可能受模型版本、联网能力和 Project 文件状态影响，需由仓库所有者在真实平台复核退出深读与训练记忆禁令是否同时生效。

## Claude Project：观点 / 路线图论文

### Material

- 入口：`prompts/claude-project.md`
- 论文：`A Time Scaling Theory for Multi-Layer Electronic Systems`。
- 预定材料：与 `docs/validation-2026-05-27.md` 相同的真实 16 页 PDF；PDF 不入仓。

### Expected

- 保留关键词、一段话总结和论文基本信息前置块。
- 主体使用观点 / 路线图骨架：核心主张链条、证据类型与证据强度、关键产业 / 工程假设、可核验与未核验及作者预测、风险边界与适合追问的问题。
- 产品路线图、未发布芯片、内部 benchmark、供应链能力和生产数量等高影响内容使用“论文内部声明 / 作者预测 / 已公开第三方核验 / 未核验”标签。
- PDF 公式抽取异常时说明限制，不基于乱码重构公式、表格或图表。

### 实际行为

未实测。以上仅为 `prompts/claude-project.md` 论文类型、证据规则、材料范围和输出前自检共同要求的预期行为。

### Result

未实测；不判定 PASS 或 FAIL。

### 剩余风险

真实输出可能仍把标准方法 / 实验骨架与观点 / 路线图骨架混用，或漏掉个别高影响声明标签，需要在真实 Claude Project 中逐项检查。

## ChatGPT Project：链接不可读

### Material

- 入口：`prompts/chatgpt-project.md`
- 输入：只提供一个当前环境无法读取的论文链接，例如 `https://example.invalid/paper.pdf`。
- 用户未上传 PDF，也未粘贴正文或摘要。

### Expected

- 说明无法读取链接，请用户上传 PDF 或粘贴正文 / 摘要。
- 不进入深读，不基于训练记忆补论文内容。
- 只有个别元数据字段查不到时才使用“未核验”，不把整篇论文不可读降级成带“未核验”标签的完整深读。

### 实际行为

未实测。以上仅为 `prompts/chatgpt-project.md` 链接不可读规则所要求的预期行为。

### Result

未实测；不判定 PASS 或 FAIL。

### 剩余风险

真实 ChatGPT Project 的链接读取与 web search 状态可能改变分支判断，需要在关闭或无法使用链接读取能力的会话中复核阻断动作。

## Pending real-platform validation

真实平台实测是仓库所有者的待办项：在 Claude Project 执行前两个场景，在 ChatGPT Project 执行第三个场景，并如实记录模型、平台能力、实际输出、PASS / FAIL 和失败修正。完成前不得把本记录描述为“已在平台验证”。
