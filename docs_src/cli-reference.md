# CLI Reference

`daily_pipeline.cli` supports two routing paths.

## Team Mode (Core Protocol)

Core protocol execution for selected team files:

```bash
python3 -m daily_pipeline.cli \
  --team <team-a.json> \
  --team <team-b.json> \
  --output-root tmp/daily-pipeline
```

Common flags:

- `--teams-file`
- `--config`
- `--trigger team-create|team-update`
- `--allow-degraded`
- `--dry-run`

## Sync Mode (Stage 9.5 Helper Path)

```bash
python3 -m daily_pipeline.cli \
  --sync \
  --root "$VK_ROOT" \
  --build-team-py "$BUILD_TEAM_PY" \
  --post-audit
```

Common sync flags:

- `--root` (defaults to `$VK_ROOT` or `.`)
- `--build-team-py`
- `--post-audit`
- `--dry-run`

Notes:

- Routing is separated between team-mode and sync-mode behavior.
- Parser exclusivity is enforced for `--team` and `--sync`.
- `--teams-file` is a team-mode input and is not consumed in sync-mode execution.
