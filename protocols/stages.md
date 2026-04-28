# Daily Pipeline Stages

1. Validate selected teams.
2. Refresh framework documentation availability matrix.
3. Ingest and normalize team content.
4. Analyze common capabilities and references.
5. Synthesize abstract team output.
6. Build AgentTeams integration request payload.
7. Emit stage registry.
8. Emit consolidated report.

## Guardrails

- No runtime dependency on external scripts in ~/.local/bin.
- Preserve provenance for shared capability/reference output.
- Support degraded-mode reporting when framework availability is partial.
