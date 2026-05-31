import argparse
from pathlib import Path
from typing import Iterable, List, Optional

from src.output import OutputFormatter
from src.solver_engine import BeamSearchSolver
from src.validation import RequestParser


def _default_output_path(example_path: Path) -> Path:
    return Path("reports") / f"{example_path.stem}-report.md"


def _default_json_output_path(example_path: Path) -> Path:
    return Path("reports") / f"{example_path.stem}-report.json"


def _default_txt_output_path(example_path: Path) -> Path:
    return Path("reports") / f"{example_path.stem}-report.txt"


def _resolve_example_paths(example_paths: Iterable[str], all_examples: bool) -> List[Path]:
    if all_examples:
        return sorted(Path("examples").glob("*.yaml"))
    return [Path(path) for path in example_paths]


def _build_data_attribution(config: dict) -> Optional[dict]:
    provider_name = str(config.get("weather_provider", {}).get("name", "mock"))
    if provider_name != "open_meteo":
        return None

    return {
        "provider": "Open-Meteo",
        "provider_url": "https://open-meteo.com/",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "note": "Data has been transformed into itinerary-level schedule summaries.",
    }


def _apply_data_attribution(markdown: str, config: dict) -> str:
    attribution_data = _build_data_attribution(config)
    if not attribution_data:
        return markdown

    attribution = "\n\n## Data Attribution\n"
    attribution += "Weather data by [Open-Meteo.com](https://open-meteo.com/)"
    attribution += " under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)."
    attribution += " Data has been transformed into itinerary-level schedule summaries.\n"
    return markdown.rstrip() + attribution + "\n"


def generate_report_for_example(
    example_path: Path,
    output_path: Optional[Path] = None,
    json_output_path: Optional[Path] = None,
    txt_output_path: Optional[Path] = None,
    system_defaults_path: str = "config/defaults.yaml",
    cache_db_path: str = ".g2l4a_cache.db",
    max_alternatives: Optional[int] = None,
) -> Path:
    """Parse one YAML request, solve it, and persist report outputs."""
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
    markdown = _apply_data_attribution(markdown, config)
    text_payload = OutputFormatter.markdown_to_aligned_text(markdown)
    json_payload = OutputFormatter.serialize_recommendations_json(
        itineraries,
        data_attribution=_build_data_attribution(config),
    )

    final_output_path = output_path if output_path is not None else _default_output_path(example_path)
    if output_path is not None:
        final_output_path.parent.mkdir(parents=True, exist_ok=True)
        final_output_path.write_text(markdown + "\n", encoding="utf-8")

    if json_output_path is not None:
        json_output_path.parent.mkdir(parents=True, exist_ok=True)
        json_output_path.write_text(json_payload + "\n", encoding="utf-8")
    if txt_output_path is not None:
        txt_output_path.parent.mkdir(parents=True, exist_ok=True)
        txt_output_path.write_text(text_payload + "\n", encoding="utf-8")
    if output_path is None and json_output_path is not None:
        return json_output_path
    if output_path is None and txt_output_path is not None:
        return txt_output_path
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
        "--format",
        choices=("md", "txt", "json", "both", "all"),
        default="md",
        help="Output format: md (default), txt, json, both (md+json), or all (md+json+txt).",
    )
    parser.add_argument(
        "--output",
        help="Optional markdown output path (used when --format is md or both). Allowed only for a single example.",
    )
    parser.add_argument(
        "--json-output",
        help="Optional JSON output path (used when --format is json or both). Allowed only for a single example.",
    )
    parser.add_argument(
        "--txt-output",
        help="Optional text output path (used when --format is txt or all). Allowed only for a single example.",
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

    if args.json_output and len(resolved_examples) != 1:
        parser.error("--json-output can only be used when processing a single example file.")

    if args.txt_output and len(resolved_examples) != 1:
        parser.error("--txt-output can only be used when processing a single example file.")

    selected_format = args.format

    generated_paths: List[Path] = []
    generated_json_paths: List[Path] = []
    generated_txt_paths: List[Path] = []
    for example_path in resolved_examples:
        if selected_format in ("json", "txt"):
            output_path = None
        elif args.output:
            output_path = Path(args.output)
        else:
            output_path = _default_output_path(example_path)

        if args.json_output:
            json_output_path = Path(args.json_output)
        elif selected_format in ("json", "both", "all"):
            json_output_path = _default_json_output_path(example_path)
        else:
            json_output_path = None

        if args.txt_output:
            txt_output_path = Path(args.txt_output)
        elif selected_format in ("txt", "all"):
            txt_output_path = _default_txt_output_path(example_path)
        else:
            txt_output_path = None

        written = generate_report_for_example(
            example_path=example_path,
            output_path=output_path,
            json_output_path=json_output_path,
            txt_output_path=txt_output_path,
            cache_db_path=args.cache_db,
            max_alternatives=args.max_alternatives,
        )
        if output_path is not None:
            generated_paths.append(written)
        if json_output_path is not None:
            generated_json_paths.append(json_output_path)
        if txt_output_path is not None:
            generated_txt_paths.append(txt_output_path)

    for path in generated_paths:
        print(f"Generated: {path}")
    for path in generated_json_paths:
        print(f"Generated JSON: {path}")
    for path in generated_txt_paths:
        print(f"Generated TXT: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())