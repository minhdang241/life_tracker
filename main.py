from __future__ import annotations

from collections import defaultdict
from contextlib import asynccontextmanager
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from google.oauth2 import service_account
from googleapiclient.discovery import build

from calc_working_time import calculate_working_time

scheduler = BackgroundScheduler()


def crawl_google_calendar_data():
    SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
    SERVICE_ACCOUNT_FILE = "/Users/minhdg241/Documents/minh.json"

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    events = service.events().list(calendarId="d.baminh@gmail.com").execute()
    print(f"events: ", events)
    for event in events["items"]:
        print(event["summary"])
    print(f"Task executed at {datetime.now()}")
    data = defaultdict(list)
    return data


def calculate_working_hours():
    data = crawl_google_calendar_data()
    print(f"Working hours: {calculate_working_time(data)}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    scheduler.add_job(calculate_working_hours, "interval", seconds=5)
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "FastAPI with scheduled tasks"}
