from __future__ import annotations

from collections import defaultdict
import re

from daily_pipeline.models import NormalizedTeam, SharedCapability, TeamRecord


def _normalize_label(label: str) -> str:
    value = label.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "unknown"


def normalize_teams(teams: list[TeamRecord]) -> list[NormalizedTeam]:
    output = []
    for team in teams:
        cap_map: dict[str, set[str]] = defaultdict(set)
        ref_map: dict[str, set[str]] = defaultdict(set)
        for agent in team.agents:
            for cap in agent.capabilities:
                cap_map[_normalize_label(cap)].add(agent.name)
            for ref in agent.references:
                ref_map[_normalize_label(ref)].add(agent.name)
        output.append(
            NormalizedTeam(
                name=team.name,
                framework=team.framework,
                source=team.source,
                capabilities=dict(cap_map),
                references=dict(ref_map),
            )
        )
    return output


def find_shared_capabilities(
    normalized: list[NormalizedTeam],
    min_teams: int,
) -> list[SharedCapability]:
    team_count = max(len(normalized), 1)
    index: dict[str, set[str]] = defaultdict(set)
    for team in normalized:
        for cap in team.capabilities:
            index[cap].add(team.name)

    shared: list[SharedCapability] = []
    for cap, teams in sorted(index.items()):
        if len(teams) >= min_teams:
            shared.append(
                SharedCapability(
                    key=cap,
                    teams=sorted(teams),
                    confidence=round(len(teams) / team_count, 4),
                )
            )
    return shared
