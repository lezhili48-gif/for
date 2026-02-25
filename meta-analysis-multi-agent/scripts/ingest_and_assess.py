#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs" / "input_assessment_report_zh.md"
PROGRESS = ROOT / "docs" / "pipeline_progress_zh.md"
SUMMARY = ROOT / "logs" / "input_assessment_summary.json"

TARGETS = {
    "protocol_pdf": "PRISMA_Protocol_Biochar_DNRA_Denitrification.pdf",
    "protocol_md": "PRISMA_Protocol_Biochar_DNRA_Denitrification.md",
    "extraction_xlsx": "Data_Extraction_Template.xlsx",
    "analysis_r": "Meta_Analysis_R_Code.R",
}

SEARCH_ROOTS = [ROOT / "inputs", ROOT]
SKIP = {".git", "__pycache__", "node_modules", ".venv", "venv"}


def find_file(name: str) -> Path | None:
    for base in SEARCH_ROOTS:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if not p.is_file():
                continue
            if any(part in SKIP for part in p.parts):
                continue
            if p.name == name:
                return p
    return None


def main() -> None:
    located = {k: find_file(v) for k, v in TARGETS.items()}

    method_ready = bool(located["protocol_pdf"] or located["protocol_md"])
    data_ready = bool(located["extraction_xlsx"])
    analysis_ready = bool(located["analysis_r"])
    all_ready = method_ready and data_ready and analysis_ready

    lines = [
        "# 输入文件评估报告（自动生成）",
        "",
        "## 文件定位结果",
        "",
    ]
    for key in ["protocol_pdf", "protocol_md", "extraction_xlsx", "analysis_r"]:
        name = TARGETS[key]
        path = located[key]
        if path:
            lines.append(f"- {name}: ✅ 已找到（`{path.relative_to(ROOT)}`）")
        else:
            lines.append(f"- {name}: ❌ 未找到")

    lines += ["", "## 下一步", ""]
    if all_ready:
        lines += [
            "1. 基于 protocol 冻结 `templates/protocol.md` 与 `templates/eligibility_criteria.yaml`。",
            "2. 从 xlsx 导出 `data/processed/extraction_sheet.csv` 并完成列名映射。",
            "3. 运行 R 脚本并输出图表与结果表。",
            "4. 启动 manuscript 的 Methods + Results 草稿。",
        ]
    else:
        lines += [
            "1. 请将三份输入文件放到 `meta-analysis-multi-agent/inputs/`（推荐）或仓库任意子目录。",
            "2. 运行 `python meta-analysis-multi-agent/scripts/ingest_and_assess.py` 复查。",
            "3. 三类输入（protocol / xlsx / R）全部识别后，再进入统计和写作。",
        ]

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    progress = [
        "# 流程推进说明（自动更新）",
        "",
        "## 阶段就绪度",
        "",
        f"- 方法学输入（Protocol）: {'✅' if method_ready else '❌'}",
        f"- 数据结构输入（Extraction xlsx）: {'✅' if data_ready else '❌'}",
        f"- 统计执行输入（R script）: {'✅' if analysis_ready else '❌'}",
        f"- 写作启动条件（3项齐备）: {'✅' if all_ready else '❌'}",
        "",
        "## 下一步执行清单",
        "",
        "1. 固定输入路径和命名，避免后续脚本失配。",
        "2. 先冻结方法学，再导出可计算数据。",
        "3. 小样本 dry-run 验证 R 脚本输出路径和核心图表。",
        "4. 先写 Methods + Results，再写 Discussion + Abstract。",
    ]
    PROGRESS.write_text("\n".join(progress) + "\n", encoding="utf-8")

    summary = {
        "located": {k: (str(v.relative_to(ROOT)) if v else None) for k, v in located.items()},
        "readiness": {
            "method_ready": method_ready,
            "data_ready": data_ready,
            "analysis_ready": analysis_ready,
            "all_ready": all_ready,
        },
    }
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Report generated: {REPORT}")
    print(f"Progress generated: {PROGRESS}")
    print(f"Summary generated: {SUMMARY}")


if __name__ == "__main__":
    main()
