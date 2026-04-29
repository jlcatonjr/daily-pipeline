# `models` — daily-pipeline

Shared dataclass contracts for ingestion, analysis, synthesis, integration, reporting, and sync operations.

> Source: `daily_pipeline/models.py`

---

## Public Dataclasses

### Team/Agent Contracts

- `AgentRecord`
- `TeamRecord`
- `NormalizedTeam`

### Shared Analysis Contracts

- `SharedCapability`
- `SharedReference`

### Synthesis/Integration Contracts

- `AbstractTeamOutput`
- `IntegrationRequest`

### Reporting Contracts

- `StageResult`
- `RunContext`

### Stage 9.5 Helper Contract

- `SyncResult`
  - `status` values: `ok`, `skipped`, `failed`
  - `skip_reason` values when skipped:
    - `build_team_py_not_configured`
    - `build_team_py_not_found`
    - `build_description_missing`
    - `dry_run`

---

## Notes

These dataclasses are shared across modules and are part of the documented API contract for this repository's public interfaces.
