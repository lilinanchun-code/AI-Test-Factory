from __future__ import annotations

import argparse
from pathlib import Path

from .generator import generate_artifacts
from .parser import parse_scenario_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate automotive testing artifacts from scenario text.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="Path to a UTF-8 scenario text file.")
    source.add_argument("--text", help="Scenario text passed directly from command line.")
    parser.add_argument("--output", type=Path, default=Path("outputs/demo"), help="Output directory.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.input:
        text = args.input.read_text(encoding="utf-8")
    else:
        text = args.text

    scenario = parse_scenario_text(text)
    artifacts = generate_artifacts(scenario)
    artifacts.write_to(args.output)

    print(f"Generated artifacts for: {scenario.topic}")
    print(f"Output directory: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
