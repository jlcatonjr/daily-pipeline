# `protocol` — daily-pipeline

Execute the core daily-pipeline protocol.

> Source: `daily_pipeline/protocol.py`

---

## Public Functions

### `run_protocol(team_paths, config, trigger, output_root, allow_degraded)`

Run core stages 1-8 and return report metadata.

Args:

- `team_paths` (`list[str]`) — selected team JSON files.
- `config` (`PipelineConfig`) — runtime thresholds and integration target settings.
- `trigger` (`str`) — integration trigger (`team-create` or `team-update`).
- `output_root` (`str`) — root path for stage outputs.
- `allow_degraded` (`bool`) — permit degraded mode continuation when framework matrix indicates unavailable frameworks.

Returns:

- `dict[str, str]` with keys:
  - `run_dir`
  - `report`

Behavior summary:

- Stages 1-8 are executed in sequence.
- If stage 2 detects degraded mode and `allow_degraded=False`, execution exits early with blocked stage result and consolidated report.

---

## Execution Boundary

This module is authoritative for core Stages 1-8 only.

Stage 9+ orchestration behavior is external. Stage 9.5 helper callables live in `daily_pipeline/integration/sync.py` and are not executed by `run_protocol()`.

See `protocols/stages.md` for full contracts.
