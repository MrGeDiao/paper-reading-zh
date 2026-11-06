# 网页端使用

不用 CLI 的话，用 [`project-instructions.md`](./project-instructions.md) 这一份就够了，Claude Project 和 ChatGPT Project 通用。

## Claude Project / ChatGPT Project

1. 新建 Project。
2. 把 `project-instructions.md` 的全文粘贴到 Project instructions。
3. 上传论文 PDF，或者粘贴链接、标题、摘要，然后提问，例如 `精读这篇论文`、`从工程复现角度拆一下`、`比较这几篇论文`。

这份 instructions 不到 8000 字符，模式模板和论文类型骨架都已写在文件里，不需要另外上传 reference 文件。

## 和 Agent Skill 的区别

网页版和 `paper-reading-zh/` 里的 Agent Skill 用的是同一套证据规则，有三处差异：

- 网页版不能调用本地工具。能不能联网核验 venue 和代码链接，能不能看到 PDF 里的图表，取决于所用平台；做不到时，规则要求先说明限制。
- 网页版没有“直接写代码”的分流，也没有触发前的预检，因为网页端没有编码流程和预检工具。
- 网页版是精简改写：约束都保留，部分细则省略。逐项取舍见 [DESIGN.md](../DESIGN.md#web-版裁剪项)。

想用完整规则，可以把 `paper-reading-zh/SKILL.md`、`references/modes.md`、`references/paper-types.md` 三个文件上传到 Project files，再在 instructions 里写一句：`按项目文件 SKILL.md 的规则读论文，需要模板时查 modes.md 和 paper-types.md。` 这种用法还没在网页端实测过。

## 修改这份 prompt

改规则时，Agent Skill 和这份 prompt 要一起改，然后运行 `python3 scripts/check_rules.py`。脚本会检查两边的关键规则是否一致，以及 prompt 是否超过 8000 字符。
