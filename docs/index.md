# Documentation Hub — daily-pipeline

Central navigation for daily-pipeline operational and API documentation.

This documentation set preserves execution-layer boundaries:

- Core protocol execution: stages 1-8 (`daily_pipeline/protocol.py`)
- Orchestration extension: stages 9+ (externally orchestrated), with Stage 9.5 callable helpers documented in API reference

---

## Core Operational Documents

- [README](../README.md) — project overview, install, CLI usage
- [Stage Contracts](../protocols/stages.md) — full stage-by-stage contracts
- [Stage Index CSV](../protocols/stages.csv) — compact stage registry
- [Extended Operations Runbook](../EXTENDED-PIPELINE-OPERATIONS.md) — orchestration extension operations

---

## API Reference

- [API Reference Index](api-reference/index.md)
- [CLI API](api-reference/cli.md)
- [Protocol API](api-reference/protocol.md)
- [Config API](api-reference/config.md)
- [Models/Contracts API](api-reference/models.md)
- [Integration Payload API](api-reference/integration-agentteams.md)
- [Stage 9.5 Helper API](api-reference/integration-sync.md)

---

## Notes

- External script examples are optional operational references and are not required runtime dependencies for core package execution.
- For deterministic sync helper behavior and CLI status semantics, see the Stage 9.5 sections in both stage contracts and API docs.
