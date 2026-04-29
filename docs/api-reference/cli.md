# `cli` — daily-pipeline

Command-line entrypoint for core protocol runs and Stage 9.5 sync helper runs.

> Source: `daily_pipeline/cli.py`

---

## Public Entry Point

### `main()`

Parses CLI flags and routes execution to one of two modes:

1. Team mode (core Stages 1-8)
2. Sync mode (`--sync`) for Stage 9.5 helper execution

---

## Team Mode (Core Protocol)

Required inputs:

- `--team <path>` (repeatable), or
- `--teams-file <path>` (one team path per line)

Optional flags:

- `--config`
- `--trigger` (`team-create` or `team-update`)
- `--output-root`
- `--allow-degraded`
- `--dry-run`

Execution target:

- Calls `daily_pipeline.protocol.run_protocol()`

---

## Sync Mode (Stage 9.5 Helper Path)

Mode selector:

- `--sync`

Optional flags:

- `--root` (default `$VK_ROOT` or `.`)
- `--build-team-py`
- `--post-audit`
- `--dry-run`

Execution target:

- Calls `discover_sync_targets()` and `execute_agentteams_sync()` from `daily_pipeline.integration.sync`

Behavior:

- Routing is separated between team-mode execution and sync-mode execution.
- Parser-level exclusivity is enforced for `--team` and `--sync`.
- `--teams-file` remains a team-mode input and is not consumed in sync-mode execution.
- Process exits non-zero if any sync target returns `failed` status.

---

## Internal Helpers

Underscored functions (`_parser`, `_resolve_team_paths`, `_run_sync`) are internal implementation helpers and are not part of the stable public API contract.
