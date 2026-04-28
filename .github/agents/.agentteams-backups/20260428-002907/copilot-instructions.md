<!--
SECTION MANIFEST — copilot-instructions.template.md
| section_id            | designation   | notes                                    |
|-----------------------|---------------|------------------------------------------|
| project_overview      | FENCED        | Name, goal, deliverable type, output fmt |
| directory_structure   | FENCED        | Path/purpose table                       |
| output_conventions    | FENCED        | Authoring and build conventions          |
| agent_team            | FENCED        | Full agent team list                     |
| authority_hierarchy   | FENCED        | Source hierarchy list                    |
| source_repositories   | FENCED        | Authority source entries                 |
| constitutional_rules  | USER-EDITABLE | Project may extend or customise          |
| style_rules           | USER-EDITABLE | Project may extend or customise          |
-->

# daily-pipeline — Copilot Instructions

> This file defines the conventions, authority hierarchy, and agent team structure for all GitHub Copilot agents in daily-pipeline.

---

<!-- AGENTTEAMS:BEGIN project_overview v=1 -->
## Project Overview

**Name:** daily-pipeline
**Goal:** Build and run a standalone daily pipeline that ingests multiple agent teams, detects shared capabilities and references, synthesizes an abstract team, and prepares AgentTeams integration update requests for create/update workflows.
**Deliverable type:** Python modules, Protocol artifacts, Integration request payloads and Daily run reports
**Output format:** Python 3.11 modules
<!-- AGENTTEAMS:END project_overview -->

---

<!-- AGENTTEAMS:BEGIN directory_structure v=1 -->
## Directory Structure

| Path | Purpose |
|------|---------|
| `daily_pipeline/` | Primary authored deliverables |
| `tmp/daily-pipeline/` | Compiled/converted output artifacts |
| `docs/figures/` | Diagrams and figures |
| `.github/agents/references/reference-db.csv` | Reference/bibliography database |
| `.github/agents/` | Agent definition files |
| `.github/agents/references/` | Shared reference data |
<!-- AGENTTEAMS:END directory_structure -->

---

<!-- AGENTTEAMS:BEGIN output_conventions v=1 -->
## Output Conventions

- All primary deliverables are authored in `daily_pipeline/` as `Python modules, Protocol artifacts, Integration request payloads and Daily run reports`
- Compiled output lives in `tmp/daily-pipeline/` and is **never edited directly**
- Figures are generated from source files in `docs/figures/` — source files are authoritative
- Every deliverable must correspond to a Component Spec defined by a workstream expert
<!-- AGENTTEAMS:END output_conventions -->

---

<!-- AGENTTEAMS:BEGIN agent_team v=1 -->
## Agent Team

### Orchestrator
- `@orchestrator` — coordinates all agents; entry point for all user requests

### Governance Agents
- `@navigator` — project structure and file location
- `@security` — destructive operation clearance
- `@code-hygiene` — architecture enforcement and anti-sprawl auditor
- `@adversarial` — presupposition critic
- `@conflict-auditor` — consistency enforcement
- `@conflict-resolution` — ACCEPT/REJECT/REVISE decisions on flagged conflicts
- `@cleanup` — artifact removal
- `@agent-updater` — documentation synchronization
- `@agent-refactor` — spec compliance and reference extraction
- `@repo-liaison` — cross-repository impact tracking and coordination
- `@git-operations` — git/github operations and merge strategy workflow

### Domain Agents
- `@primary-producer` — drafts and revises primary deliverables
- `@quality-auditor` — read-only structural and prose quality audit
- `@technical-validator` — verifies technical accuracy against authority sources
- `@reference-manager` — manages the reference/bibliography database
- `@output-compiler` — assembles components into the final deliverable package
- `@tool-specific` — specialized domain agent

### Workstream Experts
- `@ingest-expert` — Team Ingestion
- `@analysis-expert` — Shared Capability and Reference Analysis
- `@abstraction-expert` — Abstract Team Synthesis
- `@integration-expert` — AgentTeams Integration
- `@reporting-expert` — Run Reporting
<!-- AGENTTEAMS:END agent_team -->

---

<!-- AGENTTEAMS:BEGIN authority_hierarchy v=1 -->
## Authority Hierarchy

1. **Package Source** (`daily_pipeline/`) — implementation behavior
2. **Protocol Definitions** (`protocols/`) — stage contracts and execution order
3. **Configuration Schemas** (`configs/`) — input validation and thresholds
4. **Test Suite** (`tests/`) — expected behavior and regressions
<!-- AGENTTEAMS:END authority_hierarchy -->

---

## Constitutional Rules

1. **Security first** — destructive operations require `@security` clearance
2. **Code hygiene second** — code changes require `@code-hygiene` audit before merge
3. **Authority hierarchy is ground truth** — no agent may contradict a higher-authority source
4. **Primary deliverables are the canonical output** — build artifacts are derived, never primary
5. **No fabricated references** — every citation must be verifiable in `.github/agents/references/reference-db.csv`
6. **Voice fidelity** — style governance rulings are authoritative when a style-governance agent is present
7. **Living documentation** — agent docs must not accumulate stale content
8. **Always close with `@conflict-auditor`** — required after any multi-file change session
9. **Every request must generate a plan** — any request involving two or more implementation steps (steps that write, create, rename, delete, or make agent decisions) must produce: (a) a summary saved to `tmp/<plan-slug>.plan.md` and (b) a step-by-step CSV saved to `tmp/<plan-slug>.steps.csv` before the first step executes; the CSV must include columns: `step`, `agent`, `action`, `inputs`, `outputs`, `status`, `notes`; initial `status` for all rows is `pending`; after each step completes, pass remaining steps through `@adversarial` and `@conflict-auditor` before proceeding; create `tmp/` if it does not exist

---

<!-- AGENTTEAMS:BEGIN source_repositories v=1 -->
## Source Repositories

- `daily_pipeline/` — implementation behavior
- `protocols/` — stage contracts and execution order
- `configs/` — input validation and thresholds
- `tests/` — expected behavior and regressions
<!-- AGENTTEAMS:END source_repositories -->

---

## Style Rules

- Preserve deterministic stage ordering and auditable outputs.
- Never depend at runtime on external ~/.local/bin scripts.
- All integration payloads must preserve provenance metadata.
