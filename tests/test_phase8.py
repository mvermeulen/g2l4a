import json
import sys
from pathlib import Path

import src.example_report as example_report
from src.example_report import (
    _apply_data_attribution,
    _build_data_attribution,
    _default_json_output_path,
    _default_output_path,
    _default_txt_output_path,
    build_argument_parser,
    generate_report_for_example,
)
from src.output import OutputFormatter


def test_default_output_path_uses_docs_and_stem():
    out = _default_output_path(Path("examples/us-capitals-fixed-date.yaml"))
    assert str(out) == "docs/us-capitals-fixed-date-report.md"


def test_default_json_output_path_uses_docs_and_stem():
    out = _default_json_output_path(Path("examples/us-capitals-fixed-date.yaml"))
    assert str(out) == "docs/us-capitals-fixed-date-report.json"


def test_default_txt_output_path_uses_docs_and_stem():
    out = _default_txt_output_path(Path("examples/us-capitals-fixed-date.yaml"))
    assert str(out) == "docs/us-capitals-fixed-date-report.txt"


def test_generate_report_for_example_writes_markdown(tmp_path):
    example_yaml = tmp_path / "tiny-example.yaml"
    example_yaml.write_text(
        "\n".join(
            [
                "scenario_name: Tiny Example",
                "start_city: Austin, Texas",
                "completion_city: Washington, DC",
                'start_date: "2026-02-01"',
                "via_cities:",
                "  - Oklahoma City, Oklahoma",
                "weather_constraints:",
                "  max_avg_high_f: 95",
                "  min_avg_low_f: 20",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    output_md = tmp_path / "tiny-example-report.md"
    written = generate_report_for_example(
        example_path=example_yaml,
        output_path=output_md,
        cache_db_path=str(tmp_path / "test-cache.db"),
        max_alternatives=1,
    )

    assert written == output_md
    content = output_md.read_text(encoding="utf-8")
    assert "# Route Recommendations Comparison" in content
    assert "## Overview Comparison" in content
    assert "Best Recommendation" in content


def test_generate_report_for_example_writes_json(tmp_path):
    example_yaml = tmp_path / "tiny-example.yaml"
    example_yaml.write_text(
        "\n".join(
            [
                "scenario_name: Tiny Example",
                "start_city: Austin, Texas",
                "completion_city: Washington, DC",
                'start_date: "2026-02-01"',
                "via_cities:",
                "  - Oklahoma City, Oklahoma",
                "weather_constraints:",
                "  max_avg_high_f: 95",
                "  min_avg_low_f: 20",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    output_md = tmp_path / "tiny-example-report.md"
    output_json = tmp_path / "tiny-example-report.json"
    written = generate_report_for_example(
        example_path=example_yaml,
        output_path=output_md,
        json_output_path=output_json,
        cache_db_path=str(tmp_path / "test-cache.db"),
        max_alternatives=1,
    )

    assert written == output_md
    assert output_json.exists()
    payload = json.loads(output_json.read_text(encoding="utf-8"))
    assert "recommendations" in payload
    assert len(payload["recommendations"]) >= 1


def test_generate_report_for_example_writes_txt_with_aligned_table(tmp_path):
    example_yaml = tmp_path / "tiny-example.yaml"
    example_yaml.write_text(
        "\n".join(
            [
                "scenario_name: Tiny Example",
                "start_city: Austin, Texas",
                "completion_city: Washington, DC",
                'start_date: "2026-02-01"',
                "via_cities:",
                "  - Oklahoma City, Oklahoma",
                "weather_constraints:",
                "  max_avg_high_f: 95",
                "  min_avg_low_f: 20",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    output_txt = tmp_path / "tiny-example-report.txt"
    written = generate_report_for_example(
        example_path=example_yaml,
        txt_output_path=output_txt,
        cache_db_path=str(tmp_path / "test-cache.db"),
        max_alternatives=1,
    )

    assert written == output_txt
    content = output_txt.read_text(encoding="utf-8")
    assert "+-" in content
    assert "| Option" in content
    assert "Best Recommendation" in content


def test_apply_data_attribution_for_open_meteo():
    base_md = "# Route Recommendations Comparison\n"
    cfg = {"weather_provider": {"name": "open_meteo"}}
    out = _apply_data_attribution(base_md, cfg)
    assert "## Data Attribution" in out
    assert "https://open-meteo.com/" in out
    assert "https://creativecommons.org/licenses/by/4.0/" in out


def test_apply_data_attribution_for_non_open_meteo():
    base_md = "# Route Recommendations Comparison\n"
    cfg = {"weather_provider": {"name": "mock"}}
    out = _apply_data_attribution(base_md, cfg)
    assert out == base_md


def test_build_data_attribution_for_open_meteo():
    cfg = {"weather_provider": {"name": "open_meteo"}}
    data = _build_data_attribution(cfg)
    assert data is not None
    assert data["provider"] == "Open-Meteo"
    assert data["provider_url"] == "https://open-meteo.com/"


def test_build_data_attribution_for_non_open_meteo():
    cfg = {"weather_provider": {"name": "mock"}}
    data = _build_data_attribution(cfg)
    assert data is None


def test_build_argument_parser_supports_format_option():
    parser = build_argument_parser()
    args = parser.parse_args(["examples/us-capitals-fixed-date.yaml", "--format", "both"])
    assert args.format == "both"


def test_build_argument_parser_supports_txt_format_option():
    parser = build_argument_parser()
    args = parser.parse_args(["examples/us-capitals-fixed-date.yaml", "--format", "txt"])
    assert args.format == "txt"


def test_main_with_format_both_writes_markdown_and_json(monkeypatch):
    captured: dict = {}

    def fake_generate_report_for_example(**kwargs):
        captured["output_path"] = kwargs.get("output_path")
        captured["json_output_path"] = kwargs.get("json_output_path")
        return kwargs.get("output_path") or kwargs.get("json_output_path")

    monkeypatch.setattr(example_report, "generate_report_for_example", fake_generate_report_for_example)
    monkeypatch.setattr(
        example_report,
        "_resolve_example_paths",
        lambda example_paths, all_examples: [Path("examples/us-capitals-fixed-date.yaml")],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "example_report",
            "examples/us-capitals-fixed-date.yaml",
            "--format",
            "both",
        ],
    )

    exit_code = example_report.main()

    assert exit_code == 0
    assert captured["output_path"] == Path("docs/us-capitals-fixed-date-report.md")
    assert captured["json_output_path"] == Path("docs/us-capitals-fixed-date-report.json")


def test_main_with_format_json_writes_only_json(monkeypatch):
    captured: dict = {}

    def fake_generate_report_for_example(**kwargs):
        captured["output_path"] = kwargs.get("output_path")
        captured["json_output_path"] = kwargs.get("json_output_path")
        return kwargs.get("json_output_path")

    monkeypatch.setattr(example_report, "generate_report_for_example", fake_generate_report_for_example)
    monkeypatch.setattr(
        example_report,
        "_resolve_example_paths",
        lambda example_paths, all_examples: [Path("examples/us-capitals-fixed-date.yaml")],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "example_report",
            "examples/us-capitals-fixed-date.yaml",
            "--format",
            "json",
        ],
    )

    exit_code = example_report.main()

    assert exit_code == 0
    assert captured["output_path"] is None
    assert captured["json_output_path"] == Path("docs/us-capitals-fixed-date-report.json")


def test_main_with_format_txt_writes_only_txt(monkeypatch):
    captured: dict = {}

    def fake_generate_report_for_example(**kwargs):
        captured["output_path"] = kwargs.get("output_path")
        captured["json_output_path"] = kwargs.get("json_output_path")
        captured["txt_output_path"] = kwargs.get("txt_output_path")
        return kwargs.get("txt_output_path")

    monkeypatch.setattr(example_report, "generate_report_for_example", fake_generate_report_for_example)
    monkeypatch.setattr(
        example_report,
        "_resolve_example_paths",
        lambda example_paths, all_examples: [Path("examples/us-capitals-fixed-date.yaml")],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "example_report",
            "examples/us-capitals-fixed-date.yaml",
            "--format",
            "txt",
        ],
    )

    exit_code = example_report.main()

    assert exit_code == 0
    assert captured["output_path"] is None
    assert captured["json_output_path"] is None
    assert captured["txt_output_path"] == Path("docs/us-capitals-fixed-date-report.txt")


def test_markdown_to_aligned_text_formats_pipe_tables():
    markdown = "\n".join(
        [
            "| A | BBB |",
            "|---|---|",
            "| 1 | x |",
            "| 22 | yy |",
        ]
    )

    rendered = OutputFormatter.markdown_to_aligned_text(markdown)
    assert "+----" in rendered
    assert "| A  | BBB |" in rendered
    assert "| 22 | yy  |" in rendered