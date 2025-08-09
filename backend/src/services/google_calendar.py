from __future__ import annotations

import json
from datetime import datetime


def calculate_working_time(data: dict) -> float:
    total_duration = 0
    for event in data.get("items", []):
        if event.get("summary").startswith("[WORK]") or event.get("summary").startswith(
            "[Work]"
        ):
            start_time = datetime.fromisoformat(event["start"]["dateTime"])
            end_time = datetime.fromisoformat(event["end"]["dateTime"])
            duration = (
                end_time - start_time
            ).total_seconds() / 3600  # Convert seconds to hours
            total_duration += duration

    return total_duration
