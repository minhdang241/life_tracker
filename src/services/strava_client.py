from __future__ import annotations

import json
from datetime import datetime
from typing import Dict, List

from dotenv import load_dotenv
from stravalib.client import Client
from stravalib.model import SummaryActivity

load_dotenv()


class StravaClient:
    def __init__(self):
        with open("src/services/strava_secret.json", "r") as f:
            secret = json.load(f)
            self.client = Client(
                access_token=secret["access_token"],
                refresh_token=secret["refresh_token"],
                token_expires=secret["expires_at"],
            )

    def get_activities(self) -> List[Dict]:
        """Get athlete's activities"""
        summary_activities: list[SummaryActivity] = []
        # Iterate over the activities returned by the batched iterator
        for _, activity in enumerate(self.client.get_activities()):
            summary_activities.append(activity)
        return summary_activities
