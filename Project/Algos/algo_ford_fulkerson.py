# algo_ford_fulkerson.py
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas
import random

def algo_ford_fulkerson(canvas_frame, text_area, num_vertices):
    clear_canvas(canvas_frame)

    def bfs(capacity, source, sink, parent):
        visited = [False] * len(capacity)
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for v in range(len(capacity)):
                if not visited[v] and capacity[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(capacity, source, sink):
        parent = [-1] * len(capacity)
        max_flow = 0
        while bfs(capacity, source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]
            v = sink
            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                capacity[v][u] += path_flow
                v = parent[v]
            max_flow += path_flow
        return max_flow

    # Generate random capacities for the graph
    capacity = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            capacity[i][j] = random.randint(1, 20)
            capacity[j][i] = random.randint(1, 20)

    source = 0
    sink = num_vertices - 1
    max_flow = ford_fulkerson(capacity, source, sink)

    # Display text result
    text_area.delete("1.0", "end")
    result = f"Le flot maximum entre la source {source} et le puits {sink} est : {max_flow}"
    text_area.insert("end", result)

    # Build a DiGraph for visualization
    G = nx.DiGraph()
    for u in range(num_vertices):
        for v in range(num_vertices):
            if capacity[u][v] > 0:
                G.add_edge(u, v, capacity=capacity[u][v])

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(5, 4))
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
    ax.set_title(f"Ford-Fulkerson Max Flow: {max_flow}")

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()