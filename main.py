from __future__ import annotations

import os
from contextlib import asynccontextmanager
from datetime import datetime, time, timedelta

from dotenv import load_dotenv

load_dotenv()

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from google.oauth2 import service_account
from googleapiclient.discovery import build

from calc_working_time import calculate_working_time
from models.google_sheet import GoogleSheetService, dates2ranges

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

    # Get today's date in Sydney timezone
    today = datetime.now(sydney_tz).date()

    # Calculate last Monday (start of last week)
    days_since_monday = today.weekday()  # Monday is 0, Sunday is 6
    last_monday = today - timedelta(days=days_since_monday + 7)

    # Calculate last Sunday (end of last week)
    last_sunday = last_monday + timedelta(days=6)

    # Set time to start of Monday (00:00:00)
    now = sydney_tz.localize(datetime.combine(last_monday, time(0, 0, 0))).isoformat()

    # Set time to end of Sunday (23:59:59)
    then = sydney_tz.localize(
        datetime.combine(last_sunday, time(23, 59, 59))
    ).isoformat()

    print(f"Fetching events from {last_monday} to {last_sunday}")

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
    today = datetime.now(sydney_tz).strftime("%A")
    # week_number = datetime.now(sydney_tz).isocalendar()[1]
    # ranges = f"Sheet1!{dates2ranges(today, week_number)}"
    # google_sheet_service.write(ranges, [[total_duration]])
    print(f"Total time spent on [WORK] events: {total_duration} hours")


if __name__ == "__main__":
    calculate_working_hours()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
# scheduler.start()
# scheduler.add_job(calculate_working_hours, "interval", seconds=3)
# yield
# scheduler.shutdown()


# app = FastAPI(lifespan=lifespan)
#

# @app.get("/")
# def read_root():
# return {"message": "FastAPI with scheduled tasks"}
