from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from daily_pipeline.integration.sync import discover_sync_targets, execute_agentteams_sync
from daily_pipeline.models import SyncResult


# ---------------------------------------------------------------------------
# discover_sync_targets
# ---------------------------------------------------------------------------


def test_discover_sync_targets_detects_correct_repos(tmp_path: Path) -> None:
    # Repo with build description
    repo_a = tmp_path / "repo-a"
    (repo_a / ".github" / "agents").mkdir(parents=True)
    (repo_a / ".github" / "agents" / "_build-description.json").write_text("{}")

    # Repo without build description
    repo_b = tmp_path / "repo-b"
    repo_b.mkdir()

    # File (not a dir) — should not be considered
    (tmp_path / "not-a-dir.txt").write_text("x")

    targets = discover_sync_targets(str(tmp_path))
    assert str(repo_a) in targets
    assert str(repo_b) not in targets


def test_discover_sync_targets_detects_root_itself(tmp_path: Path) -> None:
    (tmp_path / ".github" / "agents").mkdir(parents=True)
    (tmp_path / ".github" / "agents" / "_build-description.json").write_text("{}")

    targets = discover_sync_targets(str(tmp_path))
    assert str(tmp_path) in targets


# ---------------------------------------------------------------------------
# execute_agentteams_sync — subprocess paths
# ---------------------------------------------------------------------------


def _make_target(tmp_path: Path) -> Path:
    target = tmp_path / "target-repo"
    (target / ".github" / "agents").mkdir(parents=True)
    (target / ".github" / "agents" / "_build-description.json").write_text("{}")
    return target


def test_execute_agentteams_sync_ok(tmp_path: Path) -> None:
    target = _make_target(tmp_path)
    build_team_py = tmp_path / "build_team.py"
    build_team_py.write_text("# stub")

    mock_proc = MagicMock(returncode=0, stdout="Written: 2\n", stderr="")
    with patch("subprocess.run", return_value=mock_proc) as mock_run:
        result = execute_agentteams_sync(str(target), str(build_team_py))

    assert result.status == "ok"
    assert result.skip_reason == ""
    assert "Written: 2" in result.raw_output
    mock_run.assert_called_once()


def test_execute_agentteams_sync_failed_on_nonzero_exit(tmp_path: Path) -> None:
    target = _make_target(tmp_path)
    build_team_py = tmp_path / "build_team.py"
    build_team_py.write_text("# stub")

    mock_proc = MagicMock(returncode=1, stdout="", stderr="Error detail")
    with patch("subprocess.run", return_value=mock_proc):
        result = execute_agentteams_sync(str(target), str(build_team_py))

    assert result.status == "failed"
    assert "exited with code 1" in result.warnings[0]


def test_execute_agentteams_sync_skips_on_missing_build_team_py_none(tmp_path: Path) -> None:
    target = _make_target(tmp_path)

    # Clear AGENTTEAMS_REPO to prevent env-var fallback
    env = {k: v for k, v in os.environ.items() if k != "AGENTTEAMS_REPO"}
    with patch.dict(os.environ, env, clear=True):
        with patch("subprocess.run") as mock_run:
            result = execute_agentteams_sync(str(target), build_team_py=None)

    assert result.status == "skipped"
    assert result.skip_reason == "build_team_py_not_configured"
    mock_run.assert_not_called()


def test_execute_agentteams_sync_skips_on_nonexistent_build_team_py(tmp_path: Path) -> None:
    target = _make_target(tmp_path)
    nonexistent = str(tmp_path / "does_not_exist.py")

    with patch("subprocess.run") as mock_run:
        result = execute_agentteams_sync(str(target), nonexistent)

    assert result.status == "skipped"
    assert result.skip_reason == "build_team_py_not_found"
    mock_run.assert_not_called()


def test_execute_agentteams_sync_skips_on_missing_build_description(tmp_path: Path) -> None:
    target = tmp_path / "no-desc-repo"
    target.mkdir()
    build_team_py = tmp_path / "build_team.py"
    build_team_py.write_text("# stub")

    with patch("subprocess.run") as mock_run:
        result = execute_agentteams_sync(str(target), str(build_team_py))

    assert result.status == "skipped"
    assert result.skip_reason == "build_description_missing"
    mock_run.assert_not_called()


def test_execute_agentteams_sync_dry_run_no_subprocess(tmp_path: Path) -> None:
    target = _make_target(tmp_path)
    build_team_py = tmp_path / "build_team.py"
    build_team_py.write_text("# stub")

    with patch("subprocess.run") as mock_run:
        result = execute_agentteams_sync(str(target), str(build_team_py), dry_run=True)

    assert result.status == "skipped"
    assert result.skip_reason == "dry_run"
    mock_run.assert_not_called()


def test_execute_agentteams_sync_handles_subprocess_exception(tmp_path: Path) -> None:
    target = _make_target(tmp_path)
    build_team_py = tmp_path / "build_team.py"
    build_team_py.write_text("# stub")

    with patch("subprocess.run", side_effect=OSError("permission denied")):
        result = execute_agentteams_sync(str(target), str(build_team_py))

    assert result.status == "failed"
    assert any("permission denied" in w for w in result.warnings)


def test_execute_agentteams_sync_arg_takes_precedence_over_env(tmp_path: Path) -> None:
    target = _make_target(tmp_path)

    arg_build_team_py = tmp_path / "arg_build_team.py"
    arg_build_team_py.write_text("# arg stub")

    env_repo = tmp_path / "env_agentteams"
    env_repo.mkdir()
    env_build_team_py = env_repo / "build_team.py"
    env_build_team_py.write_text("# env stub")

    mock_proc = MagicMock(returncode=0, stdout="ok\n", stderr="")
    with patch.dict(os.environ, {"AGENTTEAMS_REPO": str(env_repo)}):
        with patch("subprocess.run", return_value=mock_proc) as mock_run:
            result = execute_agentteams_sync(str(target), str(arg_build_team_py))

    assert result.status == "ok"
    called_cmd = mock_run.call_args[0][0]
    # The arg-provided path should be in the command, not the env-derived one
    assert str(arg_build_team_py.resolve()) in called_cmd
    assert str(env_build_team_py) not in called_cmd
