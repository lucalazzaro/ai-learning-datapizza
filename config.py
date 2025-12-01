# config.py
import os
from dotenv import load_dotenv
from datapizza.clients.openai import OpenAIClient

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in .env")

def get_client():
    return OpenAIClient(
        api_key=OPENAI_API_KEY,
        model=OPENAI_MODEL_NAME
    )
