from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PipelineConfig:
    capability_min_teams: int
    reference_min_teams: int
    confidence_floor: float
    agentteams_repo: str
    build_team_py: str | None  # path to build_team.py executable; None = unset; Stage 9.5 use only


def load_config(config_path: str | None) -> PipelineConfig:
    if config_path is None:
        default_path = Path(__file__).resolve().parents[1] / "configs" / "defaults.json"
        content = json.loads(default_path.read_text())
    else:
        content = json.loads(Path(config_path).read_text())

    return PipelineConfig(
        capability_min_teams=int(content.get("capability_min_teams", 2)),
        reference_min_teams=int(content.get("reference_min_teams", 2)),
        confidence_floor=float(content.get("confidence_floor", 0.6)),
        agentteams_repo=str(content.get("agentteams_repo", "/Users/jamescaton/githubrepositories/agentteams")),
        build_team_py=content.get("build_team_py") or None,
    )
