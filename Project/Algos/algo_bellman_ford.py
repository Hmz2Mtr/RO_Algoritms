# algo_bellman_ford.py
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

class Edge:
    """
    Simple class to represent an edge in the Bellman-Ford algorithm.
    """
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def bellman_ford(graph_edges, source, num_vertices):
    distances = [float("inf")] * num_vertices
    distances[source] = 0

    # Relax edges (num_vertices - 1) times
    for _ in range(num_vertices - 1):
        for edge in graph_edges:
            if distances[edge.u] != float("inf") and distances[edge.u] + edge.weight < distances[edge.v]:
                distances[edge.v] = distances[edge.u] + edge.weight

    # Check for negative-weight cycles
    for edge in graph_edges:
        if distances[edge.u] != float("inf") and distances[edge.u] + edge.weight < distances[edge.v]:
            return None  # Negative cycle detected
    return distances

def create_random_edges(num_vertices):
    edges = []
    max_edges = num_vertices * (num_vertices - 1) // 2
    nb_edges = random.randint(num_vertices, max_edges)
    for _ in range(nb_edges):
        u, v = random.sample(range(num_vertices), 2)
        weight = random.randint(1, 10)
        edges.append(Edge(u, v, weight))
    return edges

def algo_bellman_ford(canvas_frame, text_area, num_vertices=None):
    """
    Implémentation de l'algorithme de Bellman-Ford pour trouver les plus courts chemins.
    """
    clear_canvas(canvas_frame)

    if num_vertices is None:
        return

    graph_edges = create_random_edges(num_vertices)
    distances = bellman_ford(graph_edges, 0, num_vertices)

    text_area.delete("1.0", "end")
    if distances is None:
        text_area.insert("end", "Le graphe contient un cycle de poids négatif.")
    else:
        result = "Distances depuis la source (0) :\n"
        for i, dist in enumerate(distances):
            result += f"Node {i}: {dist}\n"
        text_area.insert("end", result)

        # Build the graph for visualization
        G = nx.DiGraph()
        for edge in graph_edges:
            G.add_edge(edge.u, edge.v, weight=edge.weight)

        pos = nx.spring_layout(G)
        fig, ax = plt.subplots(figsize=(5, 4))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True, ax=ax)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
        ax.set_title("Bellman-Ford Results")

        canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()