import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

def algo_nord_ouest(canvas_frame, text_area, nb_usines, nb_magasins):
    """
    Exemple d'algorithme du Coin Nord-Ouest pour un problème de transport.
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
        demandes[-1] += (total_capacite - total_demande)
    else:
        capacites[-1] += (total_demande - total_capacite)

    # Méthode du Coin Nord-Ouest
    def methode_nord_ouest(capacites, demandes):
        allocation = np.zeros((len(capacites), len(demandes)), dtype=int)
        i, j = 0, 0
        while i < len(capacites) and j < len(demandes):
            quantite = min(capacites[i], demandes[j])
            allocation[i, j] = quantite
            capacites[i] -= quantite
            demandes[j] -= quantite
            if capacites[i] == 0:
                i += 1
            if demandes[j] == 0:
                j += 1
        return allocation

    allocation = methode_nord_ouest(capacites.copy(), demandes.copy())

    # Calcul du coût total
    total_cost = np.sum(couts * allocation)

    # Affichage dans la zone de texte
    text_area.delete("1.0", "end")
    result = "Solution de transport (Coin Nord-Ouest) :\n"
    for i in range(nb_usines):
        for j in range(nb_magasins):
            result += f"Usine {i+1} vers Magasin {j+1}: {allocation[i,j]} unités\n"

    result += f"\nCoût total du transport : {total_cost}\n"
    text_area.insert("end", result)

    # Visualisation de la matrice des allocations sous forme de tableau
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.axis("off")

    # Création des données pour le tableau
    table_data = [[""] + [f"Magasin {j+1}" for j in range(nb_magasins)]]
    for idx, row in enumerate(allocation):
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