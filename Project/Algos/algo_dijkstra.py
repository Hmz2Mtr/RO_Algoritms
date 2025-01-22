# algo_dijkstra.py
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

def algo_dijkstra(canvas_frame, text_area, num_vertices=None):
    """
    Implémentation de l'algorithme de Dijkstra pour trouver le chemin le plus court.
    """
    clear_canvas(canvas_frame)

    if num_vertices is None:
        return

    # Generate a random directed graph
    G = nx.DiGraph()
    for i in range(num_vertices):
        G.add_node(f'x{i}')
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and random.random() < 0.5:
                G.add_edge(f'x{i}', f'x{j}', weight=random.randint(1, 20))

    noeud_depart = random.choice(list(G.nodes))
    noeud_arrivee = random.choice(list(G.nodes))
    while noeud_arrivee == noeud_depart:
        noeud_arrivee = random.choice(list(G.nodes))

    text_area.delete("1.0", "end")
    try:
        path = nx.dijkstra_path(G, noeud_depart, noeud_arrivee)
        distance = nx.dijkstra_path_length(G, noeud_depart, noeud_arrivee)
        result = (f"Chemin le plus court de {noeud_depart} à {noeud_arrivee} : {path}\n"
                  f"Distance totale : {distance}")
    except nx.NetworkXNoPath:
        result = f"Aucun chemin n'existe entre {noeud_depart} et {noeud_arrivee}."

    text_area.insert("end", result)

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(5, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    # If a path exists, highlight it
    if "path" in locals():
        edges_on_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_on_path, edge_color='red', width=2, ax=ax)

    ax.set_title("Algorithme de Dijkstra")
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()