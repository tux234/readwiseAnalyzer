import requests
from dotenv import load_dotenv
import os
import yaml

load_dotenv()

READWISE_API_KEY = os.getenv('READWISE_API_KEY')
if not READWISE_API_KEY:
    raise EnvironmentError("READWISE_API_KEY must be set in environment or .env file")

_session = requests.Session()
_READWISE_TIMEOUT = 10

def load_config():
    """
    Load configuration from the config.yml file.

    Returns:
        dict: Configuration data from the YAML file.
    """
    with open('config/config.yml', 'r') as file:
        return yaml.safe_load(file)

config = load_config()
base_url = config['readwise']['base_url']
endpoints = config['readwise']['endpoints']

def fetch_source_urls(location='new'):
    """
    Fetch source URLs from the Readwise API based on location and filter out certain URLs.

    Args:
        location (str): The location parameter to filter documents. Defaults to 'new'.

    Returns:
        list: A list of filtered source URLs.
    """
    if location not in ('new', 'later', 'shortlist', 'archive', 'feed'):
        raise ValueError(f"Invalid location: {location!r}")
    url = base_url + endpoints['list_documents']['url']
    headers = {"Authorization": f"Token {READWISE_API_KEY}"}
    params = {'location': location}

    response = _session.get(
        url, headers=headers, params=params, timeout=_READWISE_TIMEOUT
    )
    if response.status_code == 200:
        documents = response.json().get('results', [])

        # Filter out URLs starting with "mailto:reader-forwarded-email"
        source_urls = [
            doc['source_url'] for doc in documents
            if 'source_url' in doc and not doc['source_url'].startswith('mailto:reader-forwarded-email')
        ]

        return source_urls
    else:
        raise Exception(f"Failed to fetch documents: {response.status_code}")

if __name__ == "__main__":
    try:
        source_urls = fetch_source_urls()
        for url in source_urls:
            print(url)
    except Exception as e:
        print(f"Error: {e}")