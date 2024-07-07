from typing import Dict, Any, Optional
from polygon import Polygon

polygon = Polygon()


def get_aggregates(options_ticker: str, multiplier: int, timespan: str, date_from: str, date_to: str) -> Dict[str, Any]:
    """
    GET Method: Get aggregate bars for an option contract over a given date range in custom time window sizes.
    """
    url = (f"{polygon.api_url}v2/aggs/ticker/{options_ticker}/range/{multiplier}/{timespan}/{date_from}/{date_to}"
           f"?adjusted=true&sort=asc&limit=50000&apiKey={polygon.api_token}")

    response = polygon.get_response_json(url)

    return response


def get_daily(options_ticker: str, date: str) -> Dict[str, Any]:
    """
    GET Method: Get the open, close and afterhours prices of an options contract on a certain date.
    """
    url = f"{polygon.api_url}v1/open-close/{options_ticker}/{date}?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response


def get_pair_previous_close(options_ticker: str, ) -> Dict[str, Any]:
    """
    GET Method: Get the previous day's open, high, low, and close (OHLC) for the specified option contract.
    """
    url = f"{polygon.api_url}v2/aggs/ticker/{options_ticker}/prev?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response
