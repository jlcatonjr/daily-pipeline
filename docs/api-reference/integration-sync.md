# `integration.sync` — daily-pipeline

Callable Stage 9.5 helper APIs for deterministic AgentTeams synchronization.

> Source: `daily_pipeline/integration/sync.py`

---

## Execution Layer

This module supports orchestration extension behavior (Stage 9.5). It is callable from Python/CLI, but Stage 9.5 remains externally orchestrated and is not part of `run_protocol()`.

---

## Public Functions

### `discover_sync_targets(root_dir)`

Discover candidate repositories for Stage 9.5 sync.

Args:

- `root_dir` (`str`) — workspace root (commonly `$VK_ROOT`).

Returns:

- `list[str]` — absolute repo paths containing `.github/agents/_build-description.json`.

Notes:

- Checks `root_dir` itself and immediate child directories.

---

### `execute_agentteams_sync(target_repo, build_team_py=None, post_audit=False, dry_run=False)`

Run deterministic sync for one target repository.

Args:

- `target_repo` (`str`)
- `build_team_py` (`str | None`)
- `post_audit` (`bool`)
- `dry_run` (`bool`)

Returns:

- `SyncResult`

Path resolution order for `build_team_py`:

1. Explicit function argument
2. Environment fallback: `$AGENTTEAMS_REPO/build_team.py`

When called through CLI sync mode, the argument passed to this function is resolved as:

1. `--build-team-py`
2. `config.build_team_py`
3. Function-level environment fallback above

Skip/failure behavior:

- Returns `status='skipped'` for unresolved executable, missing build description, or dry-run.
- Returns `status='failed'` for subprocess non-zero exit or execution exceptions.
- Never raises; always returns `SyncResult`.
- Stage-level orchestration contract is best-effort/non-halting; standalone CLI sync may still exit non-zero when any target fails, for operator visibility.

Command invocation:

```bash
python <build_team.py> --description <target/.github/agents/_build-description.json> --project <target> --update --merge --yes [--post-audit]
```

---

## Internal Helpers

`_resolve_build_team_py()` is internal and not part of the stable public API contract.
