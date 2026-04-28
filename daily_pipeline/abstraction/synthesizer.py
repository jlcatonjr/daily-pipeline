from __future__ import annotations

from daily_pipeline.models import (
    AbstractTeamOutput,
    NormalizedTeam,
    SharedCapability,
    SharedReference,
)


def synthesize_abstract_team(
    name: str,
    normalized: list[NormalizedTeam],
    capabilities: list[SharedCapability],
    references: list[SharedReference],
) -> AbstractTeamOutput:
    shared_cap_keys = {item.key for item in capabilities}
    mapping: dict[str, dict[str, list[str]]] = {}
    provenance: dict[str, list[str]] = {}

    for team in normalized:
        team_map: dict[str, list[str]] = {}
        for cap, agents in team.capabilities.items():
            if cap in shared_cap_keys:
                team_map[cap] = sorted(agents)
                provenance.setdefault(cap, []).append(team.name)
        mapping[team.name] = team_map

    for key in list(provenance.keys()):
        provenance[key] = sorted(set(provenance[key]))

    return AbstractTeamOutput(
        name=name,
        shared_capabilities=capabilities,
        shared_references=references,
        mapping=mapping,
        provenance=provenance,
    )
