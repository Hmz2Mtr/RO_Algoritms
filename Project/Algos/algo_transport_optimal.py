from Algos.utils import clear_canvas

def algo_transport_optimal(canvas_frame, text_area, nb_usines, nb_magasins):
    clear_canvas(canvas_frame)
    text_area.delete("1.0", "end")

    try:
        # Increase the height of the text area
        text_area.config(height=20)  # Set the height to 20 lines (or any value you prefer)

        import numpy as np

        def generer_tableaux(nb_usines, nb_magasins):
            couts = np.random.randint(1, 100, (nb_usines, nb_magasins))
            capacites = np.random.randint(20, 100, nb_usines)
            demandes = np.random.randint(20, 100, nb_magasins)
            
            total_capacite = np.sum(capacites)
            total_demande = np.sum(demandes)
            
            # Ajuster la capacité et la demande pour qu'elles soient égales
            if total_capacite > total_demande:
                demandes[-1] += (total_capacite - total_demande)
            else:
                capacites[-1] += (total_demande - total_capacite)
            
            return couts, capacites, demandes

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
                elif demandes[j] == 0:
                    j += 1
            return allocation

        def methode_moindre_cout(couts, capacites, demandes):
            allocation = np.zeros((len(capacites), len(demandes)), dtype=int)
            couts_trie = sorted([(i, j, couts[i, j]) for i in range(len(capacites)) for j in range(len(demandes))], key=lambda x: x[2])
            for i, j, _ in couts_trie:
                if capacites[i] > 0 and demandes[j] > 0:
                    quantite = min(capacites[i], demandes[j])
                    allocation[i, j] = quantite
                    capacites[i] -= quantite
                    demandes[j] -= quantite
            return allocation

        def trouver_cycle(allocation, start_i, start_j):
            # Find a cycle in the allocation matrix starting from (start_i, start_j)
            cycle = [(start_i, start_j)]
            visited_rows = set()
            visited_cols = set()
            visited_rows.add(start_i)
            visited_cols.add(start_j)
            
            while True:
                # Find the next cell in the cycle
                found = False
                for i in range(allocation.shape[0]):
                    if i not in visited_rows and allocation[i, start_j] > 0:
                        cycle.append((i, start_j))
                        visited_rows.add(i)
                        start_i = i
                        found = True
                        break
                if not found:
                    for j in range(allocation.shape[1]):
                        if j not in visited_cols and allocation[start_i, j] > 0:
                            cycle.append((start_i, j))
                            visited_cols.add(j)
                            start_j = j
                            found = True
                            break
                if not found:
                    break
            return cycle

        def modifier_cycle(allocation, cycle):
            # Modify the allocation matrix based on the cycle
            min_value = float('inf')
            for i, j in cycle[1::2]:  # Only consider cells where we subtract
                if allocation[i, j] < min_value:
                    min_value = allocation[i, j]
            for idx, (i, j) in enumerate(cycle):
                if idx % 2 == 0:
                    allocation[i, j] += min_value
                else:
                    allocation[i, j] -= min_value

        def stepping_stone(couts, allocation):
            nb_usines, nb_magasins = couts.shape
            while True:
                # Étape 1 : calculer les réduits
                u = np.zeros(nb_usines)  # Initialize u with zeros
                v = np.zeros(nb_magasins)  # Initialize v with zeros

                # Solve for u and v using the allocated cells
                for _ in range(nb_usines + nb_magasins):
                    for i in range(nb_usines):
                        for j in range(nb_magasins):
                            if allocation[i, j] > 0:
                                if u[i] != 0 or v[j] != 0:
                                    v[j] = couts[i, j] - u[i]
                                    u[i] = couts[i, j] - v[j]

                # Étape 2 : vérifier la condition optimale
                reduits = np.zeros_like(couts)
                for i in range(nb_usines):
                    for j in range(nb_magasins):
                        if allocation[i, j] == 0:
                            reduits[i, j] = couts[i, j] - (u[i] + v[j])

                if np.all(reduits >= 0):  # Si tous les réduits sont positifs, solution optimale atteinte
                    break

                # Étape 3 : améliorer la solution avec le cycle
                neg_i, neg_j = np.unravel_index(np.argmin(reduits), reduits.shape)
                cycle = trouver_cycle(allocation, neg_i, neg_j)
                modifier_cycle(allocation, cycle)

            return allocation

        def afficher_resultats(couts, allocation):
            text_area.insert("end", "\nCoûts unitaires de transport :\n")
            text_area.insert("end", str(couts) + "\n")
            text_area.insert("end", "\nAllocation optimale :\n")
            text_area.insert("end", str(allocation) + "\n")
            text_area.insert("end", "\nCoût total : " + str(np.sum(couts * allocation)) + "\n")

        # Main execution
        couts, capacites, demandes = generer_tableaux(nb_usines, nb_magasins)

        text_area.insert("end", f"\nCapacités des usines ({nb_usines}): " + str(capacites) + "\n")
        text_area.insert("end", f"Demandes des magasins ({nb_magasins}): " + str(demandes) + "\n")

        allocation_nord_ouest = methode_nord_ouest(capacites.copy(), demandes.copy())
        text_area.insert("end", "\nMéthode du coin nord-ouest :\n")
        afficher_resultats(couts, allocation_nord_ouest)

        allocation_moindre_cout = methode_moindre_cout(couts, capacites.copy(), demandes.copy())
        text_area.insert("end", "\nMéthode du moindre coût :\n")
        afficher_resultats(couts, allocation_moindre_cout)

        allocation_finale = stepping_stone(couts, allocation_moindre_cout)
        text_area.insert("end", "\nSolution finale avec l'algorithme de Stepping Stone :\n")
        afficher_resultats(couts, allocation_finale)

    except Exception as e:
        text_area.insert("end", f"\nErreur lors de l'exécution de l'algorithme : {str(e)}\n")
    finally:
        text_area.config(height=10)