from typing import Dict, Any, Optional
from polygon import Polygon

polygon = Polygon()


def get_pair_aggregates(crypto_ticker: str, multiplier: int, timespan: str, date_from: str, date_to: str) -> Dict[str, Any]:
    """
    GET Method: Get aggregate bars for a cryptocurrency pair over a given date range in custom time window sizes.
    """
    url = (f"{polygon.api_url}v2/aggs/ticker/{crypto_ticker}/range/{multiplier}/{timespan}/{date_from}/{date_to}"
           f"?adjusted=true&sort=asc&limit=50000&apiKey={polygon.api_token}")

    response = polygon.get_response_json(url)

    return response


def get_grouped_daily(date: str) -> Dict[str, Any]:
    """
    GET Method: Get the daily open, high, low, and close (OHLC) for the entire cryptocurrency markets.
    """
    url = f"{polygon.api_url}v2/aggs/grouped/locale/global/market/crypto/{date}?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response


def get_daily(from_symbol: str, to_symbol: str, date: str) -> Dict[str, Any]:
    """
    GET Method: Get the open, close prices of a cryptocurrency symbol on a certain day.
    """
    url = f"{polygon.api_url}v1/open-close/crypto/{from_symbol}/{to_symbol}/{date}?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response


def get_pair_previous_close(crypto_ticker: str, ) -> Dict[str, Any]:
    """
    GET Method: Get the previous day's open, high, low, and close (OHLC) for the specified cryptocurrency pair.
    """
    url = f"{polygon.api_url}v2/aggs/ticker/{crypto_ticker}/prev?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response