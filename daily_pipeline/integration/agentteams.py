from __future__ import annotations

import json
from pathlib import Path

from daily_pipeline.models import AbstractTeamOutput, IntegrationRequest


def build_integration_request(
    abstract_team: AbstractTeamOutput,
    trigger: str,
    target_repo: str,
    confidence_floor: float,
) -> IntegrationRequest:
    payload = {
        "action": "agentteams-update-request",
        "trigger": trigger,
        "abstract_team": abstract_team.name,
        "shared_capabilities": [
            {
                "key": cap.key,
                "teams": cap.teams,
                "confidence": cap.confidence,
            }
            for cap in abstract_team.shared_capabilities
            if cap.confidence >= confidence_floor
        ],
        "shared_references": [
            {
                "key": ref.key,
                "teams": ref.teams,
                "freshness": ref.freshness_tag,
                "confidence": ref.confidence,
            }
            for ref in abstract_team.shared_references
            if ref.confidence >= confidence_floor
        ],
        "provenance": abstract_team.provenance,
        "mapping": abstract_team.mapping,
        "constraints": {
            "reference_only_external_scripts": True,
            "no_private_imports": True,
        },
    }
    return IntegrationRequest(
        trigger=trigger,
        target_repo=target_repo,
        frameworks=["claude", "copilot-cli", "copilot-vscode"],
        abstract_team_name=abstract_team.name,
        capability_confidence_floor=confidence_floor,
        reference_confidence_floor=confidence_floor,
        payload=payload,
    )


def write_integration_request(request: IntegrationRequest, out_dir: str) -> str:
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path(out_dir) / f"agentteams-request-{request.trigger}.json"
    file_path.write_text(json.dumps(request.payload, indent=2))
    return str(file_path)
