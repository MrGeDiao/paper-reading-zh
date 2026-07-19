# paper-reading-zh v0.2.1

`v0.2.1` 是一次兼容增强，主题是 Web prompt 的防编造规则对齐。它以 `v0.2.0` 的论文类型自适应和证据审计为当前基线，不回退或重复实现已经发布的规则。

## 背景

Web Prompt Kit 与 Agent Skill 共享阅读规则，但 Web prompt 必须自包含，长期维护时容易出现某条防编造约束只落在一个入口的问题。`v0.2.0` 已经补入观点 / 路线图论文骨架、高影响产业声明四级标签、PDF 抽取乱码处置和对应自检；本版本逐条重新审计当前三入口，只回填仍缺失或不完整的部分。

## 变更

### 三入口同步机制

- `DESIGN.md` 新增 Rule Sync Matrix，记录每个规则簇在 Agent Skill、Claude Project 和 ChatGPT Project 中是完整、精简还是有理由的裁剪。
- `CONTRIBUTING.md` 与 PR 模板要求修改规则时核对矩阵受影响行。
- “只有论文锚点时不要先做预检”保留为 Agent 专属规则；Web 无预检工具链，因此在矩阵中明确裁剪。

### Web 防编造边界

- 标题或链接无法获得可信材料时，两份 Web prompt 都要求退出深读，不基于常识或训练记忆补论文内容。
- ChatGPT 链接不可读时要求用户上传 PDF 或粘贴正文 / 摘要；整篇论文不可读不能仅靠“未核验”标签继续深读，只有个别元数据字段缺失时才使用该标签。
- 后续追问默认继承上一轮论文上下文、术语表、模式、论文类型和子开关。

### 其余规则对齐

- Web prompt 补充默认优先服务 CS / AI / ML、非 CS 不强制 CCF 或工程复现建议的适用边界。
- Web prompt 补充核心符号首次中文解释、纯叙述段减少 LaTeX 符号堆叠，以及最多 5 个主线必需词条的短术语表。
- 调研比较模式补充紧凑比较表默认列和表后文字解释要求。
- 输出前自检补充“避免默认全文翻译”和“根据论文性质和用户目标调整章节权重”。

## 决策依据

- 当前 `SKILL.md` 与 `references/modes.md` 是 Agent 入口的规则基线；旧路线图引文与当前文案不同时，以当前基线为准。
- `v0.2.0` 已内联比旧路线图要求更完整的观点 / 路线图类型规则，因此本版本不再追加旧版极简段落。
- 当前 Agent 的多轮继承规则包含“论文类型和子开关”，Web prompt 按该完整现行句子同步，而不是使用旧路线图中较短的版本。
- 高影响产业声明在 Web prompt 中保留四级标签和自检，但将 Agent 的“高影响且难外部复验的内容”精简为“高影响声明”；Rule Sync Matrix 如实记录为精简。

## Validation

- `python3 scripts/check_rules.py`：8/8 PASS。
- `python3 -m json.tool evals/scenarios.json`：PASS，18 个场景、ID 唯一。
- `docs/validation-2026-07-19.md` 覆盖标题-only、观点 / 路线图论文和 ChatGPT 链接不可读三个 Web 场景，但均为基于规则文本的预期行为并明确标记“未实测”。

## 已知限制

- 尚未在真实 Claude Project 和 ChatGPT Project 会话中执行本版本的三个 Web 场景；真实平台实测是仓库所有者的待办项。
- 尚未完成 Claude Project、ChatGPT Project、Codex、Claude Code 四个平台的同一套真实论文端到端回归。
- ChatGPT Skills beta、Hermes 和 OpenClaw 仍为 Compatible, not first-regression-tested。
- Web prompt 的联网和 PDF 图表读取能力仍取决于具体平台与模型。

## 建议 tag

`v0.2.1`

## 建议发布标题

`paper-reading-zh v0.2.1 - Web prompt anti-fabrication parity`
