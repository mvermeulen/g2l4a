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
            stripped_line = line.strip()
            if stripped_line == "<details>" or stripped_line == "</details>":
                i += 1
                continue

            if stripped_line.startswith("<summary>") and stripped_line.endswith("</summary>"):
                summary_text = stripped_line[len("<summary>"): -len("</summary>")]
                out_lines.append(f"=== {summary_text} ===")
                i += 1
                continue

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
        lines.append("| Start Date | End Date | Days | Origin | Destination | Distance (mi/day) | Ascent (ft/day) | Leg Distance (mi) | Leg Ascent (ft) | Distance Source | Weather Context | Notes |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")

        distance_source = itinerary.routing_distance_source or "unknown"

        grouped_rows: List[List[Any]] = []

        def flush_group(group: List[Any]) -> None:
            if not group:
                return

            first = group[0]
            last = group[-1]
            days = len(group)
            highs = [day.high_temp_f for day in group]
            lows = [day.low_temp_f for day in group]
            sources = sorted({day.weather_source for day in group})

            if max(highs) == min(highs) and max(lows) == min(lows):
                weather_str = f"Avg High: {highs[0]}°F, Low: {lows[0]}°F ({', '.join(sources)})"
            else:
                weather_str = (
                    f"Avg High: {min(highs)}-{max(highs)}°F, "
                    f"Low: {min(lows)}-{max(lows)}°F ({', '.join(sources)})"
                )

            leg_dist = first.distance_miles * days
            leg_dist_str = f"{leg_dist:.1f}"
            notes_str = ""

            if first.is_rest_day:
                notes_str = f"Rest Day at {first.origin.name}"
                leg_dist_str = "0.0"
            else:
                # Find matching leg to extract surface breakdown
                matching_leg = None
                for leg in itinerary.legs:
                    if leg.origin.name == first.origin.name and leg.destination.name == first.destination.name:
                        matching_leg = leg
                        break

                if matching_leg and matching_leg.surface_breakdown:
                    paved_keys = {'paved', 'asphalt', 'concrete', 'paving_stones', 'cobblestone', 'grade1'}
                    unpaved_keys = {'unpaved', 'compacted', 'fine_gravel', 'gravel', 'ground', 'dirt', 'grass', 'sand', 'grade2', 'grade3', 'grade4', 'grade5'}

                    paved_miles = 0.0
                    gravel_miles = 0.0
                    for k, val in matching_leg.surface_breakdown.items():
                        k_low = k.lower()
                        if k_low in paved_keys:
                            paved_miles += val
                        elif k_low in unpaved_keys:
                            gravel_miles += val
                        else:
                            if any(x in k_low for x in ['gravel', 'dirt', 'sand', 'unpaved', 'ground', 'grass', 'grade', 'compacted']):
                                gravel_miles += val
                            elif any(x in k_low for x in ['paved', 'asphalt', 'concrete', 'stone']):
                                paved_miles += val

                    if paved_miles > 0 or gravel_miles > 0:
                        total_classified = paved_miles + gravel_miles
                        if total_classified > 0:
                            scale = leg_dist / total_classified
                            paved_miles *= scale
                            gravel_miles *= scale

                        parts = []
                        if paved_miles >= 0.05:
                            parts.append(f"{paved_miles:.1f} mi paved")
                        if gravel_miles >= 0.05:
                            parts.append(f"{gravel_miles:.1f} mi gravel")
                        if parts:
                            leg_dist_str = f"{leg_dist:.1f} mi ({', '.join(parts)})"

            grouped_rows.append([
                first.date.strftime('%Y-%m-%d'),
                last.date.strftime('%Y-%m-%d'),
                str(days),
                first.origin.name,
                first.destination.name,
                f"{first.distance_miles:.1f}/day",
                f"{first.ascent_feet:.0f}/day",
                leg_dist_str,
                f"{first.ascent_feet * days:.0f}",
                distance_source,
                weather_str,
                notes_str,
            ])

        current_group: List[Any] = [itinerary.schedule[0]]
        for item in itinerary.schedule[1:]:
            previous = current_group[-1]
            same_leg = (
                previous.origin.name == item.origin.name
                and previous.destination.name == item.destination.name
            )
            if same_leg:
                current_group.append(item)
                continue

            flush_group(current_group)
            current_group = [item]

        flush_group(current_group)

        for row in grouped_rows:
            notes = row[11]
            lines.append(
                f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} | {row[9]} | {row[10]} | {notes} |"
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

        # Aggregate surface breakdown
        total_paved = 0.0
        total_gravel = 0.0
        paved_keys = {'paved', 'asphalt', 'concrete', 'paving_stones', 'cobblestone', 'grade1'}
        unpaved_keys = {'unpaved', 'compacted', 'fine_gravel', 'gravel', 'ground', 'dirt', 'grass', 'sand', 'grade2', 'grade3', 'grade4', 'grade5'}

        for leg in itinerary.legs:
            if leg.surface_breakdown:
                for k, val in leg.surface_breakdown.items():
                    k_low = k.lower()
                    if k_low in paved_keys:
                        total_paved += val
                    elif k_low in unpaved_keys:
                        total_gravel += val
                    else:
                        if any(x in k_low for x in ['gravel', 'dirt', 'sand', 'unpaved', 'ground', 'grass', 'grade', 'compacted']):
                            total_gravel += val
                        elif any(x in k_low for x in ['paved', 'asphalt', 'concrete', 'stone']):
                            total_paved += val

        dist_str = f"{total_dist:.1f} miles"
        if total_paved > 0 or total_gravel > 0:
            total_classified = total_paved + total_gravel
            if total_classified > 0:
                scale = total_dist / total_classified
                total_paved *= scale
                total_gravel *= scale
            parts = []
            if total_paved >= 0.05:
                parts.append(f"{total_paved:.1f} mi paved")
            if total_gravel >= 0.05:
                parts.append(f"{total_gravel:.1f} mi gravel")
            if parts:
                dist_str = f"{total_dist:.1f} miles ({', '.join(parts)})"

        lines.append(f"- **Total Distance**: {dist_str}")
        lines.append(f"- **Distance Source**: {itinerary.routing_distance_source or 'unknown'}")
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
        lines.append("| Option | Start Date | Feasible? | Total Score | Weather Score | Distance Score | Hills Score | Total Distance | Distance Source | Total Climb | Key Difference |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|")
        
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
                f"{total_dist:.1f} mi | {it.routing_distance_source or 'unknown'} | {total_climb:.0f} ft | {key_diff} |"
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
            "routing_distance_source": itinerary.routing_distance_source,
            "legs": [
                {
                    "origin": leg.origin.name,
                    "destination": leg.destination.name,
                    "distance_miles": leg.distance_miles,
                    "ascent_feet": leg.ascent_feet,
                    "distance_source": itinerary.routing_distance_source,
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
                "routing_distance_source": it.routing_distance_source,
                "legs": [
                    {
                        "origin": leg.origin.name,
                        "destination": leg.destination.name,
                        "distance_miles": leg.distance_miles,
                        "ascent_feet": leg.ascent_feet,
                        "distance_source": it.routing_distance_source,
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
