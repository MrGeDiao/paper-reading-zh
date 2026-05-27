# paper-reading-zh v0.1.1

`v0.1.1` 是开源准备版本，重点不是增加新模式，而是把公开维护面和真实验证证据补齐。

## Highlights

- 新增 `CHANGELOG.md`、`CONTRIBUTING.md`、`SECURITY.md`、Issue 模板和 PR 模板。
- 新增真实论文最小端到端验证记录：`docs/validation-2026-05-27.md`。
- README 增加从 GitHub clone 后安装 Agent Skill 的命令。
- DESIGN / README 更新验证状态：已经完成一次真实 PDF 文本层验证，但仍不宣称全平台完整回归。

## Validation

本版本用一篇未随仓库发布的 16 页 PDF 做了最小验证：`A Time Scaling Theory for Multi-Layer Electronic Systems`。验证重点包括材料范围说明、观点 / 路线图论文变体选择、实验 / 产业数字锚点、公式抽取乱码边界，以及 venue / CCF / 官方代码未核验时不补事实。

## Public Release Note

公开发布时建议使用干净公开仓或 orphan public branch，不直接把包含工作记录、草稿或本地验证材料的完整开发历史改成 public。

建议 tag：`v0.1.1`

建议发布标题：`paper-reading-zh v0.1.1 - Open-source readiness`
