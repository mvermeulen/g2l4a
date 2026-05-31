from pathlib import Path

from src.example_report import _default_output_path, generate_report_for_example


def test_default_output_path_uses_docs_and_stem():
    out = _default_output_path(Path("examples/us-capitals-fixed-date.yaml"))
    assert str(out) == "docs/us-capitals-fixed-date-report.md"


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
                "  min_avg_high_f: 20",
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