from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from .llm import get_llm

class ChatBotState(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: ChatBotState):
    llm = get_llm()
    return {"messages": [llm.invoke(state["messages"])]}
