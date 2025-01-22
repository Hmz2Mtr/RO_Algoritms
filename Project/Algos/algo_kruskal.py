# algo_kruskal.py
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

def algo_kruskal(canvas_frame, text_area, num_vertices=None):
    """
    Implémentation de l'algorithme de Kruskal pour trouver l'arbre couvrant minimal (MST).
    """
    clear_canvas(canvas_frame)

    if num_vertices is None:
        return

    def trouver(parent, i):
        if parent[i] == i:
            return i
        parent[i] = trouver(parent, parent[i])  # Path compression
        return parent[i]

    def union(parent, rank, x, y):
        root_x = trouver(parent, x)
        root_y = trouver(parent, y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    # Generate random edges
    edges = []
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            weight = random.randint(1, 10)
            edges.append((weight, u, v))

    # Sort edges by weight
    edges.sort()
    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    # Find MST using Kruskal's algorithm
    mst = []
    for weight, u, v in edges:
        root_u = trouver(parent, u)
        root_v = trouver(parent, v)
        if root_u != root_v:
            mst.append((u, v, weight))
            union(parent, rank, root_u, root_v)

    # Prepare result text
    text_area.delete("1.0", "end")
    total_weight = 0
    result = f"Arbre couvrant minimal (MST) avec {num_vertices} sommets :\n"
    for u, v, w in mst:
        result += f"{u} - {v} : {w}\n"
        total_weight += w
    result += f"Poids total du MST : {total_weight}"
    text_area.insert("end", result)

    # Visualization
    G = nx.Graph()
    for weight, u, v in edges:
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(5, 4))
    labels = nx.get_edge_attributes(G, 'weight')

    # Draw all edges in gray
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, ax=ax)

    # Draw MST edges in red
    mst_edges = [(u, v) for u, v, w in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2, ax=ax)

    # Draw nodes and labels
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    ax.set_title(f"Kruskal's MST (Total Weight = {total_weight})")

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()