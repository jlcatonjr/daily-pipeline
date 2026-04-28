# Daily-Pipeline Agent Team Handoff Plan

Date: 2026-04-28
Repository: /Users/jamescaton/githubrepositories/daily-pipeline
Framework: VS Code Copilot agent team (.github/agents)

## 1) Handoff Objective

Transfer operational ownership of the generated Copilot agent team for daily-pipeline so maintainers can:

1. Keep agent definitions aligned with repository architecture.
2. Safely run update/regeneration workflows with AgentTeams.
3. Complete required manual setup values and validate consistency.

## 2) Current State Snapshot

1. Agent team generated under `.github/agents/`.
2. Current generated agent markdown files: 26.
3. Build description source:
   - `.github/agents/_build-description.json`
4. Manual setup tracker present:
   - `.github/agents/SETUP-REQUIRED.md`

## 3) Required Manual Completion (Blocker Before Production Use)

Resolve placeholders listed in `.github/agents/SETUP-REQUIRED.md`:

1. `{MANUAL:REFERENCE_DB_PATH}`
2. `{MANUAL:STYLE_REFERENCE_PATH}`
3. `{MANUAL:PIP_PACKAGE_NAME}`
4. `{MANUAL:DOC_SITE_CONFIG_FILE}`

Owner action:

1. Search all generated agent files for `{MANUAL:*}` tokens.
2. Replace with repository-valid values.
3. Run post-resolution consistency check (see Section 5).

## 4) Ownership and Roles

Primary owner:

1. Daily-pipeline maintainer assigned to `.github/agents/` governance.

Secondary owner:

1. AgentTeams maintainer for regeneration workflow and schema updates.

Escalation:

1. Architecture drift or role ambiguity: `orchestrator.agent.md` + `conflict-auditor.agent.md`.
2. Documentation/best-practice drift: `agent-updater.agent.md` + `adversarial.agent.md`.

## 5) Validation Runbook

Baseline checks:

1. Confirm no unresolved setup placeholders remain.
2. Confirm required governance agents exist:
   - `orchestrator.agent.md`
   - `primary-producer.agent.md`
   - `conflict-auditor.agent.md`
   - `adversarial.agent.md`
   - `agent-updater.agent.md`

Recommended command sequence from `agentteams` repository:

```bash
python3 build_team.py \
  --description /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents/_build-description.json \
  --project /Users/jamescaton/githubrepositories/daily-pipeline \
  --framework copilot-vscode \
  --output /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents \
  --check
```

If drift is found:

```bash
python3 build_team.py \
  --description /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents/_build-description.json \
  --project /Users/jamescaton/githubrepositories/daily-pipeline \
  --framework copilot-vscode \
  --output /Users/jamescaton/githubrepositories/daily-pipeline/.github/agents \
  --update --merge --yes
```

## 6) Ongoing Maintenance Policy

1. Regenerate after major architecture changes in `daily_pipeline/`.
2. Re-run check/update after toolchain updates (Python, pytest, packaging metadata).
3. Keep `_build-description.json` synchronized with actual components and quality criteria.
4. Treat external `~/.local/bin` scripts as reference-only, not runtime dependencies.

## 7) Change-Control Checklist

Before modifying agent definitions:

1. Update `_build-description.json` first.
2. Run `--check` before `--update`.
3. Use `--merge` unless a full overwrite is explicitly intended.
4. Record unresolved risks in a short handoff note in repository root or `.github/agents/outputs/`.

## 8) Acceptance Criteria for Handoff Completion

1. All manual placeholders are resolved.
2. `build_team.py --check` returns no blocking drift.
3. Governance agents are present and readable.
4. Maintainer can execute update workflow successfully.

## 9) First Follow-Up Tasks

1. Fill all `{MANUAL:*}` placeholders and rerun `--check`.
2. Add a brief `AGENT-TEAM-OPERATIONS.md` in `.github/agents/` with maintainer ownership and update cadence.
3. Add an automated quality check task to run `build_team.py --check` periodically.
