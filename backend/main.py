from __future__ import annotations

from typing import Dict, List

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from stravalib.model import SummaryActivity

from backend.services.strava_client import StravaClient
from backend.services.supabase_client import SupabaseClient

app = FastAPI()
strava_client = StravaClient()
supabase_client = SupabaseClient()

# Add these to your .env file
REDIRECT_URI = "http://localhost:8000/api/strava/callback"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/strava/authorize")
def authorize_strava(scopes: str = "read,activity:read"):
    """Start the OAuth flow with specified scopes"""
    from stravalib.client import Client

    client = Client()
    auth_url = client.authorization_url(
        client_id=strava_client.CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        scope=scopes.split(","),
    )
    return RedirectResponse(url=auth_url)


@app.get("/api/strava/activities")
def get_activities():
    activities = supabase_client.read_json("activities.json")
    return activities


@app.get("/api/strava/activities:download")
def download_activities():
    try:
        activities: List[SummaryActivity] = strava_client.get_activities()
        activities_data: List[Dict] = [activity.model_dump() for activity in activities]
        supabase_client.upload_json(activities_data, "activities.json")
        return {"message": len(activities)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
