# How It Works

## Core Protocol (Stages 1-8)

The core protocol performs deterministic ingestion, normalization, commonality analysis, abstract synthesis, integration-request construction, stage registry output, and reporting.

Core entrypoint:

- `daily_pipeline.protocol.run_protocol()`

## Orchestration Extension (Stages 9+)

Stages 9+ are externally orchestrated.

- Stage 9: external handoff stage
- Stage 9.5: deterministic sync helper path (callable APIs in `daily_pipeline/integration/sync.py`)
- Stages 10, 10.1, 10.5, 11: cross-repository investigation/remediation operations

Stage 9.5 helper behavior is best-effort for orchestration progression. Standalone CLI sync can return non-zero when one or more targets fail, for operator visibility.

## Discovery Scope in Stage 9.5 Helper Path

`discover_sync_targets(root_dir)` checks:

1. `root_dir` itself
2. Immediate child directories of `root_dir`

A directory is considered eligible when `.github/agents/_build-description.json` is present.

## Runtime Boundary

Core package execution does not require scripts from `~/.local/bin`. External script references are optional orchestration runbook examples.
