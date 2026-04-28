from __future__ import annotations

from collections import defaultdict

from daily_pipeline.models import NormalizedTeam, SharedReference


def _freshness_tag(reference_key: str) -> str:
    if "2026" in reference_key or "latest" in reference_key:
        return "fresh"
    return "unknown"


def find_shared_references(
    normalized: list[NormalizedTeam],
    min_teams: int,
) -> list[SharedReference]:
    team_count = max(len(normalized), 1)
    index: dict[str, set[str]] = defaultdict(set)

    for team in normalized:
        for ref in team.references:
            index[ref].add(team.name)

    shared: list[SharedReference] = []
    for ref, teams in sorted(index.items()):
        if len(teams) >= min_teams:
            shared.append(
                SharedReference(
                    key=ref,
                    teams=sorted(teams),
                    freshness_tag=_freshness_tag(ref),
                    confidence=round(len(teams) / team_count, 4),
                )
            )
    return shared
