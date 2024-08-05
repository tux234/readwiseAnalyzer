from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# These variables will be accessible throughout the package
READWISE_API_KEY = os.getenv('READWISE_API_KEY')

# Import your main modules to make them easily accessible
from .readwise import fetch_feed

# Any package-level initialization can go here