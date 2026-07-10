#!/usr/bin/env python3
"""Validate the rule package without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "paper-reading-zh/SKILL.md",
    "paper-reading-zh/references/modes.md",
    "paper-reading-zh/references/paper-types.md",
    "paper-reading-zh/agents/openai.yaml",
    "prompts/claude-project.md",
    "prompts/chatgpt-project.md",
    "evals/scenarios.json",
    "evals/fixtures/system-measurement.md",
    "evals/fixtures/theory-damaged-extraction.md",
    "evals/fixtures/evidence-audit.md",
    "scripts/check_rules.py",
    ".github/workflows/validate.yml",
]

ENTRY_FILES = {
    "Agent Skill": ROOT / "paper-reading-zh/SKILL.md",
    "Claude Project": ROOT / "prompts/claude-project.md",
    "ChatGPT Project": ROOT / "prompts/chatgpt-project.md",
}

SCENARIO_FIELDS = {
    "id",
    "category",
    "user_input",
    "material_context",
    "expected_behavior",
    "must_include",
    "must_not_include",
}


failures: list[str] = []
check_count = 0


def report(name: str, passed: bool, detail: str = "") -> None:
    global check_count
    check_count += 1
    status = "PASS" if passed else "FAIL"
    suffix = f" - {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")
    if not passed:
        failures.append(f"{name}{suffix}")


def run_check(name: str, check: Callable[[], tuple[bool, str]]) -> None:
    try:
        passed, detail = check()
    except Exception as exc:  # noqa: BLE001 - validation must report all failures
        report(name, False, f"{type(exc).__name__}: {exc}")
        return
    report(name, passed, detail)


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with a YAML frontmatter delimiter")
    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError("SKILL.md is missing the closing frontmatter delimiter")

    raw_header = text[4:closing]
    metadata: dict[str, str] = {}
    for line_number, line in enumerate(raw_header.splitlines(), start=2):
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            raise ValueError(f"unsupported frontmatter line {line_number}: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            raise ValueError(f"empty frontmatter key/value on line {line_number}")
        if key in metadata:
            raise ValueError(f"duplicate frontmatter key: {key}")
        metadata[key] = value

    return metadata, text[closing + 5 :]


def check_required_files() -> tuple[bool, str]:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        return False, f"missing: {', '.join(missing)}"
    workflow = read_text(".github/workflows/validate.yml")
    required_commands = [
        "python3 -m py_compile scripts/check_rules.py",
        "python3 scripts/check_rules.py",
        "python3 -m json.tool evals/scenarios.json",
    ]
    missing_commands = [command for command in required_commands if command not in workflow]
    if missing_commands:
        return False, f"validation workflow missing: {', '.join(missing_commands)}"
    return True, f"{len(REQUIRED_FILES)} files present"


def check_frontmatter() -> tuple[bool, str]:
    metadata, body = parse_frontmatter(read_text("paper-reading-zh/SKILL.md"))
    if set(metadata) != {"name", "description"}:
        return False, "frontmatter must contain exactly name and description"
    if metadata.get("name") != "paper-reading-zh":
        return False, "name must be paper-reading-zh"

    description = metadata.get("description", "")
    if not description:
        return False, "description is missing"
    if len(description) > 220:
        return False, f"description is not compressed enough ({len(description)} chars)"

    required_terms = [
        "论文精读",
        "工程拆解",
        "多论文比较",
        "按图表",
        "证据审计",
        "PDF",
        "链接",
        "标题",
        "纯翻译",
        "单术语定义",
        "BibTeX",
        "只找或下载论文",
        "Use when",
    ]
    missing_terms = [term for term in required_terms if term not in description]
    if missing_terms:
        return False, f"description missing: {', '.join(missing_terms)}"
    if not body.lstrip().startswith("# Paper Reading Zh"):
        return False, "body heading is missing"
    return True, f"name and {len(description)}-character description are valid"


def check_direct_references() -> tuple[bool, str]:
    skill = read_text("paper-reading-zh/SKILL.md")
    required = ["references/modes.md", "references/paper-types.md"]
    missing = [reference for reference in required if reference not in skill]
    if missing:
        return False, f"SKILL.md missing direct reference(s): {', '.join(missing)}"
    missing_toc = [
        reference
        for reference in required
        if "## 目录" not in read_text(f"paper-reading-zh/{reference}")
    ]
    if missing_toc:
        return False, f"long reference missing table of contents: {', '.join(missing_toc)}"
    return True, "both references are linked directly and include navigation"


def parse_openai_yaml() -> dict[str, str]:
    lines = [
        line
        for line in read_text("paper-reading-zh/agents/openai.yaml").splitlines()
        if line.strip()
    ]
    if not lines or lines[0] != "interface:":
        raise ValueError("top-level interface mapping is required")
    if len(lines) != 4:
        raise ValueError("openai.yaml must contain only interface and its three fields")

    values: dict[str, str] = {}
    pattern = re.compile(r'  ([a-z_]+): "([^"]*)"')
    for line in lines[1:]:
        match = pattern.fullmatch(line)
        if not match:
            raise ValueError(f"field must be indented and double-quoted: {line!r}")
        key, value = match.groups()
        if key in values:
            raise ValueError(f"duplicate interface field: {key}")
        values[key] = value
    return values


def check_openai_yaml() -> tuple[bool, str]:
    values = parse_openai_yaml()
    expected_keys = {"display_name", "short_description", "default_prompt"}
    if set(values) != expected_keys:
        return False, f"fields must be exactly: {', '.join(sorted(expected_keys))}"
    if not values["display_name"].strip():
        return False, "display_name must not be empty"

    short_description = values["short_description"]
    if not 25 <= len(short_description) <= 64:
        return False, (
            "short_description must be 25-64 characters "
            f"(found {len(short_description)})"
        )

    default_prompt = values["default_prompt"]
    if "$paper-reading-zh" not in default_prompt:
        return False, "default_prompt must mention $paper-reading-zh"
    sentence_endings = sum(default_prompt.count(mark) for mark in "。！？.!?")
    if sentence_endings != 1 or default_prompt[-1] not in "。！？.!?":
        return False, "default_prompt must be one sentence"
    return True, "interface fields, quoting, length, and default prompt are valid"


def load_scenarios() -> list[dict[str, object]]:
    data = json.loads(read_text("evals/scenarios.json"))
    if not isinstance(data, list):
        raise ValueError("top-level JSON value must be an array")
    return data


def check_scenarios() -> tuple[bool, str]:
    scenarios = load_scenarios()
    if not 12 <= len(scenarios) <= 20:
        return False, f"scenario count must be 12-20 (found {len(scenarios)})"

    ids: list[str] = []
    for index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            return False, f"scenario {index} is not an object"
        if set(scenario) != SCENARIO_FIELDS:
            missing = sorted(SCENARIO_FIELDS - set(scenario))
            extra = sorted(set(scenario) - SCENARIO_FIELDS)
            return False, (
                f"scenario {index} field mismatch; missing={missing}, extra={extra}"
            )

        for field in [
            "id",
            "category",
            "user_input",
            "material_context",
            "expected_behavior",
        ]:
            value = scenario[field]
            if not isinstance(value, str) or not value.strip():
                return False, f"scenario {index} has invalid {field}"

        for field in ["must_include", "must_not_include"]:
            value = scenario[field]
            if (
                not isinstance(value, list)
                or not value
                or any(not isinstance(item, str) or not item.strip() for item in value)
            ):
                return False, f"scenario {index} has invalid {field}"

        ids.append(scenario["id"])

    duplicates = sorted({scenario_id for scenario_id in ids if ids.count(scenario_id) > 1})
    if duplicates:
        return False, f"duplicate ids: {', '.join(duplicates)}"
    return True, f"{len(scenarios)} consistent scenarios with unique ids"


def check_paper_types_reference() -> tuple[bool, str]:
    text = read_text("paper-reading-zh/references/paper-types.md")
    required_sections = [
        "## 标准方法 / 实验论文",
        "## 系统 / 测量论文",
        "## 数据集 / benchmark 论文",
        "## 理论 / 证明论文",
        "## 综述 / 立场论文",
        "## 观点 / 路线图变体",
        "### 识别原则",
        "### 适用边界",
        "### 建议主体骨架",
    ]
    missing = [section for section in required_sections if section not in text]
    if missing:
        return False, f"paper-types.md missing: {', '.join(missing)}"
    return True, "type identification, boundaries, and skeletons are present"


def check_shared_entry_rules() -> tuple[bool, str]:
    required_groups = {
        "paper types": [
            "标准方法 / 实验",
            "系统 / 测量",
            "数据集 / benchmark",
            "理论 / 证明",
            "综述 / 立场",
            "观点 / 路线图",
        ],
        "type uncertainty boundary": ["类型不确定", "不强行套"],
        "evidence audit fields": [
            "证据审计",
            "核心主张",
            "原文锚点",
            "证据类型",
            "支持强度",
            "未覆盖问题",
        ],
        "missing evidence boundary": ["缺少证据", "反证"],
        "high-impact labels": [
            "论文内部声明",
            "作者预测",
            "已公开第三方核验",
            "未核验",
        ],
        "material exit and extraction boundary": [
            "可信材料",
            "退出深读",
            "乱码",
            "不基于乱码重构",
        ],
        "comparison boundary": ["口径不完全可比", "口径未核验"],
        "code boundary": ["用户提供", "公式-代码对齐", "非官方实现"],
        "math and terminology self-check": [
            "公式与多符号表达式",
            "术语是否首次中英对照",
        ],
    }

    missing_by_entry: list[str] = []
    for entry_name, path in ENTRY_FILES.items():
        text = path.read_text(encoding="utf-8")
        for group_name, terms in required_groups.items():
            missing = [term for term in terms if term not in text]
            if missing:
                missing_by_entry.append(
                    f"{entry_name}/{group_name}: {', '.join(missing)}"
                )

    if missing_by_entry:
        return False, "; ".join(missing_by_entry)
    return True, "shared type, audit, evidence, material, comparison, and code rules exist"


def check_web_prompts_are_self_contained() -> tuple[bool, str]:
    required_headings = [
        "### 系统 / 测量",
        "### 数据集 / benchmark",
        "### 理论 / 证明",
        "### 综述 / 立场",
        "### 观点 / 路线图",
        "### 证据审计",
    ]
    problems: list[str] = []
    for relative_path in ["prompts/claude-project.md", "prompts/chatgpt-project.md"]:
        text = read_text(relative_path)
        if "references/" in text:
            problems.append(f"{relative_path} depends on references/")
        missing = [heading for heading in required_headings if heading not in text]
        if missing:
            problems.append(f"{relative_path} missing {', '.join(missing)}")
        if "| 核心主张 | 原文锚点 | 证据类型 | 支持强度（含依据） | 未覆盖问题 |" not in text:
            problems.append(f"{relative_path} missing evidence audit skeleton")

    if problems:
        return False, "; ".join(problems)
    return True, "both Web prompts inline type and evidence-audit rules"


def main() -> int:
    run_check("necessary files", check_required_files)
    run_check("SKILL frontmatter", check_frontmatter)
    run_check("SKILL direct references", check_direct_references)
    run_check("OpenAI UI metadata", check_openai_yaml)
    run_check("scenario JSON", check_scenarios)
    run_check("paper type reference", check_paper_types_reference)
    run_check("three-entry shared behavior", check_shared_entry_rules)
    run_check("Web prompt self-containment", check_web_prompts_are_self_contained)

    if failures:
        print(f"\nFAIL: {len(failures)} of {check_count} checks failed.")
        return 1
    print(f"\nPASS: all {check_count} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
