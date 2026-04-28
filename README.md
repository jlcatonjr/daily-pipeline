# Daily Pipeline

Standalone multi-team daily pipeline module.

## Purpose

This repository builds abstract agent teams from selected source teams by finding shared capabilities and shared references, then prepares integration requests for AgentTeams update flows.

## Scope

- Multi-team selection and ingestion
- Common function/reference analysis
- Abstract team synthesis
- AgentTeams create/update integration requests
- Per-stage and consolidated reporting

## Non-goals

- Direct runtime dependency on scripts in `~/.local/bin`

## Quick start

```bash
python -m pip install -e .
daily-pipeline --help
```
