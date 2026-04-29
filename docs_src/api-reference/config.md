# `config` — daily-pipeline

Load and normalize pipeline configuration.

> Source: `daily_pipeline/config.py`

---

## Public Types

### `PipelineConfig`

Dataclass used by runtime code and CLI integration.

Fields:

- `capability_min_teams` (`int`)
- `reference_min_teams` (`int`)
- `confidence_floor` (`float`)
- `agentteams_repo` (`str`) — Stage 6 integration target path
- `build_team_py` (`str | None`) — Stage 9.5 helper executable path override

---

## Public Functions

### `load_config(config_path)`

Load config JSON from an explicit path, or fallback to `configs/defaults.json` when `config_path` is `None`.

Args:

- `config_path` (`str | None`) — optional path to config JSON file.

Returns:

- `PipelineConfig`

Notes:

- `build_team_py` falls back to `None` when unset.
- End-to-end Stage 9.5 resolution order in CLI path is `--build-team-py` argument, then `config.build_team_py`, then `$AGENTTEAMS_REPO/build_team.py` fallback in `integration/sync.py`.

---

## Authority Notes

- Config defaults: `configs/defaults.json`
- Team input schema: `configs/team-schema.json`
