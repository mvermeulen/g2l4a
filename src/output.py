import json
from typing import List, Dict, Any
from src.domain import Itinerary

class OutputFormatter:
    """Scaffolds human-readable and structured output serialization for itineraries."""
    
    @staticmethod
    def format_schedule_markdown(itinerary: Itinerary) -> str:
        """Formats an itinerary's daily schedule into a markdown table."""
        if not itinerary.is_feasible:
            return "ROUTE INFEASIBLE\n"
            
        lines = []
        lines.append("| Day | Date | Origin | Destination | Distance (mi) | Ascent (ft) | Weather Context | Notes |")
        lines.append("|---|---|---|---|---|---|---|---|")
        
        for item in itinerary.schedule:
            weather_str = f"Avg High: {item.high_temp_f}°F, Low: {item.low_temp_f}°F"
            notes = "Rest Day" if item.is_rest_day else ""
            lines.append(
                f"| {item.day_number} | {item.date} | {item.origin.name} | {item.destination.name} | "
                f"{item.distance_miles:.1f} | {item.ascent_feet:.0f} | {weather_str} | {notes} |"
            )
            
        return "\n".join(lines)

    @staticmethod
    def format_summary_markdown(itinerary: Itinerary) -> str:
        """Formats the overall itinerary score and metrics summary."""
        lines = []
        lines.append(f"### Itinerary Summary (Feasible: {itinerary.is_feasible})")
        if itinerary.is_feasible:
            total_dist = sum(leg.distance_miles for leg in itinerary.legs)
            total_climb = sum(leg.ascent_feet for leg in itinerary.legs)
            lines.append(f"- **Total Distance**: {total_dist:.1f} miles")
            lines.append(f"- **Total Climbing**: {total_climb:.0f} ft")
            lines.append(f"- **Desirability Scores**:")
            lines.append(f"  - Weather Preference: {itinerary.scores.weather:.3f}")
            lines.append(f"  - Distance Score: {itinerary.scores.distance:.3f}")
            lines.append(f"  - Climbing Score: {itinerary.scores.hills:.3f}")
            lines.append(f"  - **Total Desirability Score**: {itinerary.scores.total:.3f}")
        else:
            lines.append("Violated Constraints:")
            for violation in itinerary.violation_details:
                lines.append(
                    f"- [{violation.get('code')}] at {violation.get('location')} on {violation.get('date')}: "
                    f"observed {violation.get('observed_value')} vs threshold {violation.get('threshold_limit')}. "
                    f"Hint: {violation.get('remediation_hint')}"
                )
        return "\n".join(lines)

    @staticmethod
    def serialize_json(itinerary: Itinerary) -> str:
        """Serializes the complete itinerary structure to a structured JSON string."""
        data = {
            "is_feasible": itinerary.is_feasible,
            "start_city": itinerary.start_city.name,
            "completion_city": itinerary.completion_city.name,
            "via_cities": [c.name for c in itinerary.via_cities],
            "scores": {
                "weather": itinerary.scores.weather,
                "distance": itinerary.scores.distance,
                "hills": itinerary.scores.hills,
                "total": itinerary.scores.total,
            },
            "legs": [
                {
                    "origin": leg.origin.name,
                    "destination": leg.destination.name,
                    "distance_miles": leg.distance_miles,
                    "ascent_feet": leg.ascent_feet,
                } for leg in itinerary.legs
            ],
            "violations": itinerary.violation_details,
        }
        return json.dumps(data, indent=2)
