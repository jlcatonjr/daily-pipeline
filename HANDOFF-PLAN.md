# Daily-Pipeline Agent Team Handoff Plan

Date: 2026-04-28
Repository: daily-pipeline
Framework: VS Code Copilot agent team (.github/agents)

## 1) Handoff Objective

Transfer operational ownership of the generated Copilot agent team for daily-pipeline so maintainers can:

1. Keep agent definitions aligned with repository architecture.
2. Safely run update/regeneration workflows with AgentTeams.
3. Complete required manual setup values and validate consistency.

## 2) Current State Snapshot

1. Agent team generated under `.github/agents/`.
2. Generated agent markdown files are present under `.github/agents/` (count may change after regeneration).
3. Build description source:
   - `.github/agents/_build-description.json`
4. Manual setup tracker present:
   - `.github/agents/SETUP-REQUIRED.md`

## 3) Required Manual Completion (Historical Blocker - Resolved)

Status: Resolved on 2026-04-28. This section is retained as historical context for future regenerations.

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

Recommended command sequence from the daily-pipeline repository root:

```bash
python3 "$AGENTTEAMS_REPO/build_team.py" \
  --description .github/agents/_build-description.json \
  --project . \
  --framework copilot-vscode \
  --output .github/agents \
  --check
```

If drift is found:

```bash
python3 "$AGENTTEAMS_REPO/build_team.py" \
  --description .github/agents/_build-description.json \
  --project . \
  --framework copilot-vscode \
  --output .github/agents \
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

1. All required manual placeholders are resolved (optional adjacent-repo placeholders may remain as templates).
2. `build_team.py --check` returns no blocking drift.
3. Governance agents are present and readable.
4. Maintainer can execute update workflow successfully.

## 9) First Follow-Up Tasks

### Completed (✅ Handoff Acceptance Criteria)

1. ✅ Filled all required `{MANUAL:*}` placeholders; reran `--check`; no blocking drift remains
2. ✅ Added `.github/agents/AGENT-TEAM-OPERATIONS.md` with maintainer ownership and update cadence
3. ✅ Added `.vscode/tasks.json` automated quality check task (runs `build_team.py --check`)

### Pending (📋 Extended Pipeline Integration)

The daily-pipeline repository is part of a larger **Visual Knowledge workspace orchestration** with an extended stage model:
- Core package protocol: Stages 1–8 (implemented in `daily_pipeline/protocol.py`)
- External orchestration extension: Stages 9, 9.5, 10, 10.1, 10.5, and 11 (managed by external orchestration)

Two integration documents capture this model:

1. **`protocols/stages.md` (Extended)** — Now documents all 11 stages with input/output contracts, agent invocations, and failure handling:
   - Stages 1–8: Core package protocol (unchanged implementation; now fully documented)
   - Stage 9: External pipeline orchestration handoff stage
   - Stage 9.5: Deterministic AgentTeams synchronization (repo structural alignment)
   - Stage 10: Visual Knowledge investigation (cross-repo consistency analysis)
   - Stage 10.1: Adversarial review of investigation conclusions (presupposition validation)
   - Stage 10.5: Source-aware agent-updater synchronization (abstract team propagation)
   - Stage 11: Visual Knowledge remediation (cross-repo execution and git reconciliation)

2. **`EXTENDED-PIPELINE-OPERATIONS.md` (New)** — Operations runbook for Stages 9.5–11:
   - VK workspace architecture (collector repos, source repos, discovery logic)
   - Per-stage deployment model and governance ownership
   - Execution patterns (parallel vs. sequential; retry/fallback policies)
   - Operational procedures (pre-run checklist, troubleshooting, cron integration)
   - Integration with external orchestration script (`~/.local/bin/daily-pipeline.sh`)

### Integration Roadmap

**Next steps for VK workspace coordination:**

1. **Validate Stage Alignment:** Verify daily-pipeline's internal 8-stage model (Stages 1–8) matches `daily_pipeline/protocol.py` implementation and maps correctly into external Stage 9 orchestration handoff
2. **Test Stage 9.5 Execution:** Run deterministic sync on candidate repos; validate orchestrator.agent.md Workflow 10/11 presence
3. **Stage 10 Pilot:** Invoke orchestrator agent in test collector repo; review investigation report quality
4. **Stage 10.1 Validation:** Run adversarial review on pilot investigation; assess presupposition coverage
5. **Stage 11 Dry-Run:** Test remediation on isolated repo (non-production); validate git operations and commit structure
6. **Deployment to Production VK Workspace:** Roll out Stages 9.5–11 to full VK_ROOT with daily-pipeline.sh orchestration
7. **Establish Maintenance Cadence:** Set up cron scheduling (daily 09:00) and post-run review procedures

**Governance:** Daily-pipeline maintainer is responsible for core Stages 1–8, Stage 9 handoff integrity, and Stage 9.5 deterministic sync. VK workspace orchestrator agents (orchestrator, adversarial, reference-manager) own Stages 10-11 execution quality. See `EXTENDED-PIPELINE-OPERATIONS.md` Stage RACI section for canonical ownership.

**Authority Hierarchy:** All decisions follow the standard hierarchy (Package Source > Protocols > Configs > Tests). Extended pipeline stages inherit the same governance model as the core daily-pipeline.
