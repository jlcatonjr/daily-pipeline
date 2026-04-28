from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from daily_pipeline.models import SyncResult


def discover_sync_targets(root_dir: str) -> list[str]:
    """Return absolute paths of repos directly inside root_dir (or root_dir itself)
    that contain .github/agents/_build-description.json.

    Checks root_dir itself first, then all immediate subdirectories.
    """
    root = Path(root_dir).resolve()
    candidates = [root] + [p for p in root.iterdir() if p.is_dir()]
    targets: list[str] = []
    for candidate in candidates:
        if (candidate / ".github" / "agents" / "_build-description.json").is_file():
            targets.append(str(candidate))
    return targets


def _resolve_build_team_py(build_team_py: str | None) -> tuple[str | None, str]:
    """Resolve build_team.py path using resolution order:
    1. Explicit argument (if provided and non-empty)
    2. AGENTTEAMS_REPO environment variable → $AGENTTEAMS_REPO/build_team.py
    Returns (resolved_path_or_None, skip_reason_if_unresolved).
    """
    if build_team_py:
        resolved = Path(build_team_py).resolve()
        if not resolved.is_file():
            return None, "build_team_py_not_found"
        return str(resolved), ""

    env_repo = os.environ.get("AGENTTEAMS_REPO", "")
    if env_repo:
        candidate = Path(env_repo) / "build_team.py"
        if candidate.is_file():
            return str(candidate.resolve()), ""
        return None, "build_team_py_not_found"

    return None, "build_team_py_not_configured"


def execute_agentteams_sync(
    target_repo: str,
    build_team_py: str | None = None,
    post_audit: bool = False,
    dry_run: bool = False,
) -> SyncResult:
    """Invoke build_team.py --update --merge --yes against target_repo.

    Resolution order for build_team_py:
    1. build_team_py argument (if non-None and non-empty)
    2. $AGENTTEAMS_REPO/build_team.py environment variable fallback

    Skip conditions (status='skipped'):
    - build_team_py_not_configured: no path resolved from any source
    - build_team_py_not_found: resolved path does not exist on disk
    - build_description_missing: target_repo/.github/agents/_build-description.json absent
    - dry_run: dry_run=True; returns what would be executed without invoking subprocess

    Always returns SyncResult (never raises).
    """
    target = Path(target_repo).resolve()
    build_desc = target / ".github" / "agents" / "_build-description.json"

    if dry_run:
        return SyncResult(
            target_repo=str(target),
            status="skipped",
            skip_reason="dry_run",
            raw_output="",
            warnings=[f"dry_run: would sync {target}"],
        )

    if not build_desc.is_file():
        return SyncResult(
            target_repo=str(target),
            status="skipped",
            skip_reason="build_description_missing",
            raw_output="",
            warnings=[f"build_description_missing: {build_desc} not found"],
        )

    resolved_path, skip_reason = _resolve_build_team_py(build_team_py)
    if resolved_path is None:
        return SyncResult(
            target_repo=str(target),
            status="skipped",
            skip_reason=skip_reason,
            raw_output="",
            warnings=[f"{skip_reason}: build_team.py could not be resolved"],
        )

    cmd = [
        sys.executable,
        resolved_path,
        "--description",
        str(build_desc),
        "--project",
        str(target),
        "--update",
        "--merge",
        "--yes",
    ]
    if post_audit:
        cmd.append("--post-audit")

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
        raw_output = (proc.stdout or "") + (proc.stderr or "")
        warnings: list[str] = []
        if proc.returncode != 0:
            warnings.append(f"build_team.py exited with code {proc.returncode}")
            return SyncResult(
                target_repo=str(target),
                status="failed",
                skip_reason="",
                raw_output=raw_output,
                warnings=warnings,
            )
        return SyncResult(
            target_repo=str(target),
            status="ok",
            skip_reason="",
            raw_output=raw_output,
            warnings=warnings,
        )
    except Exception as exc:
        return SyncResult(
            target_repo=str(target),
            status="failed",
            skip_reason="",
            raw_output="",
            warnings=[f"subprocess exception: {exc}"],
        )
