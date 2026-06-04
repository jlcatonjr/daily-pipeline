<!-- AGENTTEAMS:BEGIN content v=1 -->
# SETUP-REQUIRED.md

Setup status for project **daily-pipeline**.

## Resolution Summary (2026-04-28)

The previously unresolved setup values are now defined as:

1. `REFERENCE_DB_PATH`: `.github/agents/references/reference-db.csv`
2. `STYLE_REFERENCE_PATH`: `README.md`
3. `PIP_PACKAGE_NAME`: `daily-pipeline`
4. `DOC_SITE_CONFIG_FILE`: `N/A (no docs-site config in this repository)`

## Verification Notes

1. Generated agent files now reference concrete values for reference and style paths.
2. The reference database file exists at `.github/agents/references/reference-db.csv`.
3. Operational runbook added at `.github/agents/AGENT-TEAM-OPERATIONS.md`.

## Remaining Optional Manual Tokens

`{MANUAL:ADJACENT_REPO_PATH}` and `{MANUAL:ADJACENT_REPO_AGENTS_PATH}` remain in `.github/agents/references/adjacent-repos.md` as template fields for future cross-repository registry entries.
<!-- AGENTTEAMS:END content -->
