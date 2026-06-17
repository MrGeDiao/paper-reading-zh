# paper-reading-zh v0.1.3

`v0.1.3` 是文档规划和维护溯源版本。它记录本仓如何使用本地多 agent 协作方式辅助文档更新，但不改变 `paper-reading-zh` 的论文阅读规则、触发边界或安装方式。

## 背景

`DESIGN.md` 是本项目规划、兼容矩阵和证据规则的单一事实源。v0.1 设计约束明确不把 `paper-reading-zh` 做成多 agent 调度器，也不引入固定文献流水线、traceability manifest 或 claim id。

本次更新需要说明维护者可以在文档设计、审稿和风险扫描中使用协作工作流，同时避免让读者误解为 skill 本身新增了多 agent 论文精读能力。

## 变更

1. **版本标识**：README badge 和项目状态更新到 `v0.1.3`。
2. **维护溯源**：`DESIGN.md` 新增 Maintenance Provenance，记录本次使用 `tri-collab` 式本地维护工作流作为协作方式。
3. **公开发布面**：`DESIGN.md` 的 Public Surface 列表增加 `docs/release-v0.1.3.md`。
4. **验证状态**：说明 `v0.1.3` 只更新公开文档、版本记录和维护溯源，不需要新的端到端论文阅读回归。

未改动：

- `paper-reading-zh/SKILL.md`。
- `paper-reading-zh/references/modes.md`。
- `prompts/claude-project.md` 和 `prompts/chatgpt-project.md`。
- 阅读模式、证据规则、兼容矩阵、安装方式和输出契约。

## 决策依据

- 本仓版本策略允许公开文档的兼容增强走 patch。
- `tri-collab` 是维护者本地使用的协作流程引用；公开文档只记录流程名称，不记录维护者本机绝对路径。
- 把维护过程和用户侧运行时行为分开，可以保留 v0.1 的简洁边界：论文精读规则仍只关注材料范围、证据边界和输出结构。

## 已知限制

- 本版本只记录维护协作方式，不公开维护者本机 skill 路径，也不作为公共用户入口。
- 本版本没有新增论文样例验证，也没有完成 Claude Project、ChatGPT Project、Codex、Claude Code 四个平台的完整端到端回归测试。
- 本版本不代表 `paper-reading-zh` 会自动调用 Claude Code、Antigravity 或其他 agent 参与论文阅读。

## 建议 tag

`v0.1.3`

## 建议发布标题

`paper-reading-zh v0.1.3 - Documentation provenance update`
