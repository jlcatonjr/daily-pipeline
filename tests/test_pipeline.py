from __future__ import annotations

from pathlib import Path

from daily_pipeline.config import load_config
from daily_pipeline.protocol import run_protocol


def fixture_path(name: str) -> str:
    return str(Path(__file__).parent / "fixtures" / name)


def test_run_protocol_generates_outputs(tmp_path: Path) -> None:
    config = load_config(None)
    out_root = tmp_path / "out"

    result = run_protocol(
        team_paths=[fixture_path("team_a.json"), fixture_path("team_b.json")],
        config=config,
        trigger="team-update",
        output_root=str(out_root),
        allow_degraded=True,
    )

    run_dir = Path(result["run_dir"])
    assert run_dir.exists()
    assert (run_dir / "01-validate-selection.json").exists()
    assert (run_dir / "06-build-agentteams-integration.json").exists()
    assert Path(result["report"]).exists()


def test_cli_dry_run_smoke(tmp_path: Path) -> None:
    team_file = fixture_path("team_a.json")
    assert Path(team_file).exists()
