# Daily Pipeline Stage Contracts

This repository uses a two-layer stage model:
- Core protocol (implemented): stages 1-8 in daily_pipeline/protocol.py
- Orchestration extension (external): stages 9, 9.5, 10, 10.1, 10.5, 11 managed by an external orchestration script (for example `~/.local/bin/daily-pipeline.sh`)

## Core Protocol (Stages 1-8)

Authoritative source: daily_pipeline/protocol.py

### Stage 1 - validate-selection
- Input: selected team file paths
- Action: load teams and capture team_count/team_names
- Output: 01-validate-selection.json
- Failure behavior: loader-level failures stop protocol execution

### Stage 2 - refresh-sources
- Input: framework availability matrix
- Action: compute degraded mode using framework status values
- Output: 02-refresh-sources.json
- Failure behavior:
  - If degraded_mode=true and allow_degraded=false, stage status becomes blocked and protocol exits early with consolidated report
  - Otherwise protocol proceeds

### Stage 3 - ingest-normalize
- Input: loaded teams from stage 1
- Action: normalize team structures for analysis
- Output: 03-ingest-normalize.json
- Failure behavior: analysis failures stop protocol execution

### Stage 4 - commonality-analysis
- Input: normalized teams and configured thresholds
- Action: compute shared capabilities and shared references
- Output: 04-commonality-analysis.json
- Failure behavior: analysis failures stop protocol execution

### Stage 5 - synthesize-abstract-team
- Input: normalized teams, shared capabilities, shared references
- Action: synthesize abstract-agent-team model with mapping and provenance
- Output: 05-synthesize-abstract-team.json
- Failure behavior: synthesis failures stop protocol execution

### Stage 6 - build-agentteams-integration
- Input: abstract team plus trigger/target/confidence settings
- Action: build and write integration request payload
- Output:
  - 06-build-agentteams-integration.json
  - integration_requests/agentteams-request-*.json
- Failure behavior: integration build/write failures stop protocol execution

### Stage 7 - stage-registry
- Input: prior stage results and degraded mode flag
- Action: emit machine-readable protocol registry
- Output: 07-stage-registry.json
- Failure behavior: registry serialization failures stop protocol execution

### Stage 8 - consolidated-report
- Input: run context and cumulative stage results
- Action: write markdown run summary
- Output:
  - 08-consolidated-report.json
  - daily-pipeline-YYYY-MM-DD.report.md
- Failure behavior: reporting failures stop protocol execution
- Conditional guarantee: stage 8 outputs exist only when execution reaches stage 8; in early-exit mode (blocked at stage 2 with allow_degraded=false), a consolidated report is still written but stage 8 artifact files are not emitted

## Orchestration Extension (External Stages)

Operational reference source: external orchestration script (for example `~/.local/bin/daily-pipeline.sh`)

### Stage 9 - pipeline-orchestration
- Role: external handoff/orchestration stage after core stage 8
- Action: coordinates completion status, retries, and transition to workspace-level stages
- Notes: not implemented inside daily_pipeline/protocol.py

### Stage 9.5 - agentteams-deterministic-sync
- Input: VK_ROOT repos containing .github/agents/_build-description.json
- Action: run build_team.py --update --merge --yes for each candidate repo
- Validation: checks orchestrator.agent.md contains Plan Documentation and Review (Workflow 10) and Final Check (Workflow 11)
- Failure behavior: best-effort, non-halting
- Python helpers: daily_pipeline/integration/sync.py exposes discover_sync_targets() and execute_agentteams_sync() for external orchestration use; these are callable helpers only — Stage 9.5 execution is external orchestration, not part of daily_pipeline/protocol.py
- CLI path: python3 -m daily_pipeline.cli --sync --root $VK_ROOT --build-team-py $BUILD_TEAM_PY

### Stage 10 - vk-investigation
- Input: eligible collector repos (with orchestrator agent)
- Action: run orchestrator investigation in each repo and write investigation report
- Output: .github/agents/outputs/investigation-report-YYYY-MM-DD.md
- Failure behavior: per-repo failures logged; pipeline continues

### Stage 10.1 - vk-adversarial-review
- Input: stage 10 investigation report and adversarial agent
- Action: challenge presuppositions and append review section to report
- Output: report section titled Stage 10.1 Adversarial Review
- Failure behavior: advisory only, non-halting

### Stage 10.5 - vk-source-updates
- Input: source SHA cache and source repo state
- Action: run source-aware updates for abstract definitions and downstream payloads
- Output: updated SHA cache and update artifacts
- Temporal rule: updates are prospective for stage 11 inputs, not retroactive edits to stage 8 findings
- Failure behavior: best-effort, non-halting

### Stage 11 - vk-remediation
- Input: stage 10 report (+ stage 10.1 and 10.5 context when available)
- Action:
  - Phase A: eligibility and agent resolvability checks
  - Phase B: parallel per-repo remediation execution
  - Phase C: collect success/failure markers
  - Phase D: sequential git commit/push safety phase
- Failure behavior: failed repos tracked in VK_FAILED; final exit is non-zero when failures remain

## Guardrails

- Runtime boundary:
  - daily_pipeline/protocol.py does not depend on scripts under ~/.local/bin
  - orchestration extension is external and optional for core protocol runs
  - daily_pipeline/integration/sync.py may invoke build_team.py as a subprocess using sys.executable; this is not a ~/.local/bin dependency
- Provenance:
  - shared capability/reference outputs must retain team/source traceability
- Degraded mode:
  - supported in core stage 2 behavior when allow_degraded=true
- Portability:
  - paths to local orchestration scripts are environment-specific examples; use local environment variables and workspace-relative paths where possible
- Consistency source of truth:
  - core stage semantics are governed by package source in daily_pipeline/
  - orchestration extension semantics are governed by repository protocol docs and validated operational runbooks; external scripts are non-authoritative execution references

## Related Documentation

- protocols/stages.csv
- EXTENDED-PIPELINE-OPERATIONS.md
- HANDOFF-PLAN.md
- .github/agents/AGENT-TEAM-OPERATIONS.md
- daily_pipeline/integration/sync.py
