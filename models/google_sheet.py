from __future__ import annotations

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "/Users/minhdg241/Documents/minh.json"
SHEET_ID = "1nSHAxqSRxWhdpAbkNLoO0idbcBFkFBwgqwYBX5l0BTk"


class GoogleSheetService:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        self.service = build("sheets", "v4", credentials=credentials)

    def read():
        pass

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
    google_sheet_service.write(
        "A1:C2",
        [["A", "B"], ["C", "D"]],
    )
