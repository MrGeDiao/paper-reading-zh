# Validation 2026-05-27

本记录用于验证 `paper-reading-zh` 的证据边界和真实 PDF 处理能力。它不是论文精读正文，也不把被测 PDF 作为本仓库发布资产。

## Material

- Local test file: `202605.00224v1.pdf` (local copy used for validation; not committed to this repository)
- Pages: 16
- Title from PDF text: `A Time Scaling Theory for Multi-Layer Electronic Systems`
- Author / affiliation from PDF text: Tingbo He / Huawei
- Version marker visible in extracted text: `This version posted 2026-05-25.`
- External venue / CCF / official code: 未核验；本次验证没有把任何外部页面或代码仓库写成已确认事实。

## Extraction Scope

PDF 文本层可读，足以抽取标题、摘要、章节文字、部分 sidebar、Table 1 caption 和若干数值声明。

PDF 公式抽取存在明显乱码和错位，尤其是第 4-5 页的 `tau` 分解公式和缩放公式。因此验证输出应说明：可以解释上下文中的概念，但不能基于抽取乱码重构公式细节。

## Expected Mode

这篇材料是 perspective / roadmap / 产业方法论论文，不是标准算法实验论文。`paper-reading-zh` 应使用深读模式下的“观点 / 路线图论文变体”，主体重点应放在：

- 核心主张链条
- 证据类型与证据强度
- 关键产业 / 工程假设
- 可核验、未核验与作者预测
- 风险边界与适合追问的问题

不应硬套“方法 / 实验 / 结果”的算法论文结构。

## Evidence Anchors Checked

以下均为 PDF 内部声明；除 PDF 本身外，本次没有完成第三方外部核验。

| Anchor | PDF location | Boundary label |
|---|---|---|
| LogicFolding delivers a 55% density increase and 41% power-efficiency gain at a fixed node. | Abstract / page 1 | 论文内部声明 |
| The roadmap draws on lessons from 381 chips brought to volume production between May 2020 and May 2026. | Page 2 | 论文内部声明 |
| Transistor density rose from 155 to 238 MTr/mm2 in one generation. | Page 6; Sidebar A on page 8 | 论文内部声明 |
| SoC P-core power efficiency improved by 41%, and clock frequency rose by nearly 13%. | Pages 6-7; Sidebar A on page 8 | 论文内部声明 |
| Table 1 lists Kirin CPU performance-core frequency trend: 2026 3.1 GHz silicon, 2027 3.39 GHz silicon, 2028 3.71 GHz pre-silicon, 2029 4 GHz pre-silicon. | Table 1 / pages 7-8 | 论文内部声明；2028-2029 为 pre-silicon |
| Unified Bus remote-access latency is described as falling from tens of microseconds to about 100 ns, around 500x tau reduction. | Page 9; Sidebar B on page 11 | 论文内部声明 |
| 2026 to 2035 projected hardware-integration growth is greater than 100x. | Abstract / page 1; Sidebar B / page 11; conclusion / page 14 | 作者预测 / 论文内部声明 |
| Current Linpack, MLPerf, and SPEC benchmarks are described as insufficient for tau-profile benchmarking. | Page 14 | 论文内部观点 |

## Minimal Output Behavior

一个合格的 `paper-reading-zh` 输出应体现：

1. 先说明材料范围：本地 PDF 文本层可读，公式抽取有乱码，外部 venue / CCF / 代码未核验。
2. 论文基本信息中不补不存在或未核验的 venue、CCF、代码链接。
3. 数字声明要带位置或语义锚点，例如 “page 6 / Sidebar A” 或 “Table 1”。
4. 对 `>100x by 2035`、`381 chips`、Kirin roadmap 等高影响产业声明标注为“论文内部声明”或“作者预测”，不写成独立证实的事实。
5. 对第 4-5 页公式乱码，写“PDF 抽取异常，不能重构公式”，而不是自己补公式。

## Result

本次验证通过最小证据边界检查：

- 能识别非标准算法论文，并选择观点 / 路线图论文变体。
- 能从 PDF 文本层抽取可定位的数字声明。
- 能识别公式抽取异常并设置“不重构”的边界。
- 能避免把 venue、CCF、官方代码、第三方核验状态写成已确认事实。

剩余风险：本次只验证了本地 PDF 文本层，不等同于 Claude Project、ChatGPT Project、Codex、Claude Code 四个平台的完整端到端回归。
