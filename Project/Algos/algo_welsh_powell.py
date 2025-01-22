import time
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

def algo_welsh_powell(canvas_frame, text_area, num_vertices=None):
    """
    Implémentation simplifiée de l'algorithme de Welsh-Powell pour la coloration des graphes.
    """
    def generer_graphe_aleatoire(n_sommets):
        """
        Génère un graphe aléatoire avec `n_sommets` sommets.
        """
        G = nx.Graph()
        for i in range(n_sommets):
            G.add_node(i)
        for i in range(n_sommets):
            for j in range(i + 1, n_sommets):
                if random.random() < 0.7:  # Probabilité de créer une arête
                    G.add_edge(i, j)
        return G

    def colorier_graphe(graphe):
        """
        Colorie le graphe en utilisant l'algorithme de Welsh-Powell.
        """
        sommets_tries = sorted(graphe.nodes, key=lambda x: len(graphe[x]), reverse=True)
        coloration = {}
        couleur_actuelle = 0
        while len(coloration) < len(graphe):
            couleur_actuelle += 1
            for sommet in sommets_tries:
                if sommet not in coloration:
                    peut_colorier = True
                    for voisin in graphe[sommet]:
                        if voisin in coloration and coloration[voisin] == couleur_actuelle:
                            peut_colorier = False
                            break
                    if peut_colorier:
                        coloration[sommet] = couleur_actuelle
        return coloration

    def random_colors(n):
        """
        Génère une liste de `n` couleurs aléatoires au format hexadécimal.
        """
        return ["#" + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(n)]

    # Clear the canvas and text area
    clear_canvas(canvas_frame)
    text_area.delete("1.0", "end")

    # Validate the number of vertices
    if num_vertices is None or num_vertices < 2:
        text_area.insert("end", "Invalid input! Number of vertices must be at least 2.\n")
        return

    # Generate a random graph
    G = generer_graphe_aleatoire(num_vertices)

    # Color the graph using Welsh-Powell algorithm
    start_time = time.time()
    coloration = colorier_graphe(G)
    exec_time = time.time() - start_time

    # Calculate the number of colors used
    unique_colors = list(set(coloration.values()))
    nb_couleurs = len(unique_colors)

    # Display the results in the text area
    result = (f"Nombre de couleurs utilisées : {nb_couleurs}\n"
              f"Temps d'exécution : {exec_time:.6f} secondes\n")
    text_area.insert("end", result)

    # Draw the graph with colors
    node_colors = random_colors(nb_couleurs)
    color_map = [node_colors[coloration[node]-1] for node in G.nodes]
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(5, 4))
    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=500, font_color='white', ax=ax)
    ax.set_title("Graph Colored by Welsh-Powell")

    # Embed the graph in the Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()