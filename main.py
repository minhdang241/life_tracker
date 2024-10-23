from __future__ import annotations

import datetime
from collections import defaultdict
from contextlib import asynccontextmanager

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

    calendar_id = "d.baminh@gmail.com"
    now = "2024-10-22T00:00:00+11:00"
    then = "2024-10-23T00:00:00+11:00"
    events = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=now,
            timeMax=then,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    return events


def calculate_working_hours():
    data = crawl_google_calendar_data()
    total_duration = calculate_working_time(data)
    print(f"Total time spent on [WORK] events: {total_duration} hours")


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
