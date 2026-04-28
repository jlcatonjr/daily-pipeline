from __future__ import annotations

import json
from pathlib import Path

from daily_pipeline.models import RunContext, StageResult


def write_stage_result(run_dir: str, result: StageResult) -> str:
    out = Path(run_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{result.stage}.json"
    path.write_text(json.dumps({"stage": result.stage, "status": result.status, "details": result.details}, indent=2))
    return str(path)


def write_consolidated_report(run_dir: str, context: RunContext, stages: list[StageResult]) -> str:
    report_path = Path(run_dir).parent / f"daily-pipeline-{context.run_date}.report.md"
    lines = [
        f"# Daily Pipeline Report ({context.run_date})",
        "",
        f"- Degraded mode: {context.degraded_mode}",
        "- Framework availability:",
    ]
    for framework, status in sorted(context.framework_matrix.items()):
        lines.append(f"  - {framework}: {status}")

    lines.append("")
    lines.append("## Stage Status")
    for stage in stages:
        lines.append(f"- {stage.stage}: {stage.status}")

    report_path.write_text("\n".join(lines) + "\n")
    return str(report_path)
