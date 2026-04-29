# Daily Pipeline

API Reference: [docs/api-reference/index.md](docs/api-reference/index.md)

Standalone multi-team daily pipeline module for building abstract agent-team outputs and integration requests.

This repository has two execution layers:

- Core package protocol: stages 1-8 implemented in `daily_pipeline/protocol.py`
- Orchestration extension: stages 9, 9.5, 10, 10.1, 10.5, and 11 (externally orchestrated)

## Purpose

Daily Pipeline ingests selected team definitions, identifies shared capabilities and references, synthesizes an abstract team, and emits deterministic integration payloads for AgentTeams update-request flows.

## Scope

- Multi-team selection and ingestion
- Shared capability/reference analysis
- Abstract team synthesis with provenance + mapping
- Integration request payload generation
- Per-stage artifacts and consolidated reporting
- Operational guidance for orchestration extension stages

## Non-goals

- Direct runtime dependency on scripts in `~/.local/bin`

## Install

```bash
python3 -m pip install -e .
python3 -m daily_pipeline.cli --help
```

## Execution Modes

`daily_pipeline.cli` supports two operator-facing modes:

1. Team mode (core stages 1-8)
2. Sync mode (`--sync`) for Stage 9.5 callable helper execution

These are separate behavior paths in CLI routing.

### Team Mode (Core Protocol: Stages 1-8)

Run core pipeline from selected team files:

```bash
python3 -m daily_pipeline.cli \
	--team tests/fixtures/team_a.json \
	--team tests/fixtures/team_b.json \
	--output-root tmp/daily-pipeline
```

Optional flags:

- `--teams-file <path>`
- `--trigger team-create|team-update`
- `--allow-degraded`
- `--config <path>`
- `--dry-run`

Outputs:

- Stage JSON artifacts in `tmp/daily-pipeline/YYYY-MM-DD/`
- Integration request under `integration_requests/`
- Consolidated markdown report

### Sync Mode (`--sync`, Stage 9.5 Helper Path)

Run deterministic sync helper across discovered repositories:

```bash
python3 -m daily_pipeline.cli \
	--sync \
	--root "$VK_ROOT" \
	--build-team-py "$BUILD_TEAM_PY" \
	--post-audit
```

Dry-run example:

```bash
python3 -m daily_pipeline.cli \
	--sync \
	--root "$VK_ROOT" \
	--build-team-py "$BUILD_TEAM_PY" \
	--dry-run
```

Discovery scope for sync mode:

- `--root` directory itself
- Immediate child directories of `--root`

Repository is eligible when `.github/agents/_build-description.json` exists.

Notes:

- Sync mode is a callable helper interface for orchestration extension behavior.
- Stage 9.5 remains externally orchestrated and is not executed inside `run_protocol()`.
- Stage-level contract remains best-effort/non-halting; standalone CLI sync returns non-zero if any target fails so operators can detect partial failure.
- External script examples (such as `~/.local/bin/daily-pipeline.sh`) are optional runbook references, not runtime dependencies of core package execution.

## Stage References

- Stage index (core + orchestration extension): `protocols/stages.csv`
- Full stage contracts (core + orchestration extension): `protocols/stages.md`
- Extended operations runbook: `EXTENDED-PIPELINE-OPERATIONS.md`

## API Reference

- Documentation hub: `docs/index.md`
- API reference index: `docs/api-reference/index.md`
- CLI API: `docs/api-reference/cli.md`
- Protocol API: `docs/api-reference/protocol.md`
- Config API: `docs/api-reference/config.md`
- Models/contracts: `docs/api-reference/models.md`
- Integration payload API: `docs/api-reference/integration-agentteams.md`
- Stage 9.5 helper API: `docs/api-reference/integration-sync.md`

## Documentation Application (MkDocs)

This repository includes a docs application following the AgentTeams site pattern:

- Config: `mkdocs.yml`
- Docs app source: `docs_src/`
- Build output (default): `site/`

Install docs dependencies and run locally:

```bash
python3 -m pip install mkdocs mkdocs-material pymdown-extensions
mkdocs serve
```

Build static site:

```bash
mkdocs build
```
