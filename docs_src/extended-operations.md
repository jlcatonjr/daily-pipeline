# Extended Operations

Operational runbook for orchestration extension stages is maintained in:

- `EXTENDED-PIPELINE-OPERATIONS.md`

Related pages:

- [Stage Contracts](stage-contracts.md)

Repository source file:

- `EXTENDED-PIPELINE-OPERATIONS.md`

Key lock points carried into this docs app:

- Stage 9.5 helper path in-package is callable, but orchestration ownership remains external.
- Stage-level progression is best-effort; standalone sync CLI can return non-zero on failed targets.
- Core package runtime remains independent of `~/.local/bin` script dependencies.
