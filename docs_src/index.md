# Daily Pipeline Documentation

Daily Pipeline provides two coordinated execution layers:

1. Core protocol (Stages 1-8) implemented in `daily_pipeline/protocol.py`
2. Orchestration extension (Stages 9+) operated externally, with Stage 9.5 callable helper APIs available in `daily_pipeline/integration/sync.py`

## Documentation Map

- [Getting Started](getting-started.md)
- [How It Works](how-it-works.md)
- [CLI Reference](cli-reference.md)
- [Stage Contracts](stage-contracts.md)
- [Extended Operations](extended-operations.md)
- [API Reference](api-reference/index.md)

## Source-of-Truth Notes

For this docs application:

- `docs_src/` is the authoring source for MkDocs pages and navigation.
- Repository reference docs under `docs/` remain available for direct Markdown browsing.

Execution semantics remain authoritative in:

- `daily_pipeline/` implementation behavior
- `protocols/stages.md` and `protocols/stages.csv`
- `configs/` and `tests/`
