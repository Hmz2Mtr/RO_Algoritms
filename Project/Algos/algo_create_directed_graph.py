# algo_create_directed_graph.py
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

def create_directed_graph(canvas_frame, text_area, num_vertices=None):
    """
    Create a random directed graph, display it, and show verification results
    in text_area.
    """
    clear_canvas(canvas_frame)  # Clear previous drawings

    if num_vertices is None:
        return

    # Generate random number of edges
    max_edges = num_vertices * (num_vertices - 1)  # Maximum possible edges in a directed graph
    num_edges = random.randint(num_vertices, max_edges)

    G = nx.DiGraph()
    G.add_nodes_from(range(num_vertices))

    # Add random edges
    while G.number_of_edges() < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v:
            G.add_edge(u, v)

    # Calculate in-degrees and out-degrees
    in_degrees = sum(dict(G.in_degree()).values())
    out_degrees = sum(dict(G.out_degree()).values())

    # Verify if sum of out-degrees == sum of in-degrees
    if in_degrees == out_degrees:
        verification = "Verification Passed: Sum of out-degrees equals sum of in-degrees."
    else:
        verification = "Verification Failed: Sum of out-degrees does not equal sum of in-degrees."

    # Visualization with matplotlib
    fig, ax = plt.subplots(figsize=(5, 4))
    nx.draw(G, with_labels=True, node_color='lightblue', arrows=True, ax=ax)
    ax.set_title(f"Directed Graph (V={num_vertices}, E={num_edges})")

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display result in text_area
    text_area.delete("1.0", "end")
    result_text = f"Graph created with {num_vertices} vertices and {num_edges} edges!\n{verification}"
    text_area.insert("end", result_text)