import requests
from bs4 import BeautifulSoup

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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join(p.get_text() for p in paragraphs)
        return content
    else:
        raise Exception(f"Failed to scrape URL {url}: {response.status_code}")