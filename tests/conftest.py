# Insert src directory into sys.path so application modules can be imported directly
import os
import sys

# Add project's src/ directory to the import path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
SRC_PATH = os.path.join(ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import pytest
from scraper import scrape_content

@pytest.fixture(autouse=True)
def clear_scrape_cache():
    scrape_content.cache_clear()