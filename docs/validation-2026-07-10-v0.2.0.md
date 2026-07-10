# Validation 2026-07-10 — v0.2.0

本记录验证 `v0.2.0` 新增的论文类型自适应、证据审计、三入口对齐和维护校验。它不等同于四个平台的完整真实论文回归。

## Static and structural checks

执行：

```text
python3 scripts/check_rules.py
python3 -m json.tool evals/scenarios.json
git diff --check
```

结果：

- 必要文件、SKILL frontmatter、两个直接 reference、OpenAI UI 元数据：PASS。
- `evals/scenarios.json`：18 个结构一致、ID 唯一的场景，PASS。
- Agent Skill、Claude Project、ChatGPT Project 的论文类型、证据审计、材料退出、产业声明、比较口径和代码边界：PASS。
- 两份 Web prompt 自包含，不依赖运行时读取 `references/`：PASS。
- 负向突变检查：在隔离副本中把 ChatGPT prompt 的“证据审计”标题改名后，校验器按预期失败，确认漂移门禁不是恒真检查。

静态评估只验证结构、预算和关键规则存在，不证明模型在所有材料上都会正确执行。

## Forward-test materials

测试使用三份仓库内合成材料，避免版权和隐私问题：

- `evals/fixtures/system-measurement.md`
- `evals/fixtures/theory-damaged-extraction.md`
- `evals/fixtures/evidence-audit.md`

每个测试在隔离目录中放入当前 `paper-reading-zh/` skill 和一份 fixture；测试 agent 只看到 skill、材料和用户任务，不看到 `evals/scenarios.json` 中的期望行为。

Codex CLI 的首轮隔离测试因账户用量上限未产生输出。随后使用 Claude Code `sonnet`、`high` effort 重跑；JSON provenance 显示实际模型为 `claude-sonnet-5`。

## Results

### System / measurement

任务：解释生产系统测量设计、数字实际支持什么、结论是否可推广。

结果：PASS。

- 正确识别系统 / 测量类型，没有硬套模型训练骨架。
- 把 120 ms 到 82 ms、10.6 PB 到 9.6 PB 锚定到材料中的 Table 2 / Table 3。
- 区分“部署前后观察到下降”和“下降由 EdgeCache 导致”；指出无随机分组、无同期对照、第 6 周工作负载变化未剥离。
- 没有把单厂商、单地区、8 周结果推广到其他环境。

### Evidence audit

任务：审计 MiniBench 的三个核心主张。

结果：PASS。

- 输出核心主张、原文锚点、证据类型、支持强度依据和未覆盖问题。
- 对“测量稳健推理”写“无法判断”，对部署质量相关性写“弱到中等”，对 Model A 更可靠写“弱”，并解释样本量、统计检验和构念定义缺口。
- 明确说明弱证据或缺证据不代表主张错误。

### Theory / damaged extraction

任务：解释假设、定理、证明策略和损坏公式边界。

结果：行为输出 PASS；调用完成状态不完整。

- 输出文件完整生成，正确按理论 / 证明类型组织。
- 区分 A1、A2、Theorem 1、Lemma 1 / Lemma 2 和 telescoping 证明轮廓。
- 明确拒绝恢复缺失的指数、分母和精确迭代复杂度，没有基于常见文献补公式。
- 模型调用在写完输出后返回外部会话额度错误，因此不把该次调用记为完整正常结束。

## Existing real-paper evidence

`docs/validation-2026-05-27.md` 使用一篇真实 16 页 PDF，已经覆盖观点 / 路线图变体、数字锚点、损坏公式边界和高影响产业声明标签。`v0.2.0` 保留并迁移了这些行为。

## Remaining risk

- 尚未用同一篇真实论文在 Claude Project、ChatGPT Project、Codex、Claude Code 四个平台逐一执行。
- 系统 / 测量、理论 / 证明和证据审计的新测试材料是合成 fixture，不代表真实论文分布的全部复杂度。
- ChatGPT Skills beta、Hermes 和 OpenClaw 只做格式兼容判断，尚未实机验证安装与触发。
- 声明式场景尚未接入自动模型评分器；当前发布门禁是结构检查、人工 review 和隔离前向测试的组合。
