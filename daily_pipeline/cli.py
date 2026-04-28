from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from daily_pipeline.config import load_config
from daily_pipeline.protocol import run_protocol


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run multi-team daily pipeline")

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--team", action="append", default=[], help="Path to team JSON file (repeatable)")
    mode_group.add_argument("--sync", action="store_true", help="Run Stage 9.5 AgentTeams sync across discovered repos")

    parser.add_argument(
        "--teams-file",
        help="Path to text file containing one team JSON path per line",
    )
    parser.add_argument("--config", help="Path to JSON config")
    parser.add_argument("--trigger", default="team-update", choices=["team-create", "team-update"])
    parser.add_argument("--output-root", default="tmp/daily-pipeline")
    parser.add_argument("--allow-degraded", action="store_true")
    parser.add_argument("--dry-run", action="store_true")

    # Stage 9.5 sync options (used only when --sync is active)
    parser.add_argument(
        "--root",
        default=os.environ.get("VK_ROOT", "."),
        help="Root directory to discover sync targets (default: $VK_ROOT or '.')",
    )
    parser.add_argument("--build-team-py", default=None, help="Path to build_team.py executable")
    parser.add_argument("--post-audit", action="store_true", help="Run --post-audit after each AgentTeams sync")

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

    if args.sync:
        _run_sync(args)
        return

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


def _run_sync(args: argparse.Namespace) -> None:
    from daily_pipeline.integration.sync import discover_sync_targets, execute_agentteams_sync

    config = load_config(args.config)
    build_team_py = args.build_team_py or config.build_team_py or None

    targets = discover_sync_targets(args.root)
    if not targets:
        print(f"[warn] No sync targets found under root: {args.root}")
        return

    any_failed = False
    for target in targets:
        result = execute_agentteams_sync(
            target_repo=target,
            build_team_py=build_team_py,
            post_audit=args.post_audit,
            dry_run=args.dry_run,
        )
        suffix = f"  skip_reason={result.skip_reason}" if result.skip_reason else ""
        warning_lines = "  " + "; ".join(result.warnings) if result.warnings else ""
        print(f"[{result.status}] {result.target_repo}{suffix}{warning_lines}")
        if result.status == "failed":
            any_failed = True

    if any_failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
