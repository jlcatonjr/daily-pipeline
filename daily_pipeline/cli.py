from __future__ import annotations

import argparse
from pathlib import Path

from daily_pipeline.config import load_config
from daily_pipeline.protocol import run_protocol


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run multi-team daily pipeline")
    parser.add_argument("--team", action="append", default=[], help="Path to team JSON file (repeatable)")
    parser.add_argument(
        "--teams-file",
        help="Path to text file containing one team JSON path per line",
    )
    parser.add_argument("--config", help="Path to JSON config")
    parser.add_argument("--trigger", default="team-update", choices=["team-create", "team-update"])
    parser.add_argument("--output-root", default="tmp/daily-pipeline")
    parser.add_argument("--allow-degraded", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def _resolve_team_paths(args: argparse.Namespace) -> list[str]:
    team_paths = list(args.team)
    if args.teams_file:
        lines = Path(args.teams_file).read_text().splitlines()
        team_paths.extend([line.strip() for line in lines if line.strip()])
    return team_paths


def main() -> None:
    parser = _parser()
    args = parser.parse_args()

    team_paths = _resolve_team_paths(args)
    if not team_paths:
        parser.error("At least one --team or --teams-file path is required")

    if args.dry_run:
        print("Dry-run successful")
        print(f"Team inputs: {len(team_paths)}")
        return

    config = load_config(args.config)
    result = run_protocol(
        team_paths=team_paths,
        config=config,
        trigger=args.trigger,
        output_root=args.output_root,
        allow_degraded=args.allow_degraded,
    )

    print("Run complete")
    print(f"Run dir: {result['run_dir']}")
    print(f"Report: {result['report']}")


if __name__ == "__main__":
    main()
