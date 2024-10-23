from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import datetime, time, timedelta

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from google.oauth2 import service_account
from googleapiclient.discovery import build

from calc_working_time import calculate_working_time
from models.google_sheet import GoogleSheetService

scheduler = BackgroundScheduler()

sydney_tz = pytz.timezone("Australia/Sydney")
google_sheet_service = GoogleSheetService()


def crawl_google_calendar_data():
    SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
    SERVICE_ACCOUNT_FILE = "/Users/minhdg241/Documents/minh.json"

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    calendar_id = "d.baminh@gmail.com"
    now = sydney_tz.localize(
        datetime.combine(datetime.now(sydney_tz).date(), time(0, 0, 0))
    ).isoformat()
    then = sydney_tz.localize(
        datetime.combine(
            datetime.now(sydney_tz).date() + timedelta(days=1), time(0, 0, 0)
        )
    ).isoformat()
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
