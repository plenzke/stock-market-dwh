from typing import Dict, Any, Optional
from polygon import Polygon

polygon = Polygon()


def get_aggregates(stocks_ticker: str, multiplier: int, timespan: str, date_from: str, date_to: str) -> Dict[str, Any]:
    """
    GET Method: Get aggregate bars for a stock over a given date range in custom time window sizes.
    """
    url = (f"{polygon.api_url}v2/aggs/ticker/{stocks_ticker}/range/{multiplier}/{timespan}/{date_from}/{date_to}"
           f"?adjusted=true&sort=asc&limit=50000&apiKey={polygon.api_token}")

    response = polygon.get_response_json(url)

    return response


def get_grouped_daily(date: str) -> Dict[str, Any]:
    """
    GET Method: Get the daily open, high, low, and close (OHLC) for the entire stocks/equities markets.
    """
    url = f"{polygon.api_url}v2/aggs/grouped/locale/global/market/stocks/{date}?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response


def get_daily(stocks_ticker: str, date: str) -> Dict[str, Any]:
    """
    GET Method: Get the open, close and afterhours prices of a stock symbol on a certain date.
    """
    url = f"{polygon.api_url}v1/open-close/{stocks_ticker}/{date}?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response


def get_pair_previous_close(stocks_ticker: str, ) -> Dict[str, Any]:
    """
    GET Method: Get the previous day's open, high, low, and close (OHLC) for the specified stock ticker.
    """
    url = f"{polygon.api_url}v2/aggs/ticker/{stocks_ticker}/prev?adjusted=true&apiKey={polygon.api_token}"

    response = polygon.get_response_json(url)

    return response
