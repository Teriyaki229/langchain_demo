from langgraph.graph import StateGraph, START, END
from .chat.bot import chatbot, ChatBotState


def save_graph_visualization(graph):
    """Saves the graph visualization as a PNG file."""
    try:
        with open("graph.png", "wb") as f:
            f.write(graph.get_graph().draw_mermaid_png())
        print("Graph visualization saved as graph.png")
    except Exception as e:
        # This requires some extra dependencies and is optional
        print(f"Could not generate graph visualization: {e}")
        pass


def create_graph():
    """Creates and compiles the LangGraph."""
    graph_builder = StateGraph(ChatBotState)
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    return graph_builder.compile()
