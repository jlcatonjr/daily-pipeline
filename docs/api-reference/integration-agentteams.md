# `integration.agentteams` — daily-pipeline

Build and persist Stage 6 integration request payloads.

> Source: `daily_pipeline/integration/agentteams.py`

---

## Public Functions

### `build_integration_request(abstract_team, trigger, target_repo, confidence_floor)`

Create an `IntegrationRequest` dataclass containing a filtered payload for AgentTeams update-request workflows.

Args:

- `abstract_team` (`AbstractTeamOutput`)
- `trigger` (`str`)
- `target_repo` (`str`)
- `confidence_floor` (`float`)

Returns:

- `IntegrationRequest`

Behavior:

- Includes shared capabilities/references above confidence floor.
- Preserves mapping and provenance metadata.
- Stores trigger metadata (`team-create` or `team-update`) in the payload while current action remains `agentteams-update-request`.
- Adds constraints:
  - `reference_only_external_scripts`
  - `no_private_imports`

---

### `write_integration_request(request, out_dir)`

Write JSON payload to disk.

Args:

- `request` (`IntegrationRequest`)
- `out_dir` (`str`)

Returns:

- `str` — path to written JSON file (`agentteams-request-<trigger>.json`)
