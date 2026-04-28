from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentRecord:
    name: str
    capabilities: list[str]
    references: list[str]


@dataclass
class TeamRecord:
    name: str
    framework: str
    source: str
    agents: list[AgentRecord]
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class NormalizedTeam:
    name: str
    framework: str
    source: str
    capabilities: dict[str, set[str]]
    references: dict[str, set[str]]


@dataclass
class SharedCapability:
    key: str
    teams: list[str]
    confidence: float


@dataclass
class SharedReference:
    key: str
    teams: list[str]
    freshness_tag: str
    confidence: float


@dataclass
class AbstractTeamOutput:
    name: str
    shared_capabilities: list[SharedCapability]
    shared_references: list[SharedReference]
    mapping: dict[str, dict[str, list[str]]]
    provenance: dict[str, list[str]]


@dataclass
class IntegrationRequest:
    trigger: str
    target_repo: str
    frameworks: list[str]
    abstract_team_name: str
    capability_confidence_floor: float
    reference_confidence_floor: float
    payload: dict[str, Any]


@dataclass
class StageResult:
    stage: str
    status: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class RunContext:
    run_date: str
    run_dir: str
    degraded_mode: bool
    framework_matrix: dict[str, str]


@dataclass
class SyncResult:
    target_repo: str
    status: str  # ok | skipped | failed
    skip_reason: str  # build_team_py_not_configured | build_team_py_not_found | build_description_missing | dry_run | ""
    raw_output: str  # captured stdout+stderr from subprocess; telemetry only
    warnings: list[str]
