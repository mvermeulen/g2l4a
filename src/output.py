import json
from typing import List, Dict, Any, Optional
from src.domain import Itinerary

class OutputFormatter:
    """Handles structured human-readable and JSON output serialization for route recommendations."""

    @staticmethod
    def _is_markdown_table_delimiter(line: str) -> bool:
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            return False

        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not cells:
            return False

        for cell in cells:
            if not cell:
                return False
            if any(ch not in "-: " for ch in cell):
                return False
            if "-" not in cell:
                return False
        return True

    @staticmethod
    def _parse_markdown_table_row(line: str) -> List[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    @staticmethod
    def _render_ascii_table(headers: List[str], rows: List[List[str]]) -> List[str]:
        all_rows = [headers] + rows
        widths = [max(len(row[col]) for row in all_rows) for col in range(len(headers))]

        def border() -> str:
            return "+-" + "-+-".join("-" * w for w in widths) + "-+"

        def render_row(row: List[str]) -> str:
            return "| " + " | ".join(row[i].ljust(widths[i]) for i in range(len(widths))) + " |"

        lines = [border(), render_row(headers), border()]
        lines.extend(render_row(row) for row in rows)
        lines.append(border())
        return lines

    @staticmethod
    def markdown_to_aligned_text(markdown: str) -> str:
        """Converts markdown tables to fixed-width ASCII tables for plain-text reports."""
        in_lines = markdown.splitlines()
        out_lines: List[str] = []
        i = 0

        while i < len(in_lines):
            line = in_lines[i]
            if (
                line.strip().startswith("|")
                and line.strip().endswith("|")
                and i + 1 < len(in_lines)
                and OutputFormatter._is_markdown_table_delimiter(in_lines[i + 1])
            ):
                headers = OutputFormatter._parse_markdown_table_row(line)
                j = i + 2
                rows: List[List[str]] = []
                while j < len(in_lines):
                    candidate = in_lines[j].strip()
                    if not (candidate.startswith("|") and candidate.endswith("|")):
                        break
                    row = OutputFormatter._parse_markdown_table_row(in_lines[j])
                    if len(row) < len(headers):
                        row.extend([""] * (len(headers) - len(row)))
                    elif len(row) > len(headers):
                        row = row[: len(headers)]
                    rows.append(row)
                    j += 1

                out_lines.extend(OutputFormatter._render_ascii_table(headers, rows))
                i = j
                continue

            out_lines.append(line)
            i += 1

        return "\n".join(out_lines)
    
    @staticmethod
    def format_schedule_markdown(itinerary: Itinerary) -> str:
        """Formats an itinerary's daily schedule into a markdown table."""
        if not itinerary.is_feasible:
            return "ROUTE INFEASIBLE\n"
        if not itinerary.schedule:
            return "No travel schedule generated.\n"
            
        lines = []
        lines.append("| Day | Date | Origin | Destination | Distance (mi) | Ascent (ft) | Weather Context | Notes |")
        lines.append("|---|---|---|---|---|---|---|---|")
        
        for i, item in enumerate(itinerary.schedule):
            weather_str = f"Avg High: {item.high_temp_f}°F, Low: {item.low_temp_f}°F"
            notes = ""
            origin_name = item.origin.name
            destination_name = item.destination.name
            
            if item.is_rest_day:
                notes = "Rest Day"
            else:
                is_last_day_of_leg = True
                if i < len(itinerary.schedule) - 1:
                    next_item = itinerary.schedule[i + 1]
                    if next_item.origin.name == item.origin.name and next_item.destination.name == item.destination.name:
                        is_last_day_of_leg = False
                
                # Count consecutive matching transit days for this specific leg
                matching_days = [d for d in itinerary.schedule if d.origin.name == item.origin.name and d.destination.name == item.destination.name and not d.is_rest_day]
                if len(matching_days) > 1:
                    curr_idx = matching_days.index(item) + 1
                    if is_last_day_of_leg:
                        notes = f"Arrived (Day {curr_idx} of {len(matching_days)})"
                        origin_name = f"In Transit (from {item.origin.name})"
                    else:
                        notes = f"Transit (Day {curr_idx} of {len(matching_days)})"
                        if curr_idx == 1:
                            destination_name = f"In Transit (to {item.destination.name})"
                        else:
                            origin_name = f"In Transit (from {item.origin.name})"
                            destination_name = f"In Transit (to {item.destination.name})"
            
            lines.append(
                f"| {item.day_number} | {item.date} | {origin_name} | {destination_name} | "
                f"{item.distance_miles:.1f} | {item.ascent_feet:.0f} | {weather_str} | {notes} |"
            )
            
        return "\n".join(lines)

    @staticmethod
    def format_summary_markdown(itinerary: Itinerary) -> str:
        """Formats the overall itinerary score and metrics summary."""
        lines = []
        lines.append(f"**Feasible**: {'Yes' if itinerary.is_feasible else 'No ❌'}")
        
        total_dist = sum(leg.distance_miles for leg in itinerary.legs)
        if total_dist <= 0:
            total_dist = sum(day.distance_miles for day in itinerary.schedule)
            
        total_climb = sum(leg.ascent_feet for leg in itinerary.legs)
        if total_climb <= 0:
            total_climb = sum(day.ascent_feet for day in itinerary.schedule)

        start_date_str = itinerary.start_date.isoformat() if itinerary.start_date else "N/A"
        lines.append(f"- **Start Date**: {start_date_str}")
        lines.append(f"- **Total Distance**: {total_dist:.1f} miles")
        lines.append(f"- **Total Climbing**: {total_climb:.0f} ft")
        
        if itinerary.is_feasible and itinerary.scores:
            lines.append(f"- **Desirability Scores**:")
            lines.append(f"  - Weather Preference: {itinerary.scores.weather:.3f}")
            lines.append(f"  - Distance Score: {itinerary.scores.distance:.3f}")
            lines.append(f"  - Climbing Score: {itinerary.scores.hills:.3f}")
            lines.append(f"  - **Total Desirability Score**: {itinerary.scores.total:.3f}")
        else:
            lines.append("- **Violated Constraints**:")
            for violation in itinerary.violation_details:
                lines.append(
                    f"  - [{violation.get('code')}] at {violation.get('location')} on {violation.get('date')}: "
                    f"observed {violation.get('observed_value')} vs threshold {violation.get('threshold_limit')}. "
                    f"Hint: {violation.get('remediation_hint')}"
                )
        return "\n".join(lines)

    @staticmethod
    def _compute_key_difference(current: Itinerary, best: Itinerary) -> str:
        """Determines a succinct description of why the itinerary differs from the best recommendation."""
        if current is best:
            return "Baseline / Optimal Route"
            
        date_diff = False
        if current.start_date != best.start_date:
            date_diff = True
            
        # Check order of via cities
        curr_sequence = [c.name for c in current.via_cities]
        best_sequence = [c.name for c in best.via_cities]
        order_diff = (curr_sequence != best_sequence)
        
        if date_diff and order_diff:
            date_str = current.start_date.isoformat() if current.start_date else "N/A"
            return f"Different start date ({date_str}) & alternative sequence"
        elif date_diff:
            date_str = current.start_date.isoformat() if current.start_date else "N/A"
            return f"Different start date ({date_str}), same sequence"
        elif order_diff:
            return "Alternative via-city sequence, same date"
        else:
            return "Alternative metrics/scores, same date & sequence"

    @staticmethod
    def format_recommendations_markdown(itineraries: List[Itinerary], metrics: Any = None) -> str:
        """Formats the complete list of ranked itineraries and metrics into a comparison document."""
        if not itineraries:
            return "# No Recommendations Found\n"
            
        lines = []
        lines.append("# Route Recommendations Comparison\n")
        
        # 1. Comparison Header Table
        lines.append("## Overview Comparison")
        lines.append("| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Total Climb | Key Difference |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        
        best_it = itineraries[0]
        for idx, it in enumerate(itineraries):
            name = "**Best Recommendation**" if idx == 0 else f"Alternative {idx}"
            feasible_str = "Yes" if it.is_feasible else "No ❌"
            start_date_str = it.start_date.isoformat() if it.start_date else "N/A"
            key_diff = OutputFormatter._compute_key_difference(it, best_it)
            
            # Scores & metrics
            if it.is_feasible and it.scores:
                sc_total = f"{it.scores.total:.4f}"
                sc_weather = f"{it.scores.weather:.4f}"
                sc_dist = f"{it.scores.distance:.4f}"
                sc_hills = f"{it.scores.hills:.4f}"
            else:
                sc_total = "N/A"
                sc_weather = "N/A"
                sc_dist = "N/A"
                sc_hills = "N/A"
                
            total_dist = sum(leg.distance_miles for leg in it.legs)
            if total_dist <= 0:
                total_dist = sum(day.distance_miles for day in it.schedule)
                
            total_climb = sum(leg.ascent_feet for leg in it.legs)
            if total_climb <= 0:
                total_climb = sum(day.ascent_feet for day in it.schedule)
                
            lines.append(
                f"| {name} | {start_date_str} | {feasible_str} | {sc_total} | {sc_weather} | {sc_dist} | {sc_hills} | "
                f"{total_dist:.1f} mi | {total_climb:.0f} ft | {key_diff} |"
            )
        lines.append("")
        
        # 2. Section for each Itinerary with Collapsible schedule
        lines.append("## Detailed Recommendations")
        for idx, it in enumerate(itineraries):
            name = "Best Recommendation" if idx == 0 else f"Alternative {idx}"
            lines.append(f"### {name}")
            lines.append(OutputFormatter.format_summary_markdown(it))
            lines.append("")
            
            lines.append("<details>")
            lines.append("<summary>Click to view daily travel schedule</summary>")
            lines.append("")
            lines.append(OutputFormatter.format_schedule_markdown(it))
            lines.append("")
            lines.append("</details>")
            lines.append("")
            lines.append("---")
            lines.append("")
            
        # 3. Solver Performance Metrics
        if metrics:
            metrics_dict = metrics.to_dict() if hasattr(metrics, "to_dict") else metrics
            lines.append("## Solver Execution Performance")
            lines.append(f"- **Execution Duration**: {metrics_dict.get('duration_ms', 0.0):.1f} ms")
            lines.append(f"- **Evaluated Candidates**: {metrics_dict.get('evaluated_permutations', 0)}")
            lines.append(f"- **Pruned Branches**: {metrics_dict.get('pruned_branches', 0)}")
            lines.append(f"- **Cache Hit Rate**: {metrics_dict.get('cache_hit_rate', 0.0) * 100.0:.1f}%")
            lines.append("")
            
        return "\n".join(lines)

    @staticmethod
    def serialize_json(itinerary: Itinerary, data_attribution: Optional[Dict[str, Any]] = None) -> str:
        """Serializes a single itinerary including schedule details to a JSON string."""
        data = {
            "is_feasible": itinerary.is_feasible,
            "start_city": itinerary.start_city.name,
            "completion_city": itinerary.completion_city.name,
            "via_cities": [c.name for c in itinerary.via_cities],
            "start_date": itinerary.start_date.isoformat() if itinerary.start_date else None,
            "scores": {
                "weather": itinerary.scores.weather if itinerary.is_feasible and itinerary.scores else None,
                "distance": itinerary.scores.distance if itinerary.is_feasible and itinerary.scores else None,
                "hills": itinerary.scores.hills if itinerary.is_feasible and itinerary.scores else None,
                "total": itinerary.scores.total if itinerary.is_feasible and itinerary.scores else None,
            },
            "legs": [
                {
                    "origin": leg.origin.name,
                    "destination": leg.destination.name,
                    "distance_miles": leg.distance_miles,
                    "ascent_feet": leg.ascent_feet,
                } for leg in itinerary.legs
            ],
            "schedule": [
                {
                    "day_number": item.day_number,
                    "date": item.date.isoformat(),
                    "origin": item.origin.name,
                    "destination": item.destination.name,
                    "distance_miles": item.distance_miles,
                    "ascent_feet": item.ascent_feet,
                    "high_temp_f": item.high_temp_f,
                    "low_temp_f": item.low_temp_f,
                    "is_rest_day": item.is_rest_day
                } for item in itinerary.schedule
            ],
            "violations": itinerary.violation_details,
        }
        if data_attribution:
            data["data_attribution"] = data_attribution
        return json.dumps(data, indent=2)

    @staticmethod
    def serialize_recommendations_json(
        itineraries: List[Itinerary],
        metrics: Any = None,
        data_attribution: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Serializes the complete list of ranked itineraries and metrics to a structured JSON payload."""
        recommendations = []
        for it in itineraries:
            it_data = {
                "is_feasible": it.is_feasible,
                "start_city": it.start_city.name,
                "completion_city": it.completion_city.name,
                "via_cities": [c.name for c in it.via_cities],
                "start_date": it.start_date.isoformat() if it.start_date else None,
                "scores": {
                    "weather": it.scores.weather if it.is_feasible and it.scores else None,
                    "distance": it.scores.distance if it.is_feasible and it.scores else None,
                    "hills": it.scores.hills if it.is_feasible and it.scores else None,
                    "total": it.scores.total if it.is_feasible and it.scores else None,
                },
                "legs": [
                    {
                        "origin": leg.origin.name,
                        "destination": leg.destination.name,
                        "distance_miles": leg.distance_miles,
                        "ascent_feet": leg.ascent_feet,
                    } for leg in it.legs
                ],
                "schedule": [
                    {
                        "day_number": item.day_number,
                        "date": item.date.isoformat(),
                        "origin": item.origin.name,
                        "destination": item.destination.name,
                        "distance_miles": item.distance_miles,
                        "ascent_feet": item.ascent_feet,
                        "high_temp_f": item.high_temp_f,
                        "low_temp_f": item.low_temp_f,
                        "is_rest_day": item.is_rest_day
                    } for item in it.schedule
                ],
                "violations": it.violation_details
            }
            recommendations.append(it_data)
            
        payload = {
            "solver_metrics": metrics.to_dict() if hasattr(metrics, "to_dict") else metrics,
            "recommendations": recommendations
        }
        if data_attribution:
            payload["data_attribution"] = data_attribution
        return json.dumps(payload, indent=2)
