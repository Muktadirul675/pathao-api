import os
from dotenv import load_dotenv

load_dotenv()

PATHAO_BASE_URL = os.getenv("PATHAO_BASE_URL")
PATHAO_STORE_ID = os.getenv("PATHAO_STORE_ID")
PATHAO_CLIENT_ID = os.getenv("PATHAO_CLIENT_ID")
PATHAO_CLIENT_SECRET = os.getenv("PATHAO_CLIENT_SECRET")
PATHAO_USERNAME = os.getenv("PATHAO_USERNAME")
PATHAO_PASSWORD = os.getenv("PATHAO_PASSWORD")

