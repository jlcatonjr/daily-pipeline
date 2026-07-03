<!-- AGENTTEAMS:BEGIN content v=1 -->
# daily_pipeline — Repository Architecture Map

> **Auto-generated.** Regenerated on every commit that touches the `daily_pipeline` package. Do not edit manually — changes will be overwritten.

- Modules mapped: **17**
- Packages: **6**
- Internal import edges: **18**
- Distinct external dependencies: **0**

---

## Package Dependency Diagram

Inter-package import dependencies (module-level detail in the tables below).

```mermaid
flowchart LR
    classDef root fill:#e8eefb,stroke:#1b3fa0,color:#000
    classDef sub  fill:#eef6ee,stroke:#3f8f4f,color:#000
    daily_pipeline["daily_pipeline"]
    class daily_pipeline root
    daily_pipeline_abstraction["daily_pipeline.abstraction"]
    class daily_pipeline_abstraction sub
    daily_pipeline_analysis["daily_pipeline.analysis"]
    class daily_pipeline_analysis sub
    daily_pipeline_ingest["daily_pipeline.ingest"]
    class daily_pipeline_ingest sub
    daily_pipeline_integration["daily_pipeline.integration"]
    class daily_pipeline_integration sub
    daily_pipeline_reporting["daily_pipeline.reporting"]
    class daily_pipeline_reporting sub
    daily_pipeline --> daily_pipeline_abstraction
    daily_pipeline --> daily_pipeline_analysis
    daily_pipeline --> daily_pipeline_ingest
    daily_pipeline --> daily_pipeline_integration
    daily_pipeline --> daily_pipeline_reporting
    daily_pipeline_abstraction --> daily_pipeline
    daily_pipeline_analysis --> daily_pipeline
    daily_pipeline_ingest --> daily_pipeline
    daily_pipeline_integration --> daily_pipeline
    daily_pipeline_reporting --> daily_pipeline
```

---

## Packages

| Package | Modules | Depends on |
| --- | --- | --- |
| `daily_pipeline` | 10 | `daily_pipeline.abstraction`, `daily_pipeline.analysis`, `daily_pipeline.ingest`, `daily_pipeline.integration`, `daily_pipeline.reporting` |
| `daily_pipeline.abstraction` | 1 | `daily_pipeline` |
| `daily_pipeline.analysis` | 2 | `daily_pipeline` |
| `daily_pipeline.ingest` | 1 | `daily_pipeline` |
| `daily_pipeline.integration` | 2 | `daily_pipeline` |
| `daily_pipeline.reporting` | 1 | `daily_pipeline` |

---

## Module Dependency Table

| Module | Imports (internal) | Imported by |
| --- | --- | --- |
| `daily_pipeline` | — | — |
| `daily_pipeline.abstraction` | — | — |
| `daily_pipeline.abstraction.synthesizer` | `daily_pipeline.models` | `daily_pipeline.protocol` |
| `daily_pipeline.analysis` | — | — |
| `daily_pipeline.analysis.capabilities` | `daily_pipeline.models` | `daily_pipeline.protocol` |
| `daily_pipeline.analysis.references` | `daily_pipeline.models` | `daily_pipeline.protocol` |
| `daily_pipeline.cli` | `daily_pipeline.config`, `daily_pipeline.integration.sync`, `daily_pipeline.protocol` | — |
| `daily_pipeline.config` | — | `daily_pipeline.cli`, `daily_pipeline.protocol` |
| `daily_pipeline.ingest` | — | — |
| `daily_pipeline.ingest.loader` | `daily_pipeline.models` | `daily_pipeline.protocol` |
| `daily_pipeline.integration` | — | — |
| `daily_pipeline.integration.agentteams` | `daily_pipeline.models` | `daily_pipeline.protocol` |
| `daily_pipeline.integration.sync` | `daily_pipeline.models` | `daily_pipeline.cli` |
| `daily_pipeline.models` | — | `daily_pipeline.abstraction.synthesizer`, `daily_pipeline.analysis.capabilities`, `daily_pipeline.analysis.references`, `daily_pipeline.ingest.loader`, `daily_pipeline.integration.agentteams`, `daily_pipeline.integration.sync`, `daily_pipeline.protocol`, `daily_pipeline.reporting.writer` |
| `daily_pipeline.protocol` | `daily_pipeline.abstraction.synthesizer`, `daily_pipeline.analysis.capabilities`, `daily_pipeline.analysis.references`, `daily_pipeline.config`, `daily_pipeline.ingest.loader`, `daily_pipeline.integration.agentteams`, `daily_pipeline.models`, `daily_pipeline.reporting.writer` | `daily_pipeline.cli` |
| `daily_pipeline.reporting` | — | — |
| `daily_pipeline.reporting.writer` | `daily_pipeline.models` | `daily_pipeline.protocol` |

---

## External Dependencies

Third-party (non-stdlib) top-level packages imported by the mapped package:

_None detected (standard library only)._

---

## DOT Source

```dot
digraph "daily_pipeline architecture" {
    rankdir=LR;
    node [fontname="Helvetica", fontsize=11, shape=box, style="rounded,filled", fillcolor="#eef6ee"];
    edge [fontsize=9];
    "daily_pipeline" [fillcolor="#e8eefb"];
    "daily_pipeline.abstraction" [fillcolor="#eef6ee"];
    "daily_pipeline.analysis" [fillcolor="#eef6ee"];
    "daily_pipeline.ingest" [fillcolor="#eef6ee"];
    "daily_pipeline.integration" [fillcolor="#eef6ee"];
    "daily_pipeline.reporting" [fillcolor="#eef6ee"];
    "daily_pipeline" -> "daily_pipeline.abstraction";
    "daily_pipeline" -> "daily_pipeline.analysis";
    "daily_pipeline" -> "daily_pipeline.ingest";
    "daily_pipeline" -> "daily_pipeline.integration";
    "daily_pipeline" -> "daily_pipeline.reporting";
    "daily_pipeline.abstraction" -> "daily_pipeline";
    "daily_pipeline.analysis" -> "daily_pipeline";
    "daily_pipeline.ingest" -> "daily_pipeline";
    "daily_pipeline.integration" -> "daily_pipeline";
    "daily_pipeline.reporting" -> "daily_pipeline";
}
```

---

## JSON (module-level)

```json
{
  "root_package": "daily_pipeline",
  "modules": {
    "daily_pipeline": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/__init__.py",
      "is_package": true,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.abstraction": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/abstraction/__init__.py",
      "is_package": true,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.abstraction.synthesizer": {
      "package": "daily_pipeline.abstraction",
      "path": "daily_pipeline/abstraction/synthesizer.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.models"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.analysis": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/analysis/__init__.py",
      "is_package": true,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.analysis.capabilities": {
      "package": "daily_pipeline.analysis",
      "path": "daily_pipeline/analysis/capabilities.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.models"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.analysis.references": {
      "package": "daily_pipeline.analysis",
      "path": "daily_pipeline/analysis/references.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.models"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.cli": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/cli.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.config",
        "daily_pipeline.integration.sync",
        "daily_pipeline.protocol"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.config": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/config.py",
      "is_package": false,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.ingest": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/ingest/__init__.py",
      "is_package": true,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.ingest.loader": {
      "package": "daily_pipeline.ingest",
      "path": "daily_pipeline/ingest/loader.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.models"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.integration": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/integration/__init__.py",
      "is_package": true,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.integration.agentteams": {
      "package": "daily_pipeline.integration",
      "path": "daily_pipeline/integration/agentteams.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.models"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.integration.sync": {
      "package": "daily_pipeline.integration",
      "path": "daily_pipeline/integration/sync.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.models"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.models": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/models.py",
      "is_package": false,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.protocol": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/protocol.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.abstraction.synthesizer",
        "daily_pipeline.analysis.capabilities",
        "daily_pipeline.analysis.references",
        "daily_pipeline.config",
        "daily_pipeline.ingest.loader",
        "daily_pipeline.integration.agentteams",
        "daily_pipeline.models",
        "daily_pipeline.reporting.writer"
      ],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.reporting": {
      "package": "daily_pipeline",
      "path": "daily_pipeline/reporting/__init__.py",
      "is_package": true,
      "imports_internal": [],
      "external": [],
      "repo_local": []
    },
    "daily_pipeline.reporting.writer": {
      "package": "daily_pipeline.reporting",
      "path": "daily_pipeline/reporting/writer.py",
      "is_package": false,
      "imports_internal": [
        "daily_pipeline.models"
      ],
      "external": [],
      "repo_local": []
    }
  },
  "package_edges": [
    {
      "source": "daily_pipeline",
      "target": "daily_pipeline.abstraction"
    },
    {
      "source": "daily_pipeline",
      "target": "daily_pipeline.analysis"
    },
    {
      "source": "daily_pipeline",
      "target": "daily_pipeline.ingest"
    },
    {
      "source": "daily_pipeline",
      "target": "daily_pipeline.integration"
    },
    {
      "source": "daily_pipeline",
      "target": "daily_pipeline.reporting"
    },
    {
      "source": "daily_pipeline.abstraction",
      "target": "daily_pipeline"
    },
    {
      "source": "daily_pipeline.analysis",
      "target": "daily_pipeline"
    },
    {
      "source": "daily_pipeline.ingest",
      "target": "daily_pipeline"
    },
    {
      "source": "daily_pipeline.integration",
      "target": "daily_pipeline"
    },
    {
      "source": "daily_pipeline.reporting",
      "target": "daily_pipeline"
    }
  ],
  "module_edges": [
    {
      "source": "daily_pipeline.abstraction.synthesizer",
      "target": "daily_pipeline.models"
    },
    {
      "source": "daily_pipeline.analysis.capabilities",
      "target": "daily_pipeline.models"
    },
    {
      "source": "daily_pipeline.analysis.references",
      "target": "daily_pipeline.models"
    },
    {
      "source": "daily_pipeline.cli",
      "target": "daily_pipeline.config"
    },
    {
      "source": "daily_pipeline.cli",
      "target": "daily_pipeline.integration.sync"
    },
    {
      "source": "daily_pipeline.cli",
      "target": "daily_pipeline.protocol"
    },
    {
      "source": "daily_pipeline.ingest.loader",
      "target": "daily_pipeline.models"
    },
    {
      "source": "daily_pipeline.integration.agentteams",
      "target": "daily_pipeline.models"
    },
    {
      "source": "daily_pipeline.integration.sync",
      "target": "daily_pipeline.models"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.abstraction.synthesizer"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.analysis.capabilities"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.analysis.references"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.config"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.ingest.loader"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.integration.agentteams"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.models"
    },
    {
      "source": "daily_pipeline.protocol",
      "target": "daily_pipeline.reporting.writer"
    },
    {
      "source": "daily_pipeline.reporting.writer",
      "target": "daily_pipeline.models"
    }
  ],
  "external_dependencies": [],
  "repo_local_dependencies": []
}
```
<!-- AGENTTEAMS:END content -->
