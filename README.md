# Daily Pipeline

Standalone multi-team daily pipeline module.

This repository documents two related execution layers:
- Core package protocol: 8 stages implemented in `daily_pipeline/protocol.py`
- Workspace orchestration extension: stages 9, 9.5, 10, 10.1, 10.5, and 11 (driven by external orchestration)

## Purpose

This repository builds abstract agent teams from selected source teams by finding shared capabilities and shared references, then prepares integration requests for AgentTeams update flows.

## Scope

- Multi-team selection and ingestion
- Common function/reference analysis
- Abstract team synthesis
- AgentTeams create/update integration requests
- Per-stage and consolidated reporting
- Documentation and operations guidance for extended workspace orchestration

## Non-goals

- Direct runtime dependency on scripts in `~/.local/bin`

## Stage Specifications

- Stage index (core + orchestration extension): `protocols/stages.csv`
- Full stage contracts (core + orchestration extension): `protocols/stages.md`
- Extended operations runbook: `EXTENDED-PIPELINE-OPERATIONS.md`

## Quick start

```bash
python -m pip install -e .
daily-pipeline --help
```
