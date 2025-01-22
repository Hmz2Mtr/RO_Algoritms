import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

def algo_stepping_stone(canvas_frame, text_area, nb_usines, nb_magasins):
    """
    Exemple d'algorithme Stepping Stone pour un problème de transport.
    Affiche la solution dans text_area et la matrice des allocations sur canvas_frame.
    """
    clear_canvas(canvas_frame)

    # Génération aléatoire de données
    couts = np.random.randint(1, 100, (nb_usines, nb_magasins))
    capacites = np.random.randint(20, 100, nb_usines)
    demandes = np.random.randint(20, 100, nb_magasins)

    total_capacite = np.sum(capacites)
    total_demande = np.sum(demandes)

    # Ajustement pour assurer l'équilibre
    if total_capacite > total_demande:
        demandes[-1] += total_capacite - total_demande
    else:
        capacites[-1] += total_demande - total_capacite

    def stepping_stone_algorithm(couts, capacites, demandes):
        m, n = len(couts), len(couts[0])
        solution = np.zeros((m, n), dtype=int)

        # Solution initiale (coin Nord-Ouest)
        i, j = 0, 0
        while i < m and j < n:
            qty = min(capacites[i], demandes[j])
            solution[i][j] = qty
            capacites[i] -= qty
            demandes[j] -= qty
            if capacites[i] == 0: i += 1
            if demandes[j] == 0: j += 1

        # Étape d'amélioration simplifiée (pas un stepping-stone complet)
        improved = True
        while improved:
            improved = False
            min_cost = float('inf')
            min_cell = None
            # Vérifier toutes les cellules vides
            for r in range(m):
                for c in range(n):
                    if solution[r][c] == 0:
                        cost = couts[r][c]
                        if cost < min_cost:
                            min_cost = cost
                            min_cell = (r, c)
            if min_cell:
                # Exemple : Placer 1 unité dans la cellule la moins chère
                r, c = min_cell
                solution[r][c] = 1
                improved = True

        return solution

    solution = stepping_stone_algorithm(couts, capacites.copy(), demandes.copy())
    total_cost = np.sum(couts * solution)

    # Affichage dans la zone de texte
    text_area.delete("1.0", "end")
    result = "Solution Stepping Stone :\n"
    for i in range(nb_usines):
        for j in range(nb_magasins):
            result += f"Usine {i+1} vers Magasin {j+1}: {solution[i,j]} unités\n"
    result += f"\nCoût total : {total_cost}\n"
    text_area.insert("end", result)

    # Visualisation de la matrice des allocations sous forme de tableau
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.axis("off")

    # Création des données pour le tableau
    table_data = [[""] + [f"Magasin {j+1}" for j in range(nb_magasins)]]
    for idx, row in enumerate(solution):
        table_data.append([f"Usine {idx+1}"] + list(row))

    # Création du tableau
    table = ax.table(
        cellText=table_data, 
        loc="center", 
        cellLoc="center", 
        colLoc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.2, 1.2)

    # Affichage du tableau dans l'interface graphique
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()