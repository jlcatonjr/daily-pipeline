# API Reference — daily-pipeline

Public API reference for the `daily_pipeline` package.

This reference documents the supported operator/developer-facing API surface. Underscored helpers are internal and may change without notice.

---

## Execution Layers

| Layer | Scope |
|------|------|
| Core protocol | Stages 1-8 executed by `daily_pipeline.protocol.run_protocol()` |
| Orchestration extension | Stages 9+ executed externally; Stage 9.5 has callable helpers in `integration/sync.py` |

For stage contracts, see [Stage Contracts](../stage-contracts.md).

---

## Core Modules

| Module | Role |
|------|------|
| [`config`](config.md) | Load runtime configuration (`PipelineConfig`) |
| [`protocol`](protocol.md) | Execute core Stages 1-8 |
| [`models`](models.md) | Shared dataclass contracts used across pipeline stages |
| [`cli`](cli.md) | CLI entrypoints for team mode and sync mode |

## Integration Modules

| Module | Role |
|------|------|
| [`integration-agentteams`](integration-agentteams.md) | Build and write Stage 6 integration request payloads |
| [`integration-sync`](integration-sync.md) | Stage 9.5 callable helpers for deterministic AgentTeams sync |

---

## Typical Usage

Core run (Stages 1-8):

```bash
python3 -m daily_pipeline.cli \
  --team tests/fixtures/team_a.json \
  --team tests/fixtures/team_b.json \
  --output-root tmp/daily-pipeline
```

Stage 9.5 helper path (external orchestration support):

```bash
python3 -m daily_pipeline.cli \
  --sync \
  --root "$VK_ROOT" \
  --build-team-py "$BUILD_TEAM_PY" \
  --post-audit
```

The sync path is a callable/helper interface for orchestration extension behavior. It does not move Stage 9.5 into core `run_protocol()` execution.
