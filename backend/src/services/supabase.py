from __future__ import annotations

import json
import logging
import os
from typing import Dict, List, Optional

import plotly
import requests
from dotenv import load_dotenv
from supabase import Client, create_client

logger = logging.getLogger(__name__)
load_dotenv()


class SupabaseClient:
    def __init__(self):
        self.url: str = os.getenv("SUPABASE_URL", "")
        self.key: str = os.getenv("SUPABASE_KEY", "")
        self.client: Client = create_client(self.url, self.key)
        self.bucket_name: str = os.getenv("SUPABASE_BUCKET_NAME", "activities")

    def upload_json(self, data: List[Dict], file_name: str) -> Dict:
        """Upload a JSON object to Supabase Storage

        Args:
            data: JSON data to upload
            file_name: Name to save the file as in storage (should end with .json)

        Returns:
            Dict containing the upload response
        """
        try:
            # Convert dict to JSON string
            json_str = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

            # Upload to Supabase storage
            response = self.client.storage.from_(self.bucket_name).upload(
                file_name,
                json_str.encode("utf-8"),
                {"content-type": "application/json", "upsert": "true"},
            )
            return response
        except Exception as e:
            logger.error(f"Error uploading JSON: {e}")
            return None

    def read_json(self, file_name: str) -> Optional[Dict]:
        """Read a JSON file from Supabase Storage

        Args:
            file_name: Name of the file to read from storage (should end with .json)

        Returns:
            Dict containing the JSON data if successful, None otherwise
        """
        try:
            # Get signed URL from Supabase storage, valid for 60 seconds
            signed_url = self.client.storage.from_(self.bucket_name).create_signed_url(
                file_name, 60
            )["signedURL"]

            # Use the signed URL to read the file content
            response = requests.get(signed_url)
            response.raise_for_status()

            # Parse JSON
            return response.json()
        except Exception as e:
            logger.error(f"Error reading JSON: {e}")
            return None
