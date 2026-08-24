<!-- AGENTTEAMS:BEGIN content v=1 -->
# daily-pipeline — Agent Team Topology

> **Auto-generated.** Regenerated on every `build_team.py` run.
> Do not edit manually — changes will be overwritten.

---

## Team Topology Graph

![daily-pipeline agent team topology](pipeline-graph.svg)

The handoff-only control-flow backbone (agents-list edges omitted):

![daily-pipeline handoff backbone](pipeline-handoffs.svg)

---

## Node Legend

| Colour | Agent Type |
| --- | --- |
| <svg width="12" height="12"><rect width="12" height="12" fill="#e8e8ff" stroke="#6666cc"/></svg> Blue-lavender | Governance |
| <svg width="12" height="12"><rect width="12" height="12" fill="#e8ffe8" stroke="#66aa66"/></svg> Green | Domain |
| <svg width="12" height="12"><rect width="12" height="12" fill="#fff8e8" stroke="#ccaa44"/></svg> Yellow | Workstream Expert |
| <svg width="12" height="12"><rect width="12" height="12" fill="#ffe8e8" stroke="#cc6666"/></svg> Red-pink | Tool Specialist |

---

## Agent Roster

| Agent | Type | User-Invokable | Tools |
| --- | --- | --- | --- |
| `abstraction-expert` | workstream_expert | No | read, search, agent |
| `adversarial` | governance | Yes | read, search |
| `agent-refactor` | governance | No | edit, search, agent |
| `agent-updater` | governance | No | edit, search, execute, agent |
| `analysis-expert` | workstream_expert | No | read, search, agent |
| `cleanup` | governance | No | edit, search, execute |
| `code-hygiene` | governance | No | read, search |
| `conflict-auditor` | governance | No | read, search |
| `conflict-resolution` | governance | No | edit, search, read |
| `content-enricher` | domain | Yes | read, edit, search |
| `git-operations` | governance | Yes | read, execute, search |
| `ingest-expert` | workstream_expert | No | read, search, agent |
| `integration-expert` | workstream_expert | No | read, search, agent |
| `navigator` | governance | No | read, search, execute |
| `orchestrator` | governance | Yes | read, edit, search, execute, todo, agent |
| `output-compiler` | domain | No | read, edit, execute |
| `primary-producer` | domain | No | read, edit, search |
| `quality-auditor` | domain | No | read, search |
| `reference-manager` | domain | No | read, edit, search |
| `repo-liaison` | governance | No | read, edit, search, execute, agent |
| `reporting-expert` | workstream_expert | No | read, search, agent |
| `security` | governance | No | read, search |
| `team-builder` | governance | Yes | read, edit, search, execute, todo |
| `technical-validator` | domain | No | read, search |
| `tool-python` | tool_specialist | No | read, edit, execute, search |
| `tool-specific` | tool_specialist | No | read, edit, execute, search |
| `work-summarizer` | domain | Yes | read, search, execute, edit, agent |

---

## Adjacency List

| Agent | Receives from | Hands off to |
| --- | --- | --- |
| `abstraction-expert` | — | `adversarial`, `primary-producer`, `reference-manager` |
| `adversarial` | `abstraction-expert`, `agent-updater`, `analysis-expert`, `ingest-expert`, `integration-expert`, `reporting-expert`, `work-summarizer` | — |
| `agent-refactor` | `agent-updater` | `conflict-auditor` |
| `agent-updater` | `conflict-auditor` | `adversarial`, `agent-refactor`, `conflict-auditor` |
| `analysis-expert` | — | `adversarial`, `primary-producer`, `reference-manager` |
| `cleanup` | — | — |
| `code-hygiene` | — | — |
| `conflict-auditor` | `agent-refactor`, `agent-updater`, `primary-producer`, `reference-manager`, `technical-validator`, `work-summarizer` | `agent-updater`, `conflict-resolution`, `technical-validator` |
| `conflict-resolution` | `conflict-auditor` | — |
| `content-enricher` | — | `primary-producer`, `technical-validator` |
| `git-operations` | — | — |
| `ingest-expert` | — | `adversarial`, `primary-producer`, `reference-manager` |
| `integration-expert` | — | `adversarial`, `primary-producer`, `reference-manager` |
| `navigator` | — | — |
| `orchestrator` | `tool-python`, `tool-specific` | — |
| `output-compiler` | — | `technical-validator` |
| `primary-producer` | `abstraction-expert`, `analysis-expert`, `content-enricher`, `ingest-expert`, `integration-expert`, `quality-auditor`, `reporting-expert`, `technical-validator` | `conflict-auditor`, `quality-auditor` |
| `quality-auditor` | `primary-producer` | `primary-producer` |
| `reference-manager` | `abstraction-expert`, `analysis-expert`, `ingest-expert`, `integration-expert`, `reporting-expert`, `technical-validator` | `conflict-auditor` |
| `repo-liaison` | — | — |
| `reporting-expert` | — | `adversarial`, `primary-producer`, `reference-manager` |
| `security` | `tool-python`, `tool-specific` | — |
| `team-builder` | — | — |
| `technical-validator` | `conflict-auditor`, `content-enricher`, `output-compiler`, `tool-python`, `tool-specific`, `work-summarizer` | `conflict-auditor`, `primary-producer`, `reference-manager` |
| `tool-python` | — | `orchestrator`, `security`, `technical-validator` |
| `tool-specific` | — | `orchestrator`, `security`, `technical-validator` |
| `work-summarizer` | — | `adversarial`, `conflict-auditor`, `technical-validator` |

---

## Diagram Source

<details>
<summary>Mermaid &amp; DOT source for the topology diagram above</summary>

```mermaid
flowchart LR
    classDef governance fill:#e8e8ff,stroke:#6666cc,color:#000
    classDef domain    fill:#e8ffe8,stroke:#66aa66,color:#000
    classDef workstream_expert fill:#fff8e8,stroke:#ccaa44,color:#000
    classDef tool_specialist   fill:#ffe8e8,stroke:#cc6666,color:#000
    classDef unknown   fill:#f5f5f5,stroke:#999,color:#000
    abstraction_expert["Abstract Team Synthesis Expert"]
    class abstraction_expert workstream_expert
    adversarial["Adversarial"]
    class adversarial governance
    agent_refactor["Agent Refactor"]
    class agent_refactor governance
    agent_updater["Agent Updater"]
    class agent_updater governance
    analysis_expert["Shared Capability and Reference Analysis Expert"]
    class analysis_expert workstream_expert
    cleanup["Cleanup"]
    class cleanup governance
    code_hygiene["Code Hygiene"]
    class code_hygiene governance
    conflict_auditor["Conflict Auditor"]
    class conflict_auditor governance
    conflict_resolution["Conflict Resolution"]
    class conflict_resolution governance
    content_enricher["Content Enricher"]
    class content_enricher domain
    git_operations["Git Operations"]
    class git_operations governance
    ingest_expert["Team Ingestion Expert"]
    class ingest_expert workstream_expert
    integration_expert["AgentTeams Integration Expert"]
    class integration_expert workstream_expert
    navigator["Navigator"]
    class navigator governance
    orchestrator["Orchestrator"]
    class orchestrator governance
    output_compiler["Output Compiler"]
    class output_compiler domain
    primary_producer["Primary Producer"]
    class primary_producer domain
    quality_auditor["Quality Auditor"]
    class quality_auditor domain
    reference_manager["Reference Manager"]
    class reference_manager domain
    repo_liaison["Repo Liaison"]
    class repo_liaison governance
    reporting_expert["Run Reporting Expert"]
    class reporting_expert workstream_expert
    security["Security"]
    class security governance
    team_builder["Team Builder"]
    class team_builder governance
    technical_validator["Technical Validator"]
    class technical_validator domain
    tool_python["Tool Specialist"]
    class tool_python tool_specialist
    tool_specific["Tool Specialist"]
    class tool_specific tool_specialist
    work_summarizer["Work Summarizer"]
    class work_summarizer domain
    abstraction_expert -.-> adversarial
    abstraction_expert -.-> primary_producer
    abstraction_expert -.-> reference_manager
    agent_refactor -.-> conflict_auditor
    agent_updater -.-> adversarial
    agent_updater -.-> agent_refactor
    agent_updater -.-> conflict_auditor
    analysis_expert -.-> adversarial
    analysis_expert -.-> primary_producer
    analysis_expert -.-> reference_manager
    conflict_auditor -.-> agent_updater
    conflict_auditor -.-> conflict_resolution
    conflict_auditor -.-> technical_validator
    content_enricher -.-> primary_producer
    content_enricher -.-> technical_validator
    ingest_expert -.-> adversarial
    ingest_expert -.-> primary_producer
    ingest_expert -.-> reference_manager
    integration_expert -.-> adversarial
    integration_expert -.-> primary_producer
    integration_expert -.-> reference_manager
    output_compiler -.-> technical_validator
    primary_producer -.-> conflict_auditor
    primary_producer -.-> quality_auditor
    quality_auditor -.-> primary_producer
    reference_manager -.-> conflict_auditor
    reporting_expert -.-> adversarial
    reporting_expert -.-> primary_producer
    reporting_expert -.-> reference_manager
    technical_validator -.-> conflict_auditor
    technical_validator -.-> primary_producer
    technical_validator -.-> reference_manager
    tool_python -->|"Return to Orchestrator"| orchestrator
    tool_python -->|"Security Clearance for Config Change"| security
    tool_python -->|"Validate Tool Output"| technical_validator
    tool_python -.-> security
    tool_python -.-> technical_validator
    tool_specific -->|"Return to Orchestrator"| orchestrator
    tool_specific -->|"Security Clearance for Config Change"| security
    tool_specific -->|"Validate Tool Output"| technical_validator
    tool_specific -.-> security
    tool_specific -.-> technical_validator
    work_summarizer -.-> adversarial
    work_summarizer -.-> conflict_auditor
    work_summarizer -.-> technical_validator
```

```dot
digraph "daily-pipeline Agent Team" {
    rankdir=LR;
    node [fontname="Helvetica", fontsize=11, shape=box, style="rounded,filled"];
    edge [fontsize=9];
    "abstraction-expert" [label="Abstract Team Synthesis Expert", fillcolor="#fff8e8"];
    "adversarial" [label="Adversarial", fillcolor="#e8e8ff"];
    "agent-refactor" [label="Agent Refactor", fillcolor="#e8e8ff"];
    "agent-updater" [label="Agent Updater", fillcolor="#e8e8ff"];
    "analysis-expert" [label="Shared Capability and Reference Analysis Expert", fillcolor="#fff8e8"];
    "cleanup" [label="Cleanup", fillcolor="#e8e8ff"];
    "code-hygiene" [label="Code Hygiene", fillcolor="#e8e8ff"];
    "conflict-auditor" [label="Conflict Auditor", fillcolor="#e8e8ff"];
    "conflict-resolution" [label="Conflict Resolution", fillcolor="#e8e8ff"];
    "content-enricher" [label="Content Enricher", fillcolor="#e8ffe8"];
    "git-operations" [label="Git Operations", fillcolor="#e8e8ff"];
    "ingest-expert" [label="Team Ingestion Expert", fillcolor="#fff8e8"];
    "integration-expert" [label="AgentTeams Integration Expert", fillcolor="#fff8e8"];
    "navigator" [label="Navigator", fillcolor="#e8e8ff"];
    "orchestrator" [label="Orchestrator", fillcolor="#e8e8ff"];
    "output-compiler" [label="Output Compiler", fillcolor="#e8ffe8"];
    "primary-producer" [label="Primary Producer", fillcolor="#e8ffe8"];
    "quality-auditor" [label="Quality Auditor", fillcolor="#e8ffe8"];
    "reference-manager" [label="Reference Manager", fillcolor="#e8ffe8"];
    "repo-liaison" [label="Repo Liaison", fillcolor="#e8e8ff"];
    "reporting-expert" [label="Run Reporting Expert", fillcolor="#fff8e8"];
    "security" [label="Security", fillcolor="#e8e8ff"];
    "team-builder" [label="Team Builder", fillcolor="#e8e8ff"];
    "technical-validator" [label="Technical Validator", fillcolor="#e8ffe8"];
    "tool-python" [label="Tool Specialist", fillcolor="#ffe8e8"];
    "tool-specific" [label="Tool Specialist", fillcolor="#ffe8e8"];
    "work-summarizer" [label="Work Summarizer", fillcolor="#e8ffe8"];
    "abstraction-expert" -> "adversarial" [style=dashed];
    "abstraction-expert" -> "primary-producer" [style=dashed];
    "abstraction-expert" -> "reference-manager" [style=dashed];
    "agent-refactor" -> "conflict-auditor" [style=dashed];
    "agent-updater" -> "adversarial" [style=dashed];
    "agent-updater" -> "agent-refactor" [style=dashed];
    "agent-updater" -> "conflict-auditor" [style=dashed];
    "analysis-expert" -> "adversarial" [style=dashed];
    "analysis-expert" -> "primary-producer" [style=dashed];
    "analysis-expert" -> "reference-manager" [style=dashed];
    "conflict-auditor" -> "agent-updater" [style=dashed];
    "conflict-auditor" -> "conflict-resolution" [style=dashed];
    "conflict-auditor" -> "technical-validator" [style=dashed];
    "content-enricher" -> "primary-producer" [style=dashed];
    "content-enricher" -> "technical-validator" [style=dashed];
    "ingest-expert" -> "adversarial" [style=dashed];
    "ingest-expert" -> "primary-producer" [style=dashed];
    "ingest-expert" -> "reference-manager" [style=dashed];
    "integration-expert" -> "adversarial" [style=dashed];
    "integration-expert" -> "primary-producer" [style=dashed];
    "integration-expert" -> "reference-manager" [style=dashed];
    "output-compiler" -> "technical-validator" [style=dashed];
    "primary-producer" -> "conflict-auditor" [style=dashed];
    "primary-producer" -> "quality-auditor" [style=dashed];
    "quality-auditor" -> "primary-producer" [style=dashed];
    "reference-manager" -> "conflict-auditor" [style=dashed];
    "reporting-expert" -> "adversarial" [style=dashed];
    "reporting-expert" -> "primary-producer" [style=dashed];
    "reporting-expert" -> "reference-manager" [style=dashed];
    "technical-validator" -> "conflict-auditor" [style=dashed];
    "technical-validator" -> "primary-producer" [style=dashed];
    "technical-validator" -> "reference-manager" [style=dashed];
    "tool-python" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-python" -> "security" [style=solid, label="Security Clearance for Config Change"];
    "tool-python" -> "technical-validator" [style=solid, label="Validate Tool Output"];
    "tool-specific" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-specific" -> "security" [style=solid, label="Security Clearance for Config Change"];
    "tool-specific" -> "technical-validator" [style=solid, label="Validate Tool Output"];
    "work-summarizer" -> "adversarial" [style=dashed];
    "work-summarizer" -> "conflict-auditor" [style=dashed];
    "work-summarizer" -> "technical-validator" [style=dashed];
}
```

</details>

---

## JSON Adjacency

```json
{
  "project_name": "daily-pipeline",
  "nodes": {
    "abstraction-expert": {
      "display_name": "Abstract Team Synthesis Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "adversarial": {
      "display_name": "Adversarial",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "search"
      ]
    },
    "agent-refactor": {
      "display_name": "Agent Refactor",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "agent"
      ]
    },
    "agent-updater": {
      "display_name": "Agent Updater",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "execute",
        "agent"
      ]
    },
    "analysis-expert": {
      "display_name": "Shared Capability and Reference Analysis Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "cleanup": {
      "display_name": "Cleanup",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "execute"
      ]
    },
    "code-hygiene": {
      "display_name": "Code Hygiene",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "conflict-auditor": {
      "display_name": "Conflict Auditor",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "conflict-resolution": {
      "display_name": "Conflict Resolution",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "edit",
        "search",
        "read"
      ]
    },
    "content-enricher": {
      "display_name": "Content Enricher",
      "agent_type": "domain",
      "user_invokable": true,
      "tools": [
        "read",
        "edit",
        "search"
      ]
    },
    "git-operations": {
      "display_name": "Git Operations",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "execute",
        "search"
      ]
    },
    "ingest-expert": {
      "display_name": "Team Ingestion Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "integration-expert": {
      "display_name": "AgentTeams Integration Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "navigator": {
      "display_name": "Navigator",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "execute"
      ]
    },
    "orchestrator": {
      "display_name": "Orchestrator",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "edit",
        "search",
        "execute",
        "todo",
        "agent"
      ]
    },
    "output-compiler": {
      "display_name": "Output Compiler",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute"
      ]
    },
    "primary-producer": {
      "display_name": "Primary Producer",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "search"
      ]
    },
    "quality-auditor": {
      "display_name": "Quality Auditor",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "reference-manager": {
      "display_name": "Reference Manager",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "search"
      ]
    },
    "repo-liaison": {
      "display_name": "Repo Liaison",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "search",
        "execute",
        "agent"
      ]
    },
    "reporting-expert": {
      "display_name": "Run Reporting Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "security": {
      "display_name": "Security",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "team-builder": {
      "display_name": "Team Builder",
      "agent_type": "governance",
      "user_invokable": true,
      "tools": [
        "read",
        "edit",
        "search",
        "execute",
        "todo"
      ]
    },
    "technical-validator": {
      "display_name": "Technical Validator",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "tool-python": {
      "display_name": "Tool Specialist",
      "agent_type": "tool_specialist",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute",
        "search"
      ]
    },
    "tool-specific": {
      "display_name": "Tool Specialist",
      "agent_type": "tool_specialist",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute",
        "search"
      ]
    },
    "work-summarizer": {
      "display_name": "Work Summarizer",
      "agent_type": "domain",
      "user_invokable": true,
      "tools": [
        "read",
        "search",
        "execute",
        "edit",
        "agent"
      ]
    }
  },
  "edges": [
    {
      "source": "abstraction-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "abstraction-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "abstraction-expert",
      "target": "reference-manager",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-refactor",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-updater",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-updater",
      "target": "agent-refactor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-updater",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "analysis-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "analysis-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "analysis-expert",
      "target": "reference-manager",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "conflict-auditor",
      "target": "agent-updater",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "conflict-auditor",
      "target": "conflict-resolution",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "conflict-auditor",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "content-enricher",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "content-enricher",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ingest-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ingest-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ingest-expert",
      "target": "reference-manager",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "integration-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "integration-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "integration-expert",
      "target": "reference-manager",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "output-compiler",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "primary-producer",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "primary-producer",
      "target": "quality-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "quality-auditor",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "reference-manager",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "reporting-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "reporting-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "reporting-expert",
      "target": "reference-manager",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "technical-validator",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "technical-validator",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "technical-validator",
      "target": "reference-manager",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-python",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-python",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance for Config Change"
    },
    {
      "source": "tool-python",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Tool Output"
    },
    {
      "source": "tool-python",
      "target": "security",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-python",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-specific",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-specific",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance for Config Change"
    },
    {
      "source": "tool-specific",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Tool Output"
    },
    {
      "source": "tool-specific",
      "target": "security",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-specific",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "work-summarizer",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "work-summarizer",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "work-summarizer",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    }
  ],
  "adjacency": {
    "abstraction-expert": [
      "adversarial",
      "primary-producer",
      "reference-manager"
    ],
    "adversarial": [],
    "agent-refactor": [
      "conflict-auditor"
    ],
    "agent-updater": [
      "adversarial",
      "agent-refactor",
      "conflict-auditor"
    ],
    "analysis-expert": [
      "adversarial",
      "primary-producer",
      "reference-manager"
    ],
    "cleanup": [],
    "code-hygiene": [],
    "conflict-auditor": [
      "agent-updater",
      "conflict-resolution",
      "technical-validator"
    ],
    "conflict-resolution": [],
    "content-enricher": [
      "primary-producer",
      "technical-validator"
    ],
    "git-operations": [],
    "ingest-expert": [
      "adversarial",
      "primary-producer",
      "reference-manager"
    ],
    "integration-expert": [
      "adversarial",
      "primary-producer",
      "reference-manager"
    ],
    "navigator": [],
    "orchestrator": [],
    "output-compiler": [
      "technical-validator"
    ],
    "primary-producer": [
      "conflict-auditor",
      "quality-auditor"
    ],
    "quality-auditor": [
      "primary-producer"
    ],
    "reference-manager": [
      "conflict-auditor"
    ],
    "repo-liaison": [],
    "reporting-expert": [
      "adversarial",
      "primary-producer",
      "reference-manager"
    ],
    "security": [],
    "team-builder": [],
    "technical-validator": [
      "conflict-auditor",
      "primary-producer",
      "reference-manager"
    ],
    "tool-python": [
      "orchestrator",
      "security",
      "technical-validator"
    ],
    "tool-specific": [
      "orchestrator",
      "security",
      "technical-validator"
    ],
    "work-summarizer": [
      "adversarial",
      "conflict-auditor",
      "technical-validator"
    ]
  }
}
```
<!-- AGENTTEAMS:END content -->
