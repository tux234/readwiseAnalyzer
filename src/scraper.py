import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import socket
from ipaddress import ip_address

from functools import lru_cache

_session = requests.Session()
_SCRAPER_TIMEOUT = 10

@lru_cache(maxsize=None)
def scrape_content(url):
    """
    Scrape the main content from a given URL.

    Args:
        url (str): The URL of the page to scrape.

    Returns:
        str: Extracted text content from the page.

    Raises:
        Exception: If the URL cannot be scraped due to HTTP errors.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Unsupported URL scheme: {parsed.scheme!r}")

    try:
        host_ip = socket.gethostbyname(parsed.hostname)
        if ip_address(host_ip).is_private:
            raise ValueError(f"Access to private IP {host_ip} is not allowed")
    except Exception as e:
        raise ValueError(f"Invalid host {parsed.hostname}: {e}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = _session.get(url, headers=headers, timeout=_SCRAPER_TIMEOUT)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join(p.get_text() for p in paragraphs)
        return content
    else:
        raise Exception(f"Failed to scrape URL {url}: {response.status_code}")