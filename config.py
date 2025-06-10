import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv('SERPAPI_KEY')
APOLLO_KEY = os.getenv('APOLLO_KEY')

print(APOLLO_KEY)