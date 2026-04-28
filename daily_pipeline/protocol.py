from __future__ import annotations

from dataclasses import asdict
from datetime import date
from pathlib import Path

from daily_pipeline.abstraction.synthesizer import synthesize_abstract_team
from daily_pipeline.analysis.capabilities import find_shared_capabilities, normalize_teams
from daily_pipeline.analysis.references import find_shared_references
from daily_pipeline.config import PipelineConfig
from daily_pipeline.ingest.loader import load_teams
from daily_pipeline.integration.agentteams import build_integration_request, write_integration_request
from daily_pipeline.models import RunContext, StageResult
from daily_pipeline.reporting.writer import write_consolidated_report, write_stage_result


def _framework_matrix() -> dict[str, str]:
    # In initial implementation, these are assumed available.
    return {
        "claude": "available",
        "copilot-cli": "available",
        "copilot-vscode": "available",
    }


def _degraded_mode(matrix: dict[str, str]) -> bool:
    return any(status != "available" for status in matrix.values())


def run_protocol(
    team_paths: list[str],
    config: PipelineConfig,
    trigger: str,
    output_root: str,
    allow_degraded: bool,
) -> dict[str, str]:
    run_date = date.today().isoformat()
    run_dir = str(Path(output_root) / run_date)

    stage_results: list[StageResult] = []

    teams = load_teams(team_paths)
    s1 = StageResult("01-validate-selection", "ok", {"team_count": len(teams), "team_names": [t.name for t in teams]})
    write_stage_result(run_dir, s1)
    stage_results.append(s1)

    matrix = _framework_matrix()
    degraded = _degraded_mode(matrix)
    if degraded and not allow_degraded:
        s2 = StageResult("02-refresh-sources", "blocked", {"framework_matrix": matrix})
        write_stage_result(run_dir, s2)
        stage_results.append(s2)
        context = RunContext(run_date=run_date, run_dir=run_dir, degraded_mode=True, framework_matrix=matrix)
        report = write_consolidated_report(run_dir, context, stage_results)
        return {"run_dir": run_dir, "report": report}

    s2 = StageResult("02-refresh-sources", "ok", {"framework_matrix": matrix, "degraded_mode": degraded})
    write_stage_result(run_dir, s2)
    stage_results.append(s2)

    normalized = normalize_teams(teams)
    s3 = StageResult("03-ingest-normalize", "ok", {"normalized_teams": [n.name for n in normalized]})
    write_stage_result(run_dir, s3)
    stage_results.append(s3)

    shared_caps = find_shared_capabilities(normalized, config.capability_min_teams)
    shared_refs = find_shared_references(normalized, config.reference_min_teams)
    s4 = StageResult(
        "04-commonality-analysis",
        "ok",
        {
            "shared_capability_count": len(shared_caps),
            "shared_reference_count": len(shared_refs),
        },
    )
    write_stage_result(run_dir, s4)
    stage_results.append(s4)

    abstract_team = synthesize_abstract_team("abstract-agent-team", normalized, shared_caps, shared_refs)
    s5 = StageResult(
        "05-synthesize-abstract-team",
        "ok",
        {
            "abstract_team": abstract_team.name,
            "mapping_teams": sorted(list(abstract_team.mapping.keys())),
            "provenance_keys": sorted(list(abstract_team.provenance.keys())),
        },
    )
    write_stage_result(run_dir, s5)
    stage_results.append(s5)

    integration = build_integration_request(
        abstract_team=abstract_team,
        trigger=trigger,
        target_repo=config.agentteams_repo,
        confidence_floor=config.confidence_floor,
    )
    req_path = write_integration_request(integration, str(Path(run_dir) / "integration_requests"))
    s6 = StageResult("06-build-agentteams-integration", "ok", {"request_path": req_path})
    write_stage_result(run_dir, s6)
    stage_results.append(s6)

    protocol_registry = {
        "stages": [asdict(x) for x in stage_results],
        "degraded_mode": degraded,
    }
    s7 = StageResult("07-stage-registry", "ok", protocol_registry)
    write_stage_result(run_dir, s7)
    stage_results.append(s7)

    context = RunContext(run_date=run_date, run_dir=run_dir, degraded_mode=degraded, framework_matrix=matrix)
    report = write_consolidated_report(run_dir, context, stage_results)
    s8 = StageResult("08-consolidated-report", "ok", {"report": report})
    write_stage_result(run_dir, s8)
    stage_results.append(s8)

    return {"run_dir": run_dir, "report": report}
