from .graph import create_graph, save_graph_visualization
from .chat.loop import start_chat_loop

def run():
    """Runs the main application loop."""
    graph = create_graph()
    save_graph_visualization(graph)
    start_chat_loop(graph)
