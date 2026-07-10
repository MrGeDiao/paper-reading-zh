# paper-reading-zh v0.2.0

`v0.2.0` 是第一个扩展阅读行为的 minor 版本，主题是“按论文类型读”和“把主张对回证据”。

## Highlights

- 新增论文类型自适应：系统 / 测量、数据集 / benchmark、理论 / 证明、综述 / 立场和观点 / 路线图不再硬套标准算法论文骨架。
- 新增证据审计子开关：逐项输出核心主张、原文锚点、证据类型、支持强度依据和未覆盖问题。
- 三入口规则对齐：Agent Skill、Claude Project、ChatGPT Project 共享类型、审计、材料范围和防编造边界。
- 新增 OpenAI UI 元数据，以及面向 ChatGPT Skills beta 的 Release skill 压缩包。
- 新增 18 个回归场景、3 份合成 fixture、无第三方依赖的规则 / 漂移检查和 GitHub Actions 门禁。

## 行为变化

### 先看材料，再选论文类型

`v0.1` 主要区分标准算法论文和观点 / 路线图论文。`v0.2.0` 把主模式与论文类型分开：主模式回答用户想怎么读，论文类型回答材料主要靠什么结构建立贡献和证据。

类型判断必须在确认实际可读材料之后进行。混合型论文选一个主类型，可说明次要类型；仍无法可靠判断时不反复追问，也不强行套标准方法 / 实验骨架，只输出材料实际支持的章节。

### 证据审计

用户提出“证据审计”“主张和证据”“哪些结论被实验支持”等要求时，可以在深读、工程拆解或调研比较之上叠加证据审计。

审计表的最小字段为：

```markdown
| 核心主张 | 原文锚点 | 证据类型 | 支持强度（含依据） | 未覆盖问题 |
|---|---|---|---|---|
```

无法定位时必须写“当前材料无法定位”；材料缺少证据时写“未见直接证据”或“无法判断”。缺少证据不是反证，也不自动证明主张错误。

## 兼容与安装

- Codex、Claude Code、Claude Project、ChatGPT Project 继续作为 Primary 维护入口。
- Custom GPT、Hermes、OpenClaw 保持 Compatible。
- ChatGPT Skills beta 新增为 Compatible, not first-regression-tested。GitHub Release 附带 `paper-reading-zh-v0.2.0.zip`；没有 Skills 上传入口时继续使用 `prompts/chatgpt-project.md`。
- skill 本体仍没有执行脚本、MCP、外部二进制或默认联网下载行为。仓库根目录的校验脚本只用于维护和发布。

## Validation

- `python3 scripts/check_rules.py`：8/8 PASS。
- `python3 -m json.tool evals/scenarios.json`：PASS，18 个场景、ID 唯一。
- AgentSkills 风格的 frontmatter、名称和描述校验：PASS。
- 三份合成 fixture 的隔离前向测试覆盖系统 / 测量、理论 / 证明的损坏公式边界和证据审计；完整记录见 `docs/validation-2026-07-10-v0.2.0.md`。
- 之前的真实 PDF 文本层验证仍适用于观点 / 路线图和高影响声明边界，见 `docs/validation-2026-05-27.md`。

## 已知限制

- 尚未完成 Claude Project、ChatGPT Project、Codex、Claude Code 四个平台的同一套真实论文端到端回归。
- ChatGPT Skills beta、Hermes 和 OpenClaw 尚未完成首轮实机回归。
- `evals/scenarios.json` 是声明式场景，不是自动对模型输出打分的完整评测框架。
- Web prompts 为保持自包含而比 Agent Skill 更长；后续修改必须运行漂移检查。

## Tag

`v0.2.0`

## Release title

`paper-reading-zh v0.2.0 - Type-aware reading and evidence audit`
