import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_MODEL = os.getenv("LANGCHAIN_MODEL")
