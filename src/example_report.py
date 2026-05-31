import argparse
from pathlib import Path
from typing import Iterable, List, Optional

from src.output import OutputFormatter
from src.solver_engine import BeamSearchSolver
from src.validation import RequestParser


def _default_output_path(example_path: Path) -> Path:
    return Path("docs") / f"{example_path.stem}-report.md"


def _resolve_example_paths(example_paths: Iterable[str], all_examples: bool) -> List[Path]:
    if all_examples:
        return sorted(Path("examples").glob("*.yaml"))
    return [Path(path) for path in example_paths]


def generate_report_for_example(
    example_path: Path,
    output_path: Optional[Path] = None,
    system_defaults_path: str = "config/defaults.yaml",
    cache_db_path: str = ".g2l4a_cache.db",
    max_alternatives: Optional[int] = None,
) -> Path:
    """Parse one YAML request, solve it, and persist a markdown comparison report."""
    parser = RequestParser(system_defaults_path=system_defaults_path)
    itinerary, config = parser.parse_request_file(str(example_path))

    effective_max_alternatives = max_alternatives
    if effective_max_alternatives is None:
        effective_max_alternatives = int(config.get("output", {}).get("alternatives_count", 4))

    run_config = dict(config)
    run_config["max_alternatives"] = effective_max_alternatives

    solver = BeamSearchSolver(cache_db_path)
    try:
        itineraries = solver.solve(itinerary, run_config)
    finally:
        solver.close()

    if not itineraries:
        raise RuntimeError(f"No recommendations were generated for {example_path}.")

    markdown = OutputFormatter.format_recommendations_markdown(itineraries)

    final_output_path = output_path if output_path is not None else _default_output_path(example_path)
    final_output_path.parent.mkdir(parents=True, exist_ok=True)
    final_output_path.write_text(markdown + "\n", encoding="utf-8")
    return final_output_path


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate markdown itinerary recommendation reports from example YAML configurations."
    )
    parser.add_argument(
        "examples",
        nargs="*",
        help="One or more example YAML files (for example: examples/us-capitals-fixed-date.yaml).",
    )
    parser.add_argument(
        "--all-examples",
        action="store_true",
        help="Generate reports for all .yaml files in examples/.",
    )
    parser.add_argument(
        "--output",
        help="Optional output path. Allowed only when a single example is processed.",
    )
    parser.add_argument(
        "--cache-db",
        default=".g2l4a_cache.db",
        help="SQLite cache file path used by the solver.",
    )
    parser.add_argument(
        "--max-alternatives",
        type=int,
        help="Override maximum number of alternative itineraries in addition to the best recommendation.",
    )
    return parser


def main() -> int:
    parser = build_argument_parser()
    args = parser.parse_args()

    if not args.examples and not args.all_examples:
        parser.error("Provide at least one example path or use --all-examples.")

    if args.max_alternatives is not None and args.max_alternatives < 0:
        parser.error("--max-alternatives must be >= 0.")

    resolved_examples = _resolve_example_paths(args.examples, args.all_examples)
    if not resolved_examples:
        parser.error("No example YAML files were found.")

    if args.output and len(resolved_examples) != 1:
        parser.error("--output can only be used when processing a single example file.")

    generated_paths: List[Path] = []
    for example_path in resolved_examples:
        output_path = Path(args.output) if args.output else None
        written = generate_report_for_example(
            example_path=example_path,
            output_path=output_path,
            cache_db_path=args.cache_db,
            max_alternatives=args.max_alternatives,
        )
        generated_paths.append(written)

    for path in generated_paths:
        print(f"Generated: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())