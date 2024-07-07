from typing import Dict, Any, Optional
from polygon import Polygon

polygon = Polygon()


def get_pair_aggregates(forex_ticker: str, multiplier: int, timespan: str, date_from: str, date_to: str) -> Dict[str, Any]:
    """
    GET Method: Get aggregate bars for a forex pair over a given date range in custom time window sizes.
    """
    url = (f"{polygon.api_url}v2/aggs/ticker/{forex_ticker}/range/{multiplier}/{timespan}/{date_from}/{date_to}"
           f"?adjusted=true&sort=asc&limit=50000&apiKey={polygon.api_token}")

    response = polygon.get_response_json(url)

    return response


def get_grouped_daily(date: str) -> Dict[str, Any]:
    """
    GET Method: Get the daily open, high, low, and close (OHLC) for the entire forex markets.
    """
    url = f"{polygon.api_url}v2/aggs/grouped/locale/global/market/fx/{date}?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response


def get_pair_previous_close(forex_ticker: str, ) -> Dict[str, Any]:
    """
    GET Method: Get the previous day's open, high, low, and close (OHLC) for the specified forex pair.
    """
    url = f"{polygon.api_url}v2/aggs/ticker/{forex_ticker}/prev?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response