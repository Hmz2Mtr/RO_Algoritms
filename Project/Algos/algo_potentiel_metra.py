# algo_potentiel_metra.py
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algos.utils import clear_canvas

def algo_potentiel_metra(canvas_frame, text_area):
    clear_canvas(canvas_frame)

    def generate_costs_and_supply_demand():
        n_sources = random.randint(3, 5)
        n_destinations = random.randint(3, 5)

        supply = [random.randint(30, 50) for _ in range(n_sources)]
        demand = [random.randint(30, 50) for _ in range(n_destinations)]

        total_supply = sum(supply)
        total_demand = sum(demand)
        if total_supply > total_demand:
            demand[-1] += (total_supply - total_demand)
        elif total_demand > total_supply:
            supply[-1] += (total_demand - total_supply)

        cost = [[random.randint(1, 10) for _ in range(n_destinations)] 
                for _ in range(n_sources)]
        return supply, demand, cost

    def potentiel_metra_algorithm(supply, demand, cost):
        n_sources = len(supply)
        n_destinations = len(demand)
        allocation = [[0]*n_destinations for _ in range(n_sources)]
        for i in range(n_sources):
            for j in range(n_destinations):
                if supply[i] > 0 and demand[j] > 0:
                    qty = min(supply[i], demand[j])
                    allocation[i][j] = qty
                    supply[i] -= qty
                    demand[j] -= qty
        total_cost = sum(allocation[i][j]*cost[i][j] 
                         for i in range(n_sources) 
                         for j in range(n_destinations))
        return allocation, total_cost

    supply, demand, cost = generate_costs_and_supply_demand()
    allocation, total_cost = potentiel_metra_algorithm(supply, demand, cost)

    # Show result in text_area
    text_area.delete("1.0", "end")
    result = "Solution Potentiel Metra :\nCoûts :\n"
    for row in cost:
        result += f"{row}\n"
    result += "\nAllocation :\n"
    for i, row in enumerate(allocation):
        result += f"Source {i+1}: {row}\n"
    result += f"\nCoût total : {total_cost}\n"
    text_area.insert("end", result)

    # Build a directed graph to illustrate
    G = nx.DiGraph()
    sources = [f"S{i+1}" for i in range(len(allocation))]
    destinations = [f"D{j+1}" for j in range(len(allocation[0]))]
    G.add_nodes_from(sources + destinations)

    edge_labels = {}
    for i, src in enumerate(sources):
        for j, dst in enumerate(destinations):
            if allocation[i][j] > 0:
                G.add_edge(src, dst, flow=allocation[i][j])
                edge_labels[(src, dst)] = f"{allocation[i][j]}"

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(5, 4))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    ax.set_title(f"Potentiel Metra (Coût Total : {total_cost})")

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
