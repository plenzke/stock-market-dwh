import os
from typing import Dict, Any, Optional
import requests
from dotenv import load_dotenv

# Load API TOKEN from .env
load_dotenv()
API_TOKEN = os.getenv("POLYGON_API_TOKEN")
API_URL = os.getenv("POLYGON_API_URL")


def get_pair_previous_close(forex_ticker: str, api_token: str, api_url) -> Dict[str, Any]:
    """
    GET Method: Get the previous day's open, high, low, and close (OHLC) for the specified forex pair.
    :param api_url: API URL
    :param api_token: API Auth Token
    :param forex_ticker: The ticker symbol of the currency pair.
    :return: JSON in Dict[str, Any]
    """
    url = f"{api_url}v2/aggs/ticker/{forex_ticker}/prev?adjusted=true&apiKey={api_token}"

    response = requests.get(url)

    return response.json()


def get_pair_aggregates(forex_ticker: str, multiplier: int, timespan: str, date_from: str, date_to: str, api_token: str,
                        api_url) -> Dict[str, Any]:
    """
    GET Method: Get aggregate bars for a forex pair over a given date range in custom time window sizes.
    :param date_to: Date in YYYY-MM-DD format
    :param date_from: Date in YYYY-MM-DD format
    :param timespan: The size of the time window: year, quarter, month, week, day, hour, minute, second
    :param multiplier: The size of the timespan multiplier
    :param api_url: API URL
    :param api_token: API Auth Token
    :param forex_ticker: The ticker symbol of the currency pair.
    :return: JSON in Dict[str, Any]
    """
    url = f"{api_url}v2/aggs/ticker/{forex_ticker}/range/{multiplier}/{timespan}/{date_from}/{date_to}?adjusted=true&sort=asc&apiKey={api_token}"

    response = requests.get(url)

    return response.json()


def get_grouped_daily(date: str, api_token: str, api_url: str) -> Dict[str, Any]:
    """
    GET Method: Get the daily open, high, low, and close (OHLC) for the entire forex markets.
    :param date: The beginning date for the aggregate window in YYYY-MM-DD format
    :param api_token: API Auth Token
    :param api_url: API URL
    :return: JSON in Dict[str, Any]
    """
    url = f"{api_url}v2/aggs/grouped/locale/global/market/fx/{date}?adjusted=true&apiKey={api_token}"

    response = requests.get(url)

    return response.json()


def get_quotes_bbo(fx_ticker: str, date: Optional[str], api_token: str, api_url: str) -> Dict[str, Any]:
    """
    GET Method: Get BBO quotes for a ticker symbol in a given time range.
    :param api_token: API Auth Token
    :param api_url: API URL
    :param date: Query by timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
    :param fx_ticker: The ticker symbol to get quotes for
    :return:
    """
    url = f"{api_url}v3/quotes/{fx_ticker}?timestamp={date}&limit=10&apiKey={api_token}"

    response = requests.get(url)

    return response.json()


# print(get_pair_previous_close(forex_ticker="C:USDRUB", api_token=API_TOKEN, api_url=API_URL))
# print(get_pair_aggregates(forex_ticker="C:USDRUB", multiplier=1, timespan="day", date_from="2024-06-01", date_to="2024-06-30", api_token=API_TOKEN, api_url=API_URL))
# print(get_grouped_daily(date="2024-06-30", api_token=API_TOKEN, api_url=API_URL))
print(get_quotes_bbo(fx_ticker="C:EUR-USD", date="2024-06-30", api_token=API_TOKEN, api_url=API_URL))
