# Getting Started

## Install

```bash
python3 -m pip install -e .
python3 -m daily_pipeline.cli --help
```

## Quick Core Run (Stages 1-8)

```bash
python3 -m daily_pipeline.cli \
  --team tests/fixtures/team_a.json \
  --team tests/fixtures/team_b.json \
  --output-root tmp/daily-pipeline
```

## Quick Stage 9.5 Helper Run

```bash
python3 -m daily_pipeline.cli \
  --sync \
  --root "$VK_ROOT" \
  --build-team-py "$BUILD_TEAM_PY" \
  --post-audit
```

## Dry Run Examples

Core mode dry run:

```bash
python3 -m daily_pipeline.cli --team tests/fixtures/team_a.json --dry-run
```

Sync mode dry run:

```bash
python3 -m daily_pipeline.cli --sync --root "$VK_ROOT" --build-team-py "$BUILD_TEAM_PY" --dry-run
```
