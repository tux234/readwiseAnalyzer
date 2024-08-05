import requests
from dotenv import load_dotenv
import os
import yaml

# Load environment variables
load_dotenv()

READWISE_API_KEY = os.getenv('READWISE_API_KEY')

# Load configuration from config.yml
def load_config():
    with open('config/config.yml', 'r') as file:
        return yaml.safe_load(file)

config = load_config()
base_url = config['readwise']['base_url']
endpoints = config['readwise']['endpoints']

def fetch_source_urls(location):
    """Fetch source URLs from the Readwise API based on location and filter out certain URLs."""
    url = base_url + endpoints['list_documents']['url']
    headers = {"Authorization": f"Token {READWISE_API_KEY}"}
    params = {'location': location}

    response = requests.get(url, headers=headers, params=params)
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

# To Test uncomment the below
# if __name__ == "__main__":
#     try:
#         source_urls = fetch_source_urls(location='feed')
#         for url in source_urls:
#             print(url)
#     except Exception as e:
#         print(f"Error: {e}")