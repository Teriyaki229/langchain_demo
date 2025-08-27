from langchain.chat_models import init_chat_model
from . import config


def get_llm():
    """Initializes and returns the chat model."""
    return init_chat_model(model=config.LANGCHAIN_MODEL, apiKey=config.GOOGLE_API_KEY)
