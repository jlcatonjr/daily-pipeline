# Extended Pipeline Operations — Visual Knowledge Workspace Orchestration

**Document:** EXTENDED-PIPELINE-OPERATIONS.md  
**Scope:** Stage 9 context plus detailed operations for Stages 9.5–11 of the daily-pipeline extension; Visual Knowledge workspace orchestration  
**Audience:** Daily-pipeline maintainers; Visual Knowledge workspace orchestrators; infrastructure support  
**Authority:** Daily-pipeline repository protocol docs and implementation; external orchestration scripts are execution references

---

## Overview

The daily-pipeline repository implements an 8-stage research and synthesis pipeline (Stages 1–8 in package code). This pipeline is embedded within a larger **Visual Knowledge workspace orchestration** that adds external handoff and workspace stages (9, 9.5–11):

- **Stage 9 — Pipeline Orchestration Handoff:** External orchestrator transition from core package outputs to workspace-level execution
- **Stage 9.5 — Deterministic AgentTeams Sync:** Structural alignment pass before AI-driven investigation
- **Stages 10–11 — VK Investigation & Remediation:** Cross-workspace consistency detection and remediation

An external orchestration script (for example `~/.local/bin/daily-pipeline.sh`) can orchestrate the full 11-stage pipeline. This document explains the architectural relationship and governance model.

---

## Visual Knowledge Workspace Architecture

### Directory Structure

```
VK_ROOT
├── daily-pipeline/               (this repository)
│   ├── daily_pipeline/           (Python package: Stages 1–8)
│   ├── protocols/stages.md        (this stage specification)
│   ├── .github/agents/            (generated Copilot agent team)
│   └── tmp/daily-pipeline/YYYY-MM-DD/ (daily-pipeline stage artifacts and report)
│
├── collector-repo-1/             (Copilot agent team under investigation)
│   ├── .github/agents/orchestrator.agent.md
│   ├── .github/agents/outputs/investigation-report-YYYY-MM-DD.md
│   └── [application code]
│
├── collector-repo-2/
│   └── [same structure as collector-repo-1]
│
├── source-repo-A/                (Upstream protocol/capability definitions)
│   ├── .github/agents/
│   └── [protocol definitions, shared capabilities]
│
└── [additional collector/source repos...]
```

### Terminology

**Collector Repo:** A repository with `.github/agents/orchestrator.agent.md`. Collector repos are the targets of Stage 10 investigation and Stage 11 remediation. They aggregate capability definitions from upstream source repos and coordinate cross-workspace consistency.

**Source Repo:** An upstream repository that defines protocols, shared capabilities, or agent definitions that are referenced by collector repos. Examples: agentteams, shared-protocols, capability-registry. Source repos are discovered via the external orchestration source-SHA detector (not core Stage 8); their state informs Stage 10 investigations.

**VK Root:** The directory containing all collector and source repos; identified by the `VK_ROOT` environment variable in external orchestration. Default: workspace root containing daily-pipeline and sibling repos.

Portability note: absolute paths in this document are examples from one workstation. Prefer environment-variable-driven values (`VK_ROOT`, `COPILOT_BIN`, `BUILD_TEAM_PY`, `LOG_DIR`) in operational scripts and local runbooks.

---

## Stages 9.5–11: Execution Model

### Stage 9.5 — Deterministic AgentTeams Synchronization

**What it does:**
- Discovers all repos with `.github/agents/_build-description.json` (build metadata)
- Runs `build_team.py --update --merge --yes` on each repo
- Validates that orchestrator.agent.md contains Plan Documentation and Review (Workflow 10) and Final Check (Workflow 11)
- Writes machine-readable summary for trend analysis

**Why it's needed:**
- Ensures all collector repos are structurally aligned before Stage 10 investigation
- Avoids false-positive drift findings caused by stale agent template versions
- Deterministic (no AI involved); can short-circuit if no metadata present

**Deployment:**
- External dependency: `build_team.py` from agentteams repository
- Location check: `$BUILD_TEAM_PY` (for example `~/githubrepositories/agentteams/build_team.py`)
- If missing: Stage 9.5 skips with warning; pipeline continues
- Python-callable helpers: `daily_pipeline.integration.sync` provides `discover_sync_targets(root_dir)` and `execute_agentteams_sync(target_repo, build_team_py, post_audit, dry_run)` for direct use by external orchestration code
- Config field: `build_team_py` in `configs/defaults.json` (separate from `agentteams_repo`; see semantics note below)
- Semantics: `agentteams_repo` = integration payload target (Stage 6 use); `build_team_py` = path to `build_team.py` executable (Stage 9.5 use)

**Governance:**
- Owner: daily-pipeline maintainer (responsible for configuring build metadata in each repo)
- Escalation: If sync fails, check `.github/agents/_build-description.json` validity and AgentTeams toolchain version

### Stage 10 — Visual Knowledge Investigation

**What it does:**
- Discovers collector repos (repos with orchestrator.agent.md)
- Invokes orchestrator agent in each repo with 15-minute timeout
- Prompt includes: source-SHA change summaries from external orchestration, workspace scope, and investigation objectives
- Orchestrator writes investigation report with `## Orchestrator Instructions` section (remediation plan)

**Why it's needed:**
- Multi-repo consistency audit: detects capability cross-references, capability gaps, integration issues
- Cross-repo impact analysis: identifies downstream effects of upstream changes (source-SHA detector inputs)
- Remediation planning: orchestrator synthesizes a plan tailored to each repo's specific state

**Execution Pattern:**
- Sequential: runs one repo at a time (orchestrator agent can be long-running, up to 15 minutes)
- No retry: if orchestrator fails, repo is skipped with warning; continues to next repo
- Fallback: if investigation report missing, Stage 11 skips that repo

**Governance:**
- Owner: VK workspace lead (operational accountability), executed by per-repo orchestrator agents
- Escalation: If investigation findings seem incorrect, escalate to orchestrator agent author via VK workspace lead

### Stage 10.1 — Adversarial Review of Investigation Conclusions

**What it does:**
- Post-processes Stage 10 investigation reports
- Invokes adversarial agent in each repo with 600-second timeout
- Prompt includes: full investigation report, 6-step Critique Protocol (CAUSAL_CLAIM, DATA_STATE, SCOPE_BOUNDARY, TEMPORAL, cascade analysis, Recommendation)
- Appends findings to investigation report as `## Stage 10.1 Adversarial Review` section

**Why it's needed:**
- Validates investigator presuppositions: Is drift causal or correlational? Were file states verified? Is scope boundary accurate? Is temporal state current?
- Cascade analysis: Traces which specific remediation instructions depend on each presupposition
- Confidence filter: Allows operators to assess which recommendations are high-confidence vs. require manual review

**Failure Handling:**
- Advisory stage: failures do NOT halt pipeline or add repos to VK_FAILED
- If adversarial agent missing: skipped per-repo with warning
- Proceed to Stage 11 even if Stage 10.1 unavailable

**Governance:**
- Owner: VK workspace lead (operational accountability), executed by per-repo adversarial agents
- Escalation: If adversarial findings conflict with investigation findings, route to conflict-auditor via VK workspace lead

### Stage 10.5 — Source-Aware Agent-Updater Synchronization

**What it does:**
- Detects which source repositories have changed (SHA-based comparison against cached prior-run state)
- For each changed source: invokes agent-updater with source-state awareness
- Updates abstract team definition (from Stage 5) to reflect new capabilities/changes
- Updates downstream integration payloads

**Why it's needed:**
- Bridge between external source-SHA change detection and Stage 11 remediation at repo level
- Ensures Stage 11 remediation incorporates latest upstream capability state
- Deterministic: source change detection enables short-circuit if no upstream changes

**Failure Handling:**
- Best-effort: failures logged but do not halt pipeline
- If agent-updater unavailable: changes proceed to Stage 11 without source-aware updates

**Governance:**
- Owner: VK workspace lead (operational accountability), executed by agent-updater/reference-manager workflows
- Escalation: If source updates conflict with existing abstractions, escalate to reference-manager via VK workspace lead

### Stage 11 — Per-Repo Remediation

**What it does:**
1. **Phase A — Filter eligible repos:** Find repos with investigation reports; preflight-probe orchestrator agents
2. **Phase B — Parallel dispatch:** Launch up to 4 concurrent Copilot CLI calls; each invokes local orchestrator with remediation prompt (includes Stage 10 findings + 10.1 adversarial review + 10.5 abstract updates)
3. **Phase C — Result collection:** Wait for all parallel jobs; collect success/failure status
4. **Phase D — Sequential commit/push:** For successful repos, commit residual changes and push to origin

**Why it's needed:**
- Applies remediation decisions (from Stage 10) in each collector repo's local context
- Parallelization (Phase B) accelerates multi-repo remediation without sacrificing git integrity
- Sequential push (Phase D) avoids merge conflicts and race conditions across repos

**Execution Pattern:**
- Parallel within Phase B (up to 4 repos at once, limited by Copilot CLI concurrency budget)
- Sequential within Phase D (commit/push one repo at a time)
- Idempotent: safe to re-run on failed repos without duplicating prior changes

**Failure Handling:**
- Per-repo failures: logged to VK_FAILED array; no commit/push attempted
- Preflight failures (missing orchestrator agent): skipped with warning; doesn't block other repos
- Final exit code: 1 if any repo in VK_FAILED (indicates operator follow-up needed)

**Governance:**
- Owner: VK workspace lead (operational accountability), executed by per-repo orchestrator agents
- Escalation: If remediation produces unexpected changes, escalate to orchestrator agent author via VK workspace lead

---

## Governance Model

### Ownership

| **Role** | **Responsibility** | **Repository/File** |
|----------|-------------------|-------------------|
| Daily-pipeline maintainer | Operate and maintain Stages 1–8; ensure Stage 9 handoff integrity; configure Stage 9.5 metadata | daily-pipeline/ + all repos' `_build-description.json` |
| Orchestrator agent author | Design Stage 10 investigation prompts; refine Stage 11 remediation actions | Orchestrator agent definition; Stage 10/11 prompt templates |
| Adversarial agent author | Design Stage 10.1 critique protocols; challenge presuppositions | Adversarial agent definition; 6-step critique methodology |
| Conflict-auditor | Review Stage 10.1 findings; escalate contradictions | Conflict-auditor agent definition |
| Reference-manager | Manage Stage 10.5 source SHA tracking; abstract team propagation | Reference database; abstract team definition |
| VK workspace lead | Coordinate across all agents; make final remediation decisions | VK_ROOT/.github/WORKSPACE-OPERATIONS.md (if exists) |

### Stage RACI (Canonical)

| Stage | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| 9 | daily-pipeline maintainer | daily-pipeline maintainer | VK workspace lead | collector repo maintainers |
| 9.5 | daily-pipeline maintainer | daily-pipeline maintainer | AgentTeams maintainer | VK workspace lead |
| 10 | per-repo orchestrator agent | VK workspace lead | orchestrator agent author, daily-pipeline maintainer | collector repo maintainers |
| 10.1 | per-repo adversarial agent | VK workspace lead | conflict-auditor, adversarial agent author | collector repo maintainers |
| 10.5 | agent-updater/reference-manager workflow | VK workspace lead | reference-manager, daily-pipeline maintainer | collector repo maintainers |
| 11 | per-repo orchestrator agent | VK workspace lead | orchestrator agent author, conflict-auditor | collector repo maintainers |

### Decision Authority (Authority Hierarchy)

1. **Package Source** (`daily_pipeline/` module implementation) — Authoritative for Stage 1–8 behavior
2. **Protocol Definitions** (`protocols/stages.md`) — Authoritative for stage contracts and execution order
3. **Configuration Schemas** (`configs/`, `_build-description.json`) — Authoritative for input validation and build metadata
4. **Test Suite** (`tests/`) — Authoritative for expected behavior and regressions

External orchestration scripts are execution references only and are not authority sources.

### Escalation Paths

| **Issue** | **Primary Escalation** | **Secondary** | **Authority** |
|-----------|----------------------|--------------|---|
| Stage 9.5 sync fails; suspect build metadata | Daily-pipeline maintainer → AgentTeams maintainer | Code-hygiene agent | AgentTeams maintainer (final) |
| Stage 10 investigation findings seem incorrect | Daily-pipeline maintainer → Orchestrator agent author | Adversarial agent (peer review) | VK workspace lead (final) |
| Stage 10.1 adversarial critique conflicts with investigation | Orchestrator agent author → Adversarial agent author | Conflict-auditor | VK workspace lead (final) |
| Stage 11 remediation produces unexpected changes | VK workspace lead → Orchestrator agent author | Code-hygiene agent | VK workspace lead (final) |
| **Source-SHA detector output corrupts Stage 10 investigation input** | Daily-pipeline maintainer (detector owner) → VK workspace lead | Cross-stage review by orchestrator author | **VK workspace lead** |
| **Stage 10 depends on external detector inputs owned separately** | VK workspace lead | Designate liaison between daily-pipeline maintainer and orchestrator author | VK workspace lead (establishes interface) |
| Governance ambiguity or cross-agent conflicts | VK workspace lead → Conflict-auditor agent | Orchestrator agent | VK workspace lead (final) |

---

## Operational Procedures

### Pre-Run Checklist

Before running the orchestration script (full extended pipeline):

1. **Verify external script exists:** `ls -la "$PIPELINE_SCRIPT"` (executable)
2. **Verify daily-pipeline repo is up to date:** `cd "$REPO_ROOT" && git status` (clean or stashable)
3. **Verify VK_ROOT structure:** All collector repos have `.github/agents/orchestrator.agent.md`
4. **Verify build metadata:** All candidate repos have `.github/agents/_build-description.json` (if Stage 9.5 sync intended)
5. **Verify SSH/auth:** `gh auth status` (authenticated); SSH agent running (`ssh-add -l`)
6. **Verify Copilot CLI:** `"$COPILOT_BIN" --version` (working)

### Running the Pipeline

**Full run (Stages 1–11):**
```bash
"$PIPELINE_SCRIPT"
```

**Stages 1–8 only (skip VK extension):**
```bash
python3 -m daily_pipeline.cli --team tests/fixtures/team_a.json --team tests/fixtures/team_b.json --output-root tmp/daily-pipeline
```

**VK stages only (skip Stages 1–8):**
```bash
"$PIPELINE_SCRIPT" --vk-only
```

**Stage 9.5 sync only:**
```bash
"$PIPELINE_SCRIPT" --vk-sync-only
```

**Stage 9.5 sync only (Python CLI path — no external script required):**
```bash
python3 -m daily_pipeline.cli --sync --root "$VK_ROOT" --build-team-py "$BUILD_TEAM_PY"
```

**Stage 9.5 sync dry-run (discover targets; no subprocess invoked):**
```bash
python3 -m daily_pipeline.cli --sync --root "$VK_ROOT" --build-team-py "$BUILD_TEAM_PY" --dry-run
```

**Single stage re-run:**
```bash
"$PIPELINE_SCRIPT" --stage 10  # Re-run Stage 10
```

### Post-Run Review

After pipeline completes:

1. **Check final status:** Review `$LOG_DIR` logs (or your configured log directory)
2. **Review failed stages:** Inspect stage artifacts in `tmp/daily-pipeline/YYYY-MM-DD/`
3. **Review VK failures:** If `VK_FAILED` non-empty, check investigation reports in each repo's `.github/agents/outputs/`
4. **Review adversarial findings:** In Stage 10.1 reports, check `## Stage 10.1 Adversarial Review` sections
5. **Validate git state:** Ensure all expected commits were pushed; check GitHub branch history

### Troubleshooting

| **Symptom** | **Likely Cause** | **Remediation** |
|------------|------------------|-----------------|
| Stage 9.5 sync fails on repo X | Invalid `_build-description.json` in repo X | Validate JSON syntax; check build metadata fields |
| Stage 10 times out (15+ minutes) | Orchestrator agent loop or slow API | Check Copilot CLI logs; reduce investigation scope if needed |
| Stage 10.1 findings contradict Stage 10 | Adversarial methodology mismatch | Review 6-step Critique Protocol prompt; adjust if needed |
| Stage 11 remediation fails on repo Y | Orchestrator agent action failed | Check `.github/agents/outputs/investigation-report-*.md` instructions; validate repo state before manual application |
| VK_FAILED repos not committed/pushed | Git credentials expired or auth failed | Verify `gh auth status`; re-run Stage 11 with `--vk-remediate-only` after fixing auth |

---

## Cron Integration

If deployed, the external orchestration script can be registered as a LaunchAgent on macOS and scheduled for daily execution.

**Location (example):** `~/Library/LaunchAgents/com.example.daily-pipeline.plist`

**Typical schedule window (example):** morning run (full pipeline runtime, including Stages 1–8 + 9 + 9.5–11)

**Log output:** Configured in orchestration script (example default: `~/logs/daily-pipeline/`)

### Notes on Scheduled Execution

- stdin redirected from `/dev/null` to prevent SIGTTIN signals in background mode
- SSH agent setup runs at pipeline start (requires passphrase if not in Keychain)
- Git pull --rebase before Stages 1–8 core execution (non-destructive; uses autostash on conflicts)
- VK stages (10–11) run after daily-pipeline commits are pushed (ensures latest state)

---

## Integration with Daily-Pipeline Repository

The daily-pipeline repository (Stages 1–8) is **self-contained**:
- All stage logic in `daily_pipeline/protocol.py`
- No runtime dependency on external orchestration scripts
- Can run independently via `python3 -m daily_pipeline.cli --team tests/fixtures/team_a.json --team tests/fixtures/team_b.json --dry-run`

The external script provides:
- **Orchestration timing:** Runs daily-pipeline at 09:00, then VK stages after completion
- **Change detection:** Caches source SHAs; enables short-circuit on unchanged inputs
- **Retry logic:** Core scripted stage retries apply to the pre-VK script stage set; VK stages use per-stage failure handling described in this runbook
- **Logging/reporting:** Centralized log aggregation across all 11 stages

This separation ensures:
- Daily-pipeline can evolve independently without breaking external orchestration
- External script can be updated without modifying daily-pipeline code
- Both remain testable in isolation and when integrated

---

## Maintenance and Updates

### When to Regenerate Agent Team (Stage 9.5)

- After updates to `daily_pipeline/` module structure
- After updates to `_build-description.json` (quality criteria, authority hierarchy)
- After AgentTeams toolchain major version upgrades
- Quarterly baseline sync (ensure no drift accumulation)

### When to Re-run Investigation (Stage 10)

- Weekly or when upstream sources change (external source-SHA detector identifies changes)
- After major changes to orchestrator agent prompts
- When consistency findings seem stale (>7 days old)

### When to Update Operational Docs

- After governance model changes (new agents, role shifts)
- After significant protocol changes (new stages, execution order changes)
- After discoveries of new presuppositions or risks (from adversarial reviews)
- Quarterly documentation health audit (check for stale content)

---

## Key Design Decisions

1. **Sequential core stages and staged VK orchestration:** Core Stages 1–8 are sequential in package implementation; Stage 11 Phase B is parallelized while Phase D remains sequential for git safety.

2. **Stage 10.1 as advisory (non-halting):** Allows adversarial findings to be logged without blocking remediation; operators can review findings post-run.

3. **Stage 9.5 deterministic sync before AI investigation:** Ensures baseline structural alignment before Stage 10 makes capability assumptions.

4. **Parallel Phase B + sequential Phase D in Stage 11:** Balances speed (parallel Copilot CLI calls) with git integrity (sequential commits/pushes).

5. **No runtime dependency on external scripts:** Daily-pipeline remains independently testable; external script is orchestration convenience, not requirement.

6. **Authority hierarchy preserved in all stages:** Package Source > Protocols > Configs > Tests; allows reproducible regeneration and conflict resolution.

---

## Related Documents

- [protocols/stages.md](protocols/stages.md) — Complete stage specifications (Stages 1–11)
- [HANDOFF-PLAN.md](HANDOFF-PLAN.md) — Agent team handoff and operational readiness
- [.github/agents/AGENT-TEAM-OPERATIONS.md](.github/agents/AGENT-TEAM-OPERATIONS.md) — Daily-pipeline agent team maintenance runbook
- [.github/copilot-instructions.md](.github/copilot-instructions.md) — Constitutional rules and governance model for all agents
- `~/.local/bin/daily-pipeline.sh` (example) — External orchestration script reference for stage ordering
