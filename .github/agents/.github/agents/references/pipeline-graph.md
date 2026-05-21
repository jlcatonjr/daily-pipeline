<!-- AGENTTEAMS:BEGIN content v=1 -->
# MusicMaker — Agent Team Topology

> **Auto-generated.** Regenerated on every `build_team.py` run.
> Do not edit manually — changes will be overwritten.

---

## Team Topology Graph

```mermaid
flowchart LR
    classDef governance fill:#e8e8ff,stroke:#6666cc,color:#000
    classDef domain    fill:#e8ffe8,stroke:#66aa66,color:#000
    classDef expert    fill:#fff8e8,stroke:#ccaa44,color:#000
    classDef tool      fill:#ffe8e8,stroke:#cc6666,color:#000
    classDef unknown   fill:#f5f5f5,stroke:#999,color:#000
    adversarial["Adversarial"]
    class adversarial governance
    agent_refactor["Agent Refactor"]
    class agent_refactor governance
    agent_updater["Agent Updater"]
    class agent_updater governance
    audio_engine_expert["Audio Engine Expert"]
    class audio_engine_expert workstream_expert
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
    data_model_expert["Data Model and Score I/O Expert"]
    class data_model_expert workstream_expert
    drag_reorder_expert["Staff System Drag-and-Drop Reorder Expert"]
    class drag_reorder_expert workstream_expert
    format_converter["Format Converter"]
    class format_converter domain
    git_operations["Git Operations"]
    class git_operations governance
    interactions_expert["Interactions and Editing Expert"]
    class interactions_expert workstream_expert
    midi_engine_expert["MIDI Engine Expert"]
    class midi_engine_expert workstream_expert
    music_notation_expert["Music Notation Expert"]
    class music_notation_expert workstream_expert
    navigator["Navigator"]
    class navigator governance
    node_build_security_expert["Node.js Build Pipeline and Security Layer Expert"]
    class node_build_security_expert workstream_expert
    notation_renderer_expert["Notation Renderer Expert"]
    class notation_renderer_expert workstream_expert
    orchestrator["Orchestrator"]
    class orchestrator governance
    output_compiler["Output Compiler"]
    class output_compiler domain
    playback_engine_expert["Playback Engine Expert"]
    class playback_engine_expert workstream_expert
    primary_producer["Primary Producer"]
    class primary_producer domain
    quality_auditor["Quality Auditor"]
    class quality_auditor domain
    repo_liaison["Repo Liaison"]
    class repo_liaison governance
    security["Security"]
    class security governance
    style_guardian["Style Guardian"]
    class style_guardian domain
    team_builder["Team Builder"]
    class team_builder governance
    technical_validator["Technical Validator"]
    class technical_validator domain
    test_suite_expert["Test Suite Expert"]
    class test_suite_expert workstream_expert
    tool_doc_researcher["Tool Documentation Researcher"]
    class tool_doc_researcher tool_specialist
    tool_eslint["Tool Specialist"]
    class tool_eslint tool_specialist
    tool_nodejs["Build System Specialist"]
    class tool_nodejs tool_specialist
    tool_tonejs["Tool Specialist"]
    class tool_tonejs tool_specialist
    tool_vexflow["Tool Specialist"]
    class tool_vexflow tool_specialist
    tool_vite["Build System Specialist"]
    class tool_vite tool_specialist
    ui_controls_expert["UI Controls and Event Listeners Expert"]
    class ui_controls_expert workstream_expert
    work_summarizer["Work Summarizer"]
    class work_summarizer domain
    orchestrator -->|"Produce / Revise Deliverable"| primary_producer
    orchestrator -->|"Audit Quality"| quality_auditor
    orchestrator -->|"Enforce Style / Standards"| style_guardian
    orchestrator -->|"Validate Technical Accuracy"| technical_validator
    orchestrator -->|"Convert / Transform Output"| format_converter
    orchestrator -->|"Compile Final Output"| output_compiler
    orchestrator -->|"Navigate Project"| navigator
    orchestrator -->|"Security Review"| security
    orchestrator -->|"Code Hygiene Audit"| code_hygiene
    orchestrator -->|"Adversarial Review"| adversarial
    orchestrator -->|"Conflict Audit"| conflict_auditor
    orchestrator -->|"Resolve Conflicts"| conflict_resolution
    orchestrator -->|"Clean Up Artifacts"| cleanup
    orchestrator -->|"Update Agent Docs"| agent_updater
    orchestrator -->|"Refactor Agent Docs"| agent_refactor
    orchestrator -->|"Cross-Repository Liaison"| repo_liaison
    orchestrator -->|"Summarize Work Period"| work_summarizer
    orchestrator -->|"Git Operations"| git_operations
    navigator -->|"Return to Orchestrator"| orchestrator
    security -->|"Return to Orchestrator"| orchestrator
    code_hygiene -->|"Security Clearance (for Deletions)"| security
    code_hygiene -->|"Cleanup Agent"| cleanup
    code_hygiene -->|"Agent Refactor (Structural Violations)"| agent_refactor
    code_hygiene -->|"Log Conflict"| conflict_auditor
    code_hygiene -->|"Return to Orchestrator"| orchestrator
    adversarial -->|"Return to Orchestrator"| orchestrator
    adversarial -->|"Audit for Conflicts"| conflict_auditor
    conflict_auditor -->|"Return to Orchestrator"| orchestrator
    conflict_auditor -->|"Update Agent Docs"| agent_updater
    conflict_auditor -->|"Resolve Conflicts"| conflict_resolution
    conflict_auditor -->|"Verify Source Drift"| technical_validator
    conflict_auditor -.-> conflict_resolution
    conflict_auditor -.-> agent_updater
    conflict_auditor -.-> technical_validator
    conflict_resolution -->|"Return to Orchestrator"| orchestrator
    conflict_resolution -->|"Update Agent Docs"| agent_updater
    cleanup -->|"Return to Orchestrator"| orchestrator
    agent_updater -->|"Refactor Agent Docs"| agent_refactor
    agent_updater -->|"Run Adversarial Review"| adversarial
    agent_updater -->|"Run Conflict Audit"| conflict_auditor
    agent_updater -->|"Return to Orchestrator"| orchestrator
    agent_updater -.-> adversarial
    agent_updater -.-> conflict_auditor
    agent_updater -.-> agent_refactor
    agent_refactor -->|"Run Conflict Audit"| conflict_auditor
    agent_refactor -->|"Return to Orchestrator"| orchestrator
    agent_refactor -.-> conflict_auditor
    repo_liaison -->|"Return to Orchestrator"| orchestrator
    repo_liaison -->|"Security Review for Cross-Repo Write"| security
    repo_liaison -->|"Conflict Audit After Cross-Repo Change"| conflict_auditor
    git_operations -->|"Return to Orchestrator"| orchestrator
    git_operations -->|"Security Review"| security
    git_operations -->|"Conflict Resolution"| conflict_resolution
    git_operations -->|"Update Agent Docs"| agent_updater
    work_summarizer -->|"Verify Summary Accuracy"| technical_validator
    work_summarizer -->|"Run Adversarial Audit"| adversarial
    work_summarizer -->|"Run Conflict Audit"| conflict_auditor
    work_summarizer -->|"Return to Orchestrator"| orchestrator
    work_summarizer -.-> technical_validator
    work_summarizer -.-> adversarial
    work_summarizer -.-> conflict_auditor
    primary_producer -->|"Style Audit"| style_guardian
    primary_producer -->|"Quality Audit"| quality_auditor
    primary_producer -->|"Conflict Audit"| conflict_auditor
    primary_producer -->|"Return to Orchestrator"| orchestrator
    primary_producer -.-> style_guardian
    primary_producer -.-> quality_auditor
    primary_producer -.-> conflict_auditor
    quality_auditor -->|"Route Corrections to Primary Producer"| primary_producer
    quality_auditor -->|"Route Style Issues"| style_guardian
    quality_auditor -->|"Return to Orchestrator"| orchestrator
    quality_auditor -.-> primary_producer
    quality_auditor -.-> style_guardian
    style_guardian -->|"Route Style Corrections"| primary_producer
    style_guardian -->|"Return to Orchestrator"| orchestrator
    style_guardian -.-> primary_producer
    technical_validator -->|"Route Corrections to Primary Producer"| primary_producer
    technical_validator -->|"Log Conflict"| conflict_auditor
    technical_validator -->|"Return to Orchestrator"| orchestrator
    technical_validator -.-> primary_producer
    technical_validator -.-> conflict_auditor
    format_converter -->|"Pass to Output Compiler"| output_compiler
    format_converter -->|"Quality Check After Conversion"| quality_auditor
    format_converter -->|"Return to Orchestrator"| orchestrator
    format_converter -.-> output_compiler
    format_converter -.-> quality_auditor
    output_compiler -->|"Convert Missing Components"| format_converter
    output_compiler -->|"Validate Technical Accuracy"| technical_validator
    output_compiler -->|"Return to Orchestrator"| orchestrator
    output_compiler -.-> format_converter
    output_compiler -.-> technical_validator
    tool_doc_researcher -->|"Update Brief and Generated Docs"| agent_updater
    tool_doc_researcher -->|"Return to Orchestrator"| orchestrator
    tool_eslint -->|"Validate Tool Output"| technical_validator
    tool_eslint -->|"Security Clearance for Config Change"| security
    tool_eslint -->|"Return to Orchestrator"| orchestrator
    tool_eslint -.-> technical_validator
    tool_eslint -.-> security
    tool_nodejs -->|"Validate Build Output"| technical_validator
    tool_nodejs -->|"Security Clearance for Build Config Change"| security
    tool_nodejs -->|"Return to Orchestrator"| orchestrator
    tool_nodejs -.-> technical_validator
    tool_nodejs -.-> security
    tool_tonejs -->|"Validate Tool Output"| technical_validator
    tool_tonejs -->|"Security Clearance for Config Change"| security
    tool_tonejs -->|"Return to Orchestrator"| orchestrator
    tool_tonejs -.-> technical_validator
    tool_tonejs -.-> security
    tool_vexflow -->|"Validate Tool Output"| technical_validator
    tool_vexflow -->|"Security Clearance for Config Change"| security
    tool_vexflow -->|"Return to Orchestrator"| orchestrator
    tool_vexflow -.-> technical_validator
    tool_vexflow -.-> security
    tool_vite -->|"Validate Build Output"| technical_validator
    tool_vite -->|"Security Clearance for Build Config Change"| security
    tool_vite -->|"Return to Orchestrator"| orchestrator
    tool_vite -.-> technical_validator
    tool_vite -.-> security
    audio_engine_expert -->|"Vet Brief Before Drafting"| adversarial
    audio_engine_expert -->|"Send to Primary Producer"| primary_producer
    audio_engine_expert -->|"Return to Orchestrator"| orchestrator
    audio_engine_expert -.-> primary_producer
    audio_engine_expert -.-> adversarial
    data_model_expert -->|"Vet Brief Before Drafting"| adversarial
    data_model_expert -->|"Send to Primary Producer"| primary_producer
    data_model_expert -->|"Return to Orchestrator"| orchestrator
    data_model_expert -.-> primary_producer
    data_model_expert -.-> adversarial
    drag_reorder_expert -->|"Vet Brief Before Drafting"| adversarial
    drag_reorder_expert -->|"Send to Primary Producer"| primary_producer
    drag_reorder_expert -->|"Return to Orchestrator"| orchestrator
    drag_reorder_expert -.-> primary_producer
    drag_reorder_expert -.-> adversarial
    interactions_expert -->|"Vet Brief Before Drafting"| adversarial
    interactions_expert -->|"Send to Primary Producer"| primary_producer
    interactions_expert -->|"Return to Orchestrator"| orchestrator
    interactions_expert -.-> primary_producer
    interactions_expert -.-> adversarial
    midi_engine_expert -->|"Vet Brief Before Drafting"| adversarial
    midi_engine_expert -->|"Send to Primary Producer"| primary_producer
    midi_engine_expert -->|"Return to Orchestrator"| orchestrator
    midi_engine_expert -.-> primary_producer
    midi_engine_expert -.-> adversarial
    music_notation_expert -->|"Vet Brief Before Drafting"| adversarial
    music_notation_expert -->|"Send to Primary Producer"| primary_producer
    music_notation_expert -->|"Return to Orchestrator"| orchestrator
    music_notation_expert -.-> primary_producer
    music_notation_expert -.-> adversarial
    node_build_security_expert -->|"Vet Brief Before Drafting"| adversarial
    node_build_security_expert -->|"Send to Primary Producer"| primary_producer
    node_build_security_expert -->|"Return to Orchestrator"| orchestrator
    node_build_security_expert -.-> primary_producer
    node_build_security_expert -.-> adversarial
    notation_renderer_expert -->|"Vet Brief Before Drafting"| adversarial
    notation_renderer_expert -->|"Send to Primary Producer"| primary_producer
    notation_renderer_expert -->|"Return to Orchestrator"| orchestrator
    notation_renderer_expert -.-> primary_producer
    notation_renderer_expert -.-> adversarial
    playback_engine_expert -->|"Vet Brief Before Drafting"| adversarial
    playback_engine_expert -->|"Send to Primary Producer"| primary_producer
    playback_engine_expert -->|"Return to Orchestrator"| orchestrator
    playback_engine_expert -.-> primary_producer
    playback_engine_expert -.-> adversarial
    test_suite_expert -->|"Vet Brief Before Drafting"| adversarial
    test_suite_expert -->|"Send to Primary Producer"| primary_producer
    test_suite_expert -->|"Return to Orchestrator"| orchestrator
    test_suite_expert -.-> primary_producer
    test_suite_expert -.-> adversarial
    ui_controls_expert -->|"Vet Brief Before Drafting"| adversarial
    ui_controls_expert -->|"Send to Primary Producer"| primary_producer
    ui_controls_expert -->|"Return to Orchestrator"| orchestrator
    ui_controls_expert -.-> primary_producer
    ui_controls_expert -.-> adversarial
    content_enricher -->|"Validate Enriched Content"| technical_validator
    content_enricher -->|"Return to Orchestrator"| orchestrator
    content_enricher -.-> primary_producer
    content_enricher -.-> technical_validator
```

---

## Node Legend

| Colour | Agent Type |
| --- | --- |
| ![governance](https://via.placeholder.com/12/e8e8ff/e8e8ff) Blue | Governance |
| ![domain](https://via.placeholder.com/12/e8ffe8/e8ffe8) Green | Domain |
| ![expert](https://via.placeholder.com/12/fff8e8/fff8e8) Yellow | Workstream Expert |
| ![tool](https://via.placeholder.com/12/ffe8e8/ffe8e8) Red | Tool Specialist |

---

## Agent Roster

| Agent | Type | User-Invokable | Tools |
| --- | --- | --- | --- |
| `adversarial` | governance | Yes | read, search |
| `agent-refactor` | governance | No | edit, search, agent |
| `agent-updater` | governance | No | edit, search, execute, agent |
| `audio-engine-expert` | workstream_expert | No | read, search, agent |
| `cleanup` | governance | No | edit, search, execute |
| `code-hygiene` | governance | No | read, search |
| `conflict-auditor` | governance | No | read, edit, search, execute |
| `conflict-resolution` | governance | No | edit, search, read |
| `content-enricher` | domain | Yes | read, edit, search |
| `data-model-expert` | workstream_expert | No | read, search, agent |
| `drag-reorder-expert` | workstream_expert | No | read, search, agent |
| `format-converter` | domain | No | read, edit, execute |
| `git-operations` | governance | Yes | read, execute, search |
| `interactions-expert` | workstream_expert | No | read, search, agent |
| `midi-engine-expert` | workstream_expert | No | read, search, agent |
| `music-notation-expert` | workstream_expert | No | read, search, agent |
| `navigator` | governance | No | read, search, execute |
| `node-build-security-expert` | workstream_expert | No | read, search, agent |
| `notation-renderer-expert` | workstream_expert | No | read, search, agent |
| `orchestrator` | governance | Yes | read, edit, search, execute, todo, agent |
| `output-compiler` | domain | No | read, edit, execute |
| `playback-engine-expert` | workstream_expert | No | read, search, agent |
| `primary-producer` | domain | No | read, edit, search |
| `quality-auditor` | domain | No | read, search |
| `repo-liaison` | governance | No | read, edit, search, execute, agent |
| `security` | governance | No | read, search |
| `style-guardian` | domain | No | read, edit, search |
| `team-builder` | governance | Yes | read, edit, search, execute, todo |
| `technical-validator` | domain | No | read, search |
| `test-suite-expert` | workstream_expert | No | read, search, agent |
| `tool-doc-researcher` | tool_specialist | No | read, search |
| `tool-eslint` | tool_specialist | No | read, edit, execute, search |
| `tool-nodejs` | tool_specialist | No | read, edit, execute, search |
| `tool-tonejs` | tool_specialist | No | read, edit, execute, search |
| `tool-vexflow` | tool_specialist | No | read, edit, execute, search |
| `tool-vite` | tool_specialist | No | read, edit, execute, search |
| `ui-controls-expert` | workstream_expert | No | read, search, agent |
| `work-summarizer` | domain | Yes | read, search, execute, edit, agent |

---

## Adjacency List

| Agent | Receives from | Hands off to |
| --- | --- | --- |
| `adversarial` | `agent-updater`, `audio-engine-expert`, `data-model-expert`, `drag-reorder-expert`, `interactions-expert`, `midi-engine-expert`, `music-notation-expert`, `node-build-security-expert`, `notation-renderer-expert`, `orchestrator`, `playback-engine-expert`, `test-suite-expert`, `ui-controls-expert`, `work-summarizer` | `conflict-auditor`, `orchestrator` |
| `agent-refactor` | `agent-updater`, `code-hygiene`, `orchestrator` | `conflict-auditor`, `orchestrator` |
| `agent-updater` | `conflict-auditor`, `conflict-resolution`, `git-operations`, `orchestrator`, `tool-doc-researcher` | `adversarial`, `agent-refactor`, `conflict-auditor`, `orchestrator` |
| `audio-engine-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `cleanup` | `code-hygiene`, `orchestrator` | `orchestrator` |
| `code-hygiene` | `orchestrator` | `agent-refactor`, `cleanup`, `conflict-auditor`, `orchestrator`, `security` |
| `conflict-auditor` | `adversarial`, `agent-refactor`, `agent-updater`, `code-hygiene`, `orchestrator`, `primary-producer`, `repo-liaison`, `technical-validator`, `work-summarizer` | `agent-updater`, `conflict-resolution`, `orchestrator`, `technical-validator` |
| `conflict-resolution` | `conflict-auditor`, `git-operations`, `orchestrator` | `agent-updater`, `orchestrator` |
| `content-enricher` | — | `orchestrator`, `primary-producer`, `technical-validator` |
| `data-model-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `drag-reorder-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `format-converter` | `orchestrator`, `output-compiler` | `orchestrator`, `output-compiler`, `quality-auditor` |
| `git-operations` | `orchestrator` | `agent-updater`, `conflict-resolution`, `orchestrator`, `security` |
| `interactions-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `midi-engine-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `music-notation-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `navigator` | `orchestrator` | `orchestrator` |
| `node-build-security-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `notation-renderer-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `orchestrator` | `adversarial`, `agent-refactor`, `agent-updater`, `audio-engine-expert`, `cleanup`, `code-hygiene`, `conflict-auditor`, `conflict-resolution`, `content-enricher`, `data-model-expert`, `drag-reorder-expert`, `format-converter`, `git-operations`, `interactions-expert`, `midi-engine-expert`, `music-notation-expert`, `navigator`, `node-build-security-expert`, `notation-renderer-expert`, `output-compiler`, `playback-engine-expert`, `primary-producer`, `quality-auditor`, `repo-liaison`, `security`, `style-guardian`, `technical-validator`, `test-suite-expert`, `tool-doc-researcher`, `tool-eslint`, `tool-nodejs`, `tool-tonejs`, `tool-vexflow`, `tool-vite`, `ui-controls-expert`, `work-summarizer` | `adversarial`, `agent-refactor`, `agent-updater`, `cleanup`, `code-hygiene`, `conflict-auditor`, `conflict-resolution`, `format-converter`, `git-operations`, `navigator`, `output-compiler`, `primary-producer`, `quality-auditor`, `repo-liaison`, `security`, `style-guardian`, `technical-validator`, `work-summarizer` |
| `output-compiler` | `format-converter`, `orchestrator` | `format-converter`, `orchestrator`, `technical-validator` |
| `playback-engine-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `primary-producer` | `audio-engine-expert`, `content-enricher`, `data-model-expert`, `drag-reorder-expert`, `interactions-expert`, `midi-engine-expert`, `music-notation-expert`, `node-build-security-expert`, `notation-renderer-expert`, `orchestrator`, `playback-engine-expert`, `quality-auditor`, `style-guardian`, `technical-validator`, `test-suite-expert`, `ui-controls-expert` | `conflict-auditor`, `orchestrator`, `quality-auditor`, `style-guardian` |
| `quality-auditor` | `format-converter`, `orchestrator`, `primary-producer` | `orchestrator`, `primary-producer`, `style-guardian` |
| `repo-liaison` | `orchestrator` | `conflict-auditor`, `orchestrator`, `security` |
| `security` | `code-hygiene`, `git-operations`, `orchestrator`, `repo-liaison`, `tool-eslint`, `tool-nodejs`, `tool-tonejs`, `tool-vexflow`, `tool-vite` | `orchestrator` |
| `style-guardian` | `orchestrator`, `primary-producer`, `quality-auditor` | `orchestrator`, `primary-producer` |
| `team-builder` | — | — |
| `technical-validator` | `conflict-auditor`, `content-enricher`, `orchestrator`, `output-compiler`, `tool-eslint`, `tool-nodejs`, `tool-tonejs`, `tool-vexflow`, `tool-vite`, `work-summarizer` | `conflict-auditor`, `orchestrator`, `primary-producer` |
| `test-suite-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `tool-doc-researcher` | — | `agent-updater`, `orchestrator` |
| `tool-eslint` | — | `orchestrator`, `security`, `technical-validator` |
| `tool-nodejs` | — | `orchestrator`, `security`, `technical-validator` |
| `tool-tonejs` | — | `orchestrator`, `security`, `technical-validator` |
| `tool-vexflow` | — | `orchestrator`, `security`, `technical-validator` |
| `tool-vite` | — | `orchestrator`, `security`, `technical-validator` |
| `ui-controls-expert` | — | `adversarial`, `orchestrator`, `primary-producer` |
| `work-summarizer` | `orchestrator` | `adversarial`, `conflict-auditor`, `orchestrator`, `technical-validator` |

---

## DOT Source

Save the block below as `pipeline-graph.dot` and run
`dot -Tsvg pipeline-graph.dot -o pipeline-graph.svg` to produce an SVG.

```dot
digraph "MusicMaker Agent Team" {
    rankdir=LR;
    node [fontname="Helvetica", fontsize=11, shape=box, style="rounded,filled"];
    edge [fontsize=9];
    "adversarial" [label="Adversarial", fillcolor="#e8e8ff"];
    "agent-refactor" [label="Agent Refactor", fillcolor="#e8e8ff"];
    "agent-updater" [label="Agent Updater", fillcolor="#e8e8ff"];
    "audio-engine-expert" [label="Audio Engine Expert", fillcolor="#fff8e8"];
    "cleanup" [label="Cleanup", fillcolor="#e8e8ff"];
    "code-hygiene" [label="Code Hygiene", fillcolor="#e8e8ff"];
    "conflict-auditor" [label="Conflict Auditor", fillcolor="#e8e8ff"];
    "conflict-resolution" [label="Conflict Resolution", fillcolor="#e8e8ff"];
    "content-enricher" [label="Content Enricher", fillcolor="#e8ffe8"];
    "data-model-expert" [label="Data Model and Score I/O Expert", fillcolor="#fff8e8"];
    "drag-reorder-expert" [label="Staff System Drag-and-Drop Reorder Expert", fillcolor="#fff8e8"];
    "format-converter" [label="Format Converter", fillcolor="#e8ffe8"];
    "git-operations" [label="Git Operations", fillcolor="#e8e8ff"];
    "interactions-expert" [label="Interactions and Editing Expert", fillcolor="#fff8e8"];
    "midi-engine-expert" [label="MIDI Engine Expert", fillcolor="#fff8e8"];
    "music-notation-expert" [label="Music Notation Expert", fillcolor="#fff8e8"];
    "navigator" [label="Navigator", fillcolor="#e8e8ff"];
    "node-build-security-expert" [label="Node.js Build Pipeline and Security Layer Expert", fillcolor="#fff8e8"];
    "notation-renderer-expert" [label="Notation Renderer Expert", fillcolor="#fff8e8"];
    "orchestrator" [label="Orchestrator", fillcolor="#e8e8ff"];
    "output-compiler" [label="Output Compiler", fillcolor="#e8ffe8"];
    "playback-engine-expert" [label="Playback Engine Expert", fillcolor="#fff8e8"];
    "primary-producer" [label="Primary Producer", fillcolor="#e8ffe8"];
    "quality-auditor" [label="Quality Auditor", fillcolor="#e8ffe8"];
    "repo-liaison" [label="Repo Liaison", fillcolor="#e8e8ff"];
    "security" [label="Security", fillcolor="#e8e8ff"];
    "style-guardian" [label="Style Guardian", fillcolor="#e8ffe8"];
    "team-builder" [label="Team Builder", fillcolor="#e8e8ff"];
    "technical-validator" [label="Technical Validator", fillcolor="#e8ffe8"];
    "test-suite-expert" [label="Test Suite Expert", fillcolor="#fff8e8"];
    "tool-doc-researcher" [label="Tool Documentation Researcher", fillcolor="#ffe8e8"];
    "tool-eslint" [label="Tool Specialist", fillcolor="#ffe8e8"];
    "tool-nodejs" [label="Build System Specialist", fillcolor="#ffe8e8"];
    "tool-tonejs" [label="Tool Specialist", fillcolor="#ffe8e8"];
    "tool-vexflow" [label="Tool Specialist", fillcolor="#ffe8e8"];
    "tool-vite" [label="Build System Specialist", fillcolor="#ffe8e8"];
    "ui-controls-expert" [label="UI Controls and Event Listeners Expert", fillcolor="#fff8e8"];
    "work-summarizer" [label="Work Summarizer", fillcolor="#e8ffe8"];
    "orchestrator" -> "primary-producer" [style=solid, label="Produce / Revise Deliverable"];
    "orchestrator" -> "quality-auditor" [style=solid, label="Audit Quality"];
    "orchestrator" -> "style-guardian" [style=solid, label="Enforce Style / Standards"];
    "orchestrator" -> "technical-validator" [style=solid, label="Validate Technical Accuracy"];
    "orchestrator" -> "format-converter" [style=solid, label="Convert / Transform Output"];
    "orchestrator" -> "output-compiler" [style=solid, label="Compile Final Output"];
    "orchestrator" -> "navigator" [style=solid, label="Navigate Project"];
    "orchestrator" -> "security" [style=solid, label="Security Review"];
    "orchestrator" -> "code-hygiene" [style=solid, label="Code Hygiene Audit"];
    "orchestrator" -> "adversarial" [style=solid, label="Adversarial Review"];
    "orchestrator" -> "conflict-auditor" [style=solid, label="Conflict Audit"];
    "orchestrator" -> "conflict-resolution" [style=solid, label="Resolve Conflicts"];
    "orchestrator" -> "cleanup" [style=solid, label="Clean Up Artifacts"];
    "orchestrator" -> "agent-updater" [style=solid, label="Update Agent Docs"];
    "orchestrator" -> "agent-refactor" [style=solid, label="Refactor Agent Docs"];
    "orchestrator" -> "repo-liaison" [style=solid, label="Cross-Repository Liaison"];
    "orchestrator" -> "work-summarizer" [style=solid, label="Summarize Work Period"];
    "orchestrator" -> "git-operations" [style=solid, label="Git Operations"];
    "navigator" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "security" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "code-hygiene" -> "security" [style=solid, label="Security Clearance (for Deletions)"];
    "code-hygiene" -> "cleanup" [style=solid, label="Cleanup Agent"];
    "code-hygiene" -> "agent-refactor" [style=solid, label="Agent Refactor (Structural Violations)"];
    "code-hygiene" -> "conflict-auditor" [style=solid, label="Log Conflict"];
    "code-hygiene" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "adversarial" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "adversarial" -> "conflict-auditor" [style=solid, label="Audit for Conflicts"];
    "conflict-auditor" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "conflict-auditor" -> "agent-updater" [style=solid, label="Update Agent Docs"];
    "conflict-auditor" -> "conflict-resolution" [style=solid, label="Resolve Conflicts"];
    "conflict-auditor" -> "technical-validator" [style=solid, label="Verify Source Drift"];
    "conflict-resolution" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "conflict-resolution" -> "agent-updater" [style=solid, label="Update Agent Docs"];
    "cleanup" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "agent-updater" -> "agent-refactor" [style=solid, label="Refactor Agent Docs"];
    "agent-updater" -> "adversarial" [style=solid, label="Run Adversarial Review"];
    "agent-updater" -> "conflict-auditor" [style=solid, label="Run Conflict Audit"];
    "agent-updater" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "agent-refactor" -> "conflict-auditor" [style=solid, label="Run Conflict Audit"];
    "agent-refactor" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "repo-liaison" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "repo-liaison" -> "security" [style=solid, label="Security Review for Cross-Repo Write"];
    "repo-liaison" -> "conflict-auditor" [style=solid, label="Conflict Audit After Cross-Repo Change"];
    "git-operations" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "git-operations" -> "security" [style=solid, label="Security Review"];
    "git-operations" -> "conflict-resolution" [style=solid, label="Conflict Resolution"];
    "git-operations" -> "agent-updater" [style=solid, label="Update Agent Docs"];
    "work-summarizer" -> "technical-validator" [style=solid, label="Verify Summary Accuracy"];
    "work-summarizer" -> "adversarial" [style=solid, label="Run Adversarial Audit"];
    "work-summarizer" -> "conflict-auditor" [style=solid, label="Run Conflict Audit"];
    "work-summarizer" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "primary-producer" -> "style-guardian" [style=solid, label="Style Audit"];
    "primary-producer" -> "quality-auditor" [style=solid, label="Quality Audit"];
    "primary-producer" -> "conflict-auditor" [style=solid, label="Conflict Audit"];
    "primary-producer" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "quality-auditor" -> "primary-producer" [style=solid, label="Route Corrections to Primary Producer"];
    "quality-auditor" -> "style-guardian" [style=solid, label="Route Style Issues"];
    "quality-auditor" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "style-guardian" -> "primary-producer" [style=solid, label="Route Style Corrections"];
    "style-guardian" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "technical-validator" -> "primary-producer" [style=solid, label="Route Corrections to Primary Producer"];
    "technical-validator" -> "conflict-auditor" [style=solid, label="Log Conflict"];
    "technical-validator" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "format-converter" -> "output-compiler" [style=solid, label="Pass to Output Compiler"];
    "format-converter" -> "quality-auditor" [style=solid, label="Quality Check After Conversion"];
    "format-converter" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "output-compiler" -> "format-converter" [style=solid, label="Convert Missing Components"];
    "output-compiler" -> "technical-validator" [style=solid, label="Validate Technical Accuracy"];
    "output-compiler" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-doc-researcher" -> "agent-updater" [style=solid, label="Update Brief and Generated Docs"];
    "tool-doc-researcher" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-eslint" -> "technical-validator" [style=solid, label="Validate Tool Output"];
    "tool-eslint" -> "security" [style=solid, label="Security Clearance for Config Change"];
    "tool-eslint" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-nodejs" -> "technical-validator" [style=solid, label="Validate Build Output"];
    "tool-nodejs" -> "security" [style=solid, label="Security Clearance for Build Config Change"];
    "tool-nodejs" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-tonejs" -> "technical-validator" [style=solid, label="Validate Tool Output"];
    "tool-tonejs" -> "security" [style=solid, label="Security Clearance for Config Change"];
    "tool-tonejs" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-vexflow" -> "technical-validator" [style=solid, label="Validate Tool Output"];
    "tool-vexflow" -> "security" [style=solid, label="Security Clearance for Config Change"];
    "tool-vexflow" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "tool-vite" -> "technical-validator" [style=solid, label="Validate Build Output"];
    "tool-vite" -> "security" [style=solid, label="Security Clearance for Build Config Change"];
    "tool-vite" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "audio-engine-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "audio-engine-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "audio-engine-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "data-model-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "data-model-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "data-model-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "drag-reorder-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "drag-reorder-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "drag-reorder-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "interactions-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "interactions-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "interactions-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "midi-engine-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "midi-engine-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "midi-engine-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "music-notation-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "music-notation-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "music-notation-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "node-build-security-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "node-build-security-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "node-build-security-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "notation-renderer-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "notation-renderer-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "notation-renderer-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "playback-engine-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "playback-engine-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "playback-engine-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "test-suite-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "test-suite-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "test-suite-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "ui-controls-expert" -> "adversarial" [style=solid, label="Vet Brief Before Drafting"];
    "ui-controls-expert" -> "primary-producer" [style=solid, label="Send to Primary Producer"];
    "ui-controls-expert" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "content-enricher" -> "technical-validator" [style=solid, label="Validate Enriched Content"];
    "content-enricher" -> "orchestrator" [style=solid, label="Return to Orchestrator"];
    "content-enricher" -> "primary-producer" [style=dashed];
}
```

---

## JSON Adjacency

```json
{
  "project_name": "MusicMaker",
  "nodes": {
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
    "audio-engine-expert": {
      "display_name": "Audio Engine Expert",
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
        "edit",
        "search",
        "execute"
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
    "data-model-expert": {
      "display_name": "Data Model and Score I/O Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "drag-reorder-expert": {
      "display_name": "Staff System Drag-and-Drop Reorder Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "format-converter": {
      "display_name": "Format Converter",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute"
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
    "interactions-expert": {
      "display_name": "Interactions and Editing Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "midi-engine-expert": {
      "display_name": "MIDI Engine Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "music-notation-expert": {
      "display_name": "Music Notation Expert",
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
    "node-build-security-expert": {
      "display_name": "Node.js Build Pipeline and Security Layer Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "notation-renderer-expert": {
      "display_name": "Notation Renderer Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
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
    "playback-engine-expert": {
      "display_name": "Playback Engine Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
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
    "security": {
      "display_name": "Security",
      "agent_type": "governance",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "style-guardian": {
      "display_name": "Style Guardian",
      "agent_type": "domain",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
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
    "test-suite-expert": {
      "display_name": "Test Suite Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
      ]
    },
    "tool-doc-researcher": {
      "display_name": "Tool Documentation Researcher",
      "agent_type": "tool_specialist",
      "user_invokable": false,
      "tools": [
        "read",
        "search"
      ]
    },
    "tool-eslint": {
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
    "tool-nodejs": {
      "display_name": "Build System Specialist",
      "agent_type": "tool_specialist",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute",
        "search"
      ]
    },
    "tool-tonejs": {
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
    "tool-vexflow": {
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
    "tool-vite": {
      "display_name": "Build System Specialist",
      "agent_type": "tool_specialist",
      "user_invokable": false,
      "tools": [
        "read",
        "edit",
        "execute",
        "search"
      ]
    },
    "ui-controls-expert": {
      "display_name": "UI Controls and Event Listeners Expert",
      "agent_type": "workstream_expert",
      "user_invokable": false,
      "tools": [
        "read",
        "search",
        "agent"
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
      "source": "orchestrator",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Produce / Revise Deliverable"
    },
    {
      "source": "orchestrator",
      "target": "quality-auditor",
      "edge_type": "handoff",
      "label": "Audit Quality"
    },
    {
      "source": "orchestrator",
      "target": "style-guardian",
      "edge_type": "handoff",
      "label": "Enforce Style / Standards"
    },
    {
      "source": "orchestrator",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Technical Accuracy"
    },
    {
      "source": "orchestrator",
      "target": "format-converter",
      "edge_type": "handoff",
      "label": "Convert / Transform Output"
    },
    {
      "source": "orchestrator",
      "target": "output-compiler",
      "edge_type": "handoff",
      "label": "Compile Final Output"
    },
    {
      "source": "orchestrator",
      "target": "navigator",
      "edge_type": "handoff",
      "label": "Navigate Project"
    },
    {
      "source": "orchestrator",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Review"
    },
    {
      "source": "orchestrator",
      "target": "code-hygiene",
      "edge_type": "handoff",
      "label": "Code Hygiene Audit"
    },
    {
      "source": "orchestrator",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Adversarial Review"
    },
    {
      "source": "orchestrator",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Conflict Audit"
    },
    {
      "source": "orchestrator",
      "target": "conflict-resolution",
      "edge_type": "handoff",
      "label": "Resolve Conflicts"
    },
    {
      "source": "orchestrator",
      "target": "cleanup",
      "edge_type": "handoff",
      "label": "Clean Up Artifacts"
    },
    {
      "source": "orchestrator",
      "target": "agent-updater",
      "edge_type": "handoff",
      "label": "Update Agent Docs"
    },
    {
      "source": "orchestrator",
      "target": "agent-refactor",
      "edge_type": "handoff",
      "label": "Refactor Agent Docs"
    },
    {
      "source": "orchestrator",
      "target": "repo-liaison",
      "edge_type": "handoff",
      "label": "Cross-Repository Liaison"
    },
    {
      "source": "orchestrator",
      "target": "work-summarizer",
      "edge_type": "handoff",
      "label": "Summarize Work Period"
    },
    {
      "source": "orchestrator",
      "target": "git-operations",
      "edge_type": "handoff",
      "label": "Git Operations"
    },
    {
      "source": "navigator",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "security",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "code-hygiene",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance (for Deletions)"
    },
    {
      "source": "code-hygiene",
      "target": "cleanup",
      "edge_type": "handoff",
      "label": "Cleanup Agent"
    },
    {
      "source": "code-hygiene",
      "target": "agent-refactor",
      "edge_type": "handoff",
      "label": "Agent Refactor (Structural Violations)"
    },
    {
      "source": "code-hygiene",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Log Conflict"
    },
    {
      "source": "code-hygiene",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "adversarial",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "adversarial",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Audit for Conflicts"
    },
    {
      "source": "conflict-auditor",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "conflict-auditor",
      "target": "agent-updater",
      "edge_type": "handoff",
      "label": "Update Agent Docs"
    },
    {
      "source": "conflict-auditor",
      "target": "conflict-resolution",
      "edge_type": "handoff",
      "label": "Resolve Conflicts"
    },
    {
      "source": "conflict-auditor",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Verify Source Drift"
    },
    {
      "source": "conflict-auditor",
      "target": "conflict-resolution",
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
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "conflict-resolution",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "conflict-resolution",
      "target": "agent-updater",
      "edge_type": "handoff",
      "label": "Update Agent Docs"
    },
    {
      "source": "cleanup",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "agent-updater",
      "target": "agent-refactor",
      "edge_type": "handoff",
      "label": "Refactor Agent Docs"
    },
    {
      "source": "agent-updater",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Run Adversarial Review"
    },
    {
      "source": "agent-updater",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Run Conflict Audit"
    },
    {
      "source": "agent-updater",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "agent-updater",
      "target": "adversarial",
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
      "source": "agent-updater",
      "target": "agent-refactor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "agent-refactor",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Run Conflict Audit"
    },
    {
      "source": "agent-refactor",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "agent-refactor",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "repo-liaison",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "repo-liaison",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Review for Cross-Repo Write"
    },
    {
      "source": "repo-liaison",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Conflict Audit After Cross-Repo Change"
    },
    {
      "source": "git-operations",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "git-operations",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Review"
    },
    {
      "source": "git-operations",
      "target": "conflict-resolution",
      "edge_type": "handoff",
      "label": "Conflict Resolution"
    },
    {
      "source": "git-operations",
      "target": "agent-updater",
      "edge_type": "handoff",
      "label": "Update Agent Docs"
    },
    {
      "source": "work-summarizer",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Verify Summary Accuracy"
    },
    {
      "source": "work-summarizer",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Run Adversarial Audit"
    },
    {
      "source": "work-summarizer",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Run Conflict Audit"
    },
    {
      "source": "work-summarizer",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "work-summarizer",
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
      "source": "primary-producer",
      "target": "style-guardian",
      "edge_type": "handoff",
      "label": "Style Audit"
    },
    {
      "source": "primary-producer",
      "target": "quality-auditor",
      "edge_type": "handoff",
      "label": "Quality Audit"
    },
    {
      "source": "primary-producer",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Conflict Audit"
    },
    {
      "source": "primary-producer",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "primary-producer",
      "target": "style-guardian",
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
      "source": "primary-producer",
      "target": "conflict-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "quality-auditor",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Route Corrections to Primary Producer"
    },
    {
      "source": "quality-auditor",
      "target": "style-guardian",
      "edge_type": "handoff",
      "label": "Route Style Issues"
    },
    {
      "source": "quality-auditor",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "quality-auditor",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "quality-auditor",
      "target": "style-guardian",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "style-guardian",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Route Style Corrections"
    },
    {
      "source": "style-guardian",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "style-guardian",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "technical-validator",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Route Corrections to Primary Producer"
    },
    {
      "source": "technical-validator",
      "target": "conflict-auditor",
      "edge_type": "handoff",
      "label": "Log Conflict"
    },
    {
      "source": "technical-validator",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "technical-validator",
      "target": "primary-producer",
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
      "source": "format-converter",
      "target": "output-compiler",
      "edge_type": "handoff",
      "label": "Pass to Output Compiler"
    },
    {
      "source": "format-converter",
      "target": "quality-auditor",
      "edge_type": "handoff",
      "label": "Quality Check After Conversion"
    },
    {
      "source": "format-converter",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "format-converter",
      "target": "output-compiler",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "format-converter",
      "target": "quality-auditor",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "output-compiler",
      "target": "format-converter",
      "edge_type": "handoff",
      "label": "Convert Missing Components"
    },
    {
      "source": "output-compiler",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Technical Accuracy"
    },
    {
      "source": "output-compiler",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "output-compiler",
      "target": "format-converter",
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
      "source": "tool-doc-researcher",
      "target": "agent-updater",
      "edge_type": "handoff",
      "label": "Update Brief and Generated Docs"
    },
    {
      "source": "tool-doc-researcher",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-eslint",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Tool Output"
    },
    {
      "source": "tool-eslint",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance for Config Change"
    },
    {
      "source": "tool-eslint",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-eslint",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-eslint",
      "target": "security",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-nodejs",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Build Output"
    },
    {
      "source": "tool-nodejs",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance for Build Config Change"
    },
    {
      "source": "tool-nodejs",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-nodejs",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-nodejs",
      "target": "security",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-tonejs",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Tool Output"
    },
    {
      "source": "tool-tonejs",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance for Config Change"
    },
    {
      "source": "tool-tonejs",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-tonejs",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-tonejs",
      "target": "security",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-vexflow",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Tool Output"
    },
    {
      "source": "tool-vexflow",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance for Config Change"
    },
    {
      "source": "tool-vexflow",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-vexflow",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-vexflow",
      "target": "security",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-vite",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Build Output"
    },
    {
      "source": "tool-vite",
      "target": "security",
      "edge_type": "handoff",
      "label": "Security Clearance for Build Config Change"
    },
    {
      "source": "tool-vite",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "tool-vite",
      "target": "technical-validator",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "tool-vite",
      "target": "security",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "audio-engine-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "audio-engine-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "audio-engine-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "audio-engine-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "audio-engine-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "data-model-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "data-model-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "data-model-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "data-model-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "data-model-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "drag-reorder-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "drag-reorder-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "drag-reorder-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "drag-reorder-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "drag-reorder-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "interactions-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "interactions-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "interactions-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "interactions-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "interactions-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "midi-engine-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "midi-engine-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "midi-engine-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "midi-engine-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "midi-engine-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "music-notation-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "music-notation-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "music-notation-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "music-notation-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "music-notation-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "node-build-security-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "node-build-security-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "node-build-security-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "node-build-security-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "node-build-security-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "notation-renderer-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "notation-renderer-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "notation-renderer-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "notation-renderer-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "notation-renderer-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "playback-engine-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "playback-engine-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "playback-engine-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "playback-engine-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "playback-engine-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "test-suite-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "test-suite-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "test-suite-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "test-suite-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "test-suite-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ui-controls-expert",
      "target": "adversarial",
      "edge_type": "handoff",
      "label": "Vet Brief Before Drafting"
    },
    {
      "source": "ui-controls-expert",
      "target": "primary-producer",
      "edge_type": "handoff",
      "label": "Send to Primary Producer"
    },
    {
      "source": "ui-controls-expert",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
    },
    {
      "source": "ui-controls-expert",
      "target": "primary-producer",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "ui-controls-expert",
      "target": "adversarial",
      "edge_type": "agents-list",
      "label": null
    },
    {
      "source": "content-enricher",
      "target": "technical-validator",
      "edge_type": "handoff",
      "label": "Validate Enriched Content"
    },
    {
      "source": "content-enricher",
      "target": "orchestrator",
      "edge_type": "handoff",
      "label": "Return to Orchestrator"
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
    }
  ],
  "adjacency": {
    "orchestrator": [
      "adversarial",
      "agent-refactor",
      "agent-updater",
      "cleanup",
      "code-hygiene",
      "conflict-auditor",
      "conflict-resolution",
      "format-converter",
      "git-operations",
      "navigator",
      "output-compiler",
      "primary-producer",
      "quality-auditor",
      "repo-liaison",
      "security",
      "style-guardian",
      "technical-validator",
      "work-summarizer"
    ],
    "navigator": [
      "orchestrator"
    ],
    "security": [
      "orchestrator"
    ],
    "code-hygiene": [
      "agent-refactor",
      "cleanup",
      "conflict-auditor",
      "orchestrator",
      "security"
    ],
    "adversarial": [
      "conflict-auditor",
      "orchestrator"
    ],
    "conflict-auditor": [
      "agent-updater",
      "conflict-resolution",
      "orchestrator",
      "technical-validator"
    ],
    "conflict-resolution": [
      "agent-updater",
      "orchestrator"
    ],
    "cleanup": [
      "orchestrator"
    ],
    "agent-updater": [
      "adversarial",
      "agent-refactor",
      "conflict-auditor",
      "orchestrator"
    ],
    "agent-refactor": [
      "conflict-auditor",
      "orchestrator"
    ],
    "repo-liaison": [
      "conflict-auditor",
      "orchestrator",
      "security"
    ],
    "git-operations": [
      "agent-updater",
      "conflict-resolution",
      "orchestrator",
      "security"
    ],
    "work-summarizer": [
      "adversarial",
      "conflict-auditor",
      "orchestrator",
      "technical-validator"
    ],
    "primary-producer": [
      "conflict-auditor",
      "orchestrator",
      "quality-auditor",
      "style-guardian"
    ],
    "quality-auditor": [
      "orchestrator",
      "primary-producer",
      "style-guardian"
    ],
    "style-guardian": [
      "orchestrator",
      "primary-producer"
    ],
    "technical-validator": [
      "conflict-auditor",
      "orchestrator",
      "primary-producer"
    ],
    "format-converter": [
      "orchestrator",
      "output-compiler",
      "quality-auditor"
    ],
    "output-compiler": [
      "format-converter",
      "orchestrator",
      "technical-validator"
    ],
    "tool-doc-researcher": [
      "agent-updater",
      "orchestrator"
    ],
    "tool-eslint": [
      "orchestrator",
      "security",
      "technical-validator"
    ],
    "tool-nodejs": [
      "orchestrator",
      "security",
      "technical-validator"
    ],
    "tool-tonejs": [
      "orchestrator",
      "security",
      "technical-validator"
    ],
    "tool-vexflow": [
      "orchestrator",
      "security",
      "technical-validator"
    ],
    "tool-vite": [
      "orchestrator",
      "security",
      "technical-validator"
    ],
    "audio-engine-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "data-model-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "drag-reorder-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "interactions-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "midi-engine-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "music-notation-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "node-build-security-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "notation-renderer-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "playback-engine-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "test-suite-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "ui-controls-expert": [
      "adversarial",
      "orchestrator",
      "primary-producer"
    ],
    "team-builder": [],
    "content-enricher": [
      "orchestrator",
      "primary-producer",
      "technical-validator"
    ]
  }
}
```
<!-- AGENTTEAMS:END content -->
