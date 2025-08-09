from __future__ import annotations

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "/Users/minhdg241/Documents/minh.json"
SHEET_ID = "1nSHAxqSRxWhdpAbkNLoO0idbcBFkFBwgqwYBX5l0BTk"

ANCHOR_WEEK = 41


def dates2ranges(today, week_no):
    week_no = int(week_no) - ANCHOR_WEEK
    match today:
        case "Monday":
            return f"A{week_no}:B{week_no}"
        case "Tuesday":
            return f"C{week_no}:D{week_no}"
        case "Wednesday":
            return f"D{week_no}:E{week_no}"
        case "Thursday":
            return f"E{week_no}:F{week_no}"
        case "Friday":
            return f"F{week_no}:G{week_no}"
        case "Saturday":
            return f"G{week_no}:H{week_no}"
        case "Sunday":
            return f"H{week_no}:H{week_no}"
        case _:
            print("Invalid day")
            return None


class GoogleSheetService:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        self.service = build("sheets", "v4", credentials=credentials)

    def read(self, range_name):
        try:
            range_names = range_name
            result = (
                self.service.spreadsheets()
                .values()
                .batchGet(spreadsheetId=SHEET_ID, ranges=range_names)
                .execute()
            )
            ranges = result.get("valueRanges", [])
            print(f"{len(ranges)} ranges retrieved")
            if ranges:
                for range in ranges:
                    print(f"Values: {range['values']}")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def write(self, range_name, _value):
        try:
            values = _value
            body = {"values": values}
            result = (
                self.service.spreadsheets()
                .values()
                .update(
                    spreadsheetId=SHEET_ID,
                    range=range_name,
                    valueInputOption="USER_ENTERED",
                    body=body,
                )
                .execute()
            )
            print(f"{result.get('updatedCells')} cells updated.")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error


if __name__ == "__main__":
    google_sheet_service = GoogleSheetService()
    google_sheet_service.read(
        "A2:B2",
    )
    google_sheet_service.write(
        "A2:B2",
        [[2]],
    )
