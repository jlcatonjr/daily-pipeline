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

# MusicMaker — Copilot Instructions

> This file defines the conventions, authority hierarchy, and agent team structure for all GitHub Copilot agents in MusicMaker.

---

<!-- AGENTTEAMS:BEGIN project_overview v=1 -->
## Project Overview

**Name:** MusicMaker
**Goal:** Restructure and maintain a browser-based musical composition application that supports grand-staff notation editing, MIDI keyboard input and output, multi-instrument synthesis, real-time audio playback, and score file save/load. The restructuring goal is to migrate from a monolithic global-variable architecture (~5,900 lines across 9 unmodularised JS files loaded via script tags) to a maintainable ES-module codebase bundled by a Node.js build pipeline, with Node.js also providing the security layer (dependency locking, JSON schema validation, Content-Security-Policy headers, and ESLint security ruleset). The resulting application must preserve all existing interactive behaviour while establishing a sound foundation for ongoing feature development.
**Deliverable type:** ES module JavaScript source files, Vite build configuration and package.json, JSON score schema (AJV-validated), Node.js dev-server with security headers, Jest test suite and Refactored HTML entry point
**Output format:** Browser JavaScript application (ES modules, Vite-bundled)
<!-- AGENTTEAMS:END project_overview -->

---

<!-- AGENTTEAMS:BEGIN directory_structure v=1 -->
## Directory Structure

| Path | Purpose |
|------|---------|
| `src/` | Primary authored deliverables |
| `dist/` | Compiled/converted output artifacts |
| `docs/figures/` | Diagrams and figures |
| `docs/reference-db.md` | Reference/bibliography database |
| `.github/agents/` | Agent definition files |
| `.github/agents/references/` | Shared reference data |
<!-- AGENTTEAMS:END directory_structure -->

---

<!-- AGENTTEAMS:BEGIN output_conventions v=1 -->
## Output Conventions

- All primary deliverables are authored in `src/` as `ES module JavaScript source files, Vite build configuration and package.json, JSON score schema (AJV-validated), Node.js dev-server with security headers, Jest test suite and Refactored HTML entry point`
- Compiled output lives in `dist/` and is **never edited directly**
- Figures are generated from source files in `docs/figures/` — source files are authoritative
- Every deliverable must correspond to a Component Spec defined by a workstream expert
- Work summaries are authored in `workSummaries/` from canonical `tmp/by-week/` plan artifacts, legacy `tmp/` fallbacks, and git history
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
- `@work-summarizer` — synthesizes daily/weekly/monthly work summaries from plan artifacts and git history
- `@primary-producer` — drafts and revises primary deliverables
- `@quality-auditor` — read-only structural and prose quality audit
- `@style-guardian` — enforces voice and style fidelity
- `@technical-validator` — verifies technical accuracy against authority sources
- `@format-converter` — converts deliverables to final output format
- `@output-compiler` — assembles components into the final deliverable package
- `@tool-doc-researcher` — specialized domain agent

### Workstream Experts
- `@audio-engine-expert` — Audio Engine
- `@data-model-expert` — Data Model and Score I/O
- `@drag-reorder-expert` — Staff System Drag-and-Drop Reorder
- `@interactions-expert` — Interactions and Editing
- `@midi-engine-expert` — MIDI Engine
- `@music-notation-expert` — Music Notation
- `@node-build-security-expert` — Node.js Build Pipeline and Security Layer
- `@notation-renderer-expert` — Notation Renderer
- `@playback-engine-expert` — Playback Engine
- `@test-suite-expert` — Test Suite
- `@ui-controls-expert` — UI Controls and Event Listeners
<!-- AGENTTEAMS:END agent_team -->

---

<!-- AGENTTEAMS:BEGIN authority_hierarchy v=1 -->
## Authority Hierarchy

1. **Project source files** — ground truth for all technical claims
<!-- AGENTTEAMS:END authority_hierarchy -->

---

## Constitutional Rules

1. **Security first** — destructive operations require `@security` clearance
2. **Code hygiene second** — code changes require `@code-hygiene` audit before merge
3. **Authority hierarchy is ground truth** — no agent may contradict a higher-authority source
4. **Primary deliverables are the canonical output** — build artifacts are derived, never primary
5. **No fabricated references** — every citation must be verifiable in `docs/reference-db.md`
6. **Voice fidelity** — style governance rulings are authoritative when a style-governance agent is present
7. **Living documentation** — agent docs must not accumulate stale content
8. **Always close with `@conflict-auditor`** — required after any multi-file change session
9. **Every request must generate a plan** — any request involving two or more implementation steps (steps that write, create, rename, delete, or make agent decisions) must produce: (a) a summary saved to `tmp/by-week/YYYY-Www/<plan-slug>.plan.md` and (b) a step-by-step CSV saved to `tmp/by-week/YYYY-Www/<plan-slug>.steps.csv` before the first step executes; the CSV must include columns: `step`, `agent`, `action`, `inputs`, `outputs`, `status`, `notes`; initial `status` for all rows is `pending`; after each step completes, pass remaining steps through `@adversarial` and `@conflict-auditor` before proceeding; create the week folder if it does not exist and read legacy undated plans from `tmp/` when canonical week-organized storage is absent
10. **Completed plans must be captured in daily work summaries** — when a plan reaches all `done` during a session, invoke `@work-summarizer` to append/update `workSummaries/daily/YYYY-MM-DD.md` before closeout

---

<!-- AGENTTEAMS:BEGIN source_repositories v=1 -->
## Source Repositories

- Project source files (read-only)
<!-- AGENTTEAMS:END source_repositories -->

---

## Style Rules

No project-specific style rules defined.
