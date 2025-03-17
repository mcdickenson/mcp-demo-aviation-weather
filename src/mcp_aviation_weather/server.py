import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from html2text import html2text

from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

mcp = FastMCP("aviation_weather")

@mcp.tool()
def get_aviation_weather(
    airport: str
) -> str:
    """
    Get aviation weather for a given airport.

    Args:
        airport (str): The ICAO code of the airport.

    Returns:
        str: The aviation weather report.
    """
    try:
        url = f"https://aviationweather.gov/api/data/metar?ids={airport}"
        response = requests.get(url)
        response.raise_for_status()
    except RequestException as e:
        raise McpError(INTERNAL_ERROR, ErrorData(str(e)))

    try:
        return response.content
    except AttributeError:
        raise McpError(INVALID_PARAMS, ErrorData("No data found for the given airport."))
