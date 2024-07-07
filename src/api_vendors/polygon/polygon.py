import os
from typing import Dict, Any, Optional
import requests
from dotenv import load_dotenv


class Polygon:
    """Class for connecting to the polygon api and sending requests"""
    def __init__(self):
        # Load API TOKEN from .env
        load_dotenv()
        self.api_token = os.getenv("POLYGON_API_TOKEN")
        self.api_url = os.getenv("POLYGON_API_URL")

    def get_response_json(self, url: str) -> Dict[str, Any]:
        """
        Gets data from a url request in json format
        """
        response = requests.get(url)

        return response.json()