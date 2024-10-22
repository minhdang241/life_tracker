from __future__ import annotations

import json
from datetime import datetime


def calculate_working_time(data: dict) -> float:
    total_duration = 0
    for event in data["items"]:
        if event.get("colorId") == "2":
            start_time = datetime.fromisoformat(event["start"]["dateTime"])
            end_time = datetime.fromisoformat(event["end"]["dateTime"])
            duration = (
                end_time - start_time
            ).total_seconds() / 3600  # Convert seconds to hours
            total_duration += duration

    print(f"Total time spent on events with colorId = 2: {total_duration} hours")
    return total_duration
