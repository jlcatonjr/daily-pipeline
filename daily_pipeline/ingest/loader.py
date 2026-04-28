from __future__ import annotations

import json
from pathlib import Path

from daily_pipeline.models import AgentRecord, TeamRecord


def load_team_file(path: str) -> TeamRecord:
    raw = json.loads(Path(path).read_text())
    agents = []
    for item in raw.get("agents", []):
        agents.append(
            AgentRecord(
                name=str(item.get("name", "unknown-agent")),
                capabilities=[str(x) for x in item.get("capabilities", [])],
                references=[str(x) for x in item.get("references", [])],
            )
        )

    return TeamRecord(
        name=str(raw.get("name", Path(path).stem)),
        framework=str(raw.get("framework", "mixed")),
        source=str(raw.get("source", path)),
        agents=agents,
        metadata=dict(raw.get("metadata", {})),
    )


def load_teams(paths: list[str]) -> list[TeamRecord]:
    return [load_team_file(p) for p in paths]
