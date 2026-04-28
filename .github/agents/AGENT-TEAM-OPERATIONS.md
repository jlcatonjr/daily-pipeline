# Agent Team Operations

Date created: 2026-04-28
Scope: Operational maintenance for the generated Copilot agent team in this repository.

## Ownership

Primary owner: daily-pipeline maintainer responsible for `.github/agents/`.
Secondary owner: AgentTeams maintainer responsible for template and schema updates.
Escalation (role/scope conflicts): `orchestrator.agent.md` and `conflict-auditor.agent.md`.

## Update Cadence

- Weekly: run drift check (`build_team.py --check`).
- On structural changes: run drift check immediately after updates to `daily_pipeline/`, `protocols/`, `configs/`, or `tests/`.
- On toolchain changes: rerun check after Python/pytest/packaging changes.

## Operational Runbook

1. Validate no unresolved `{MANUAL:*}` placeholders remain in `.github/agents/`.
2. Run `build_team.py --check` using the project description file.
3. If drift is reported, run `build_team.py --update --merge --yes`.
4. Re-run `build_team.py --check` to confirm clean state.
5. Review diffs before committing.

## Standard Commands

Run from `/Users/jamescaton/githubrepositories/agentteams`:

```bash
python3 build_team.py \
  --description /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents/_build-description.json \
  --project /Users/jamescaton/githubrepositories/daily-pipeline \
  --framework copilot-vscode \
  --output /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents \
  --check
```

```bash
python3 build_team.py \
  --description /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents/_build-description.json \
  --project /Users/jamescaton/githubrepositories/daily-pipeline \
  --framework copilot-vscode \
  --output /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents \
  --update --merge --yes
```

## Automated Quality Check

Use the `Agent Team Check` VS Code task in `.vscode/tasks.json`.
Recommended local scheduling: run this task at least weekly.
