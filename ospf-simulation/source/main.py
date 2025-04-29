from router import Router
from network import build_graph_from_lsdb
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

# Step 1: Create routers
routers = {
    "A": Router("A"),
    "B": Router("B"),
    "C": Router("C"),
    "D": Router("D"),
    "E": Router("E"),
    "F": Router("F"),
    "G": Router("G"),
}

# Define neighbor relationships as pairs
links = [
    ("A", "B"), ("A", "C"),
    ("B", "A"), ("B", "C"), ("B", "D"),
    ("C", "A"), ("C", "B"), ("C", "D"), ("C", "E"), ("C", "G"),
    ("D", "B"), ("D", "C"), ("D", "E"),
    ("E", "D"), ("E", "F"), ("E", "C"), ("E", "G"),
    ("F", "E"), ("F", "G"),
    ("G", "F"), ("G", "E"), ("G", "C"),
]

print("\n--- Initializing Routers ---")
for router_id in routers:
    print(f"Router {router_id} initialized.")
    time.sleep(0.5)

# Step 2: Define neighbor relationships
print("\n--- Defining Neighbor Relationships ---")
for src, dest in links:
    cost = random.randint(1, 5)
    routers[src].add_neighbor(dest, cost)
    print(f"Link created: {src} -> {dest} (Cost: {cost})")
    time.sleep(0.5)

print("Router A neighbors:", routers["A"].neighbors)
print("Router B neighbors:", routers["B"].neighbors)
print("Router C neighbors:", routers["C"].neighbors)
print("Router D neighbors:", routers["D"].neighbors)
print("Router E neighbors:", routers["E"].neighbors)
print("Router F neighbors:", routers["F"].neighbors)
print("Router G neighbors:", routers["G"].neighbors)
print("Neighbor relationships defined.")

# Step 3: Exchange LSAs (simulate flooding)
print("\n--- Generating and Exchanging LSAs ---")
for r in routers.values():
    lsa = r.generate_lsa()
    print(f"Router {r.router_id} generated LSA: {lsa}")
    time.sleep(0.5)
    for other in routers.values():
        other.receive_lsa(lsa)
        print(f"Router {other.router_id} received LSA from {r.router_id}: {lsa}")
        time.sleep(0.5)

# Step 5: Build the network topology graph
print("\n--- Building Network Topology ---")
sample_router = routers["A"]
G = build_graph_from_lsdb(sample_router.lsdb)
time.sleep(0.5)
print("Network topology graph built.")

# Step 4: Calculate and display routing tables for each router
print("\033[92m--- Routing Tables ---\033[0m")
for router_id in routers:
    print(f"\n\033[92mRouter {router_id} running SPF algorithm...\033[0m")
    paths = nx.single_source_dijkstra_path_length(G, router_id)
    time.sleep(0.5)
    print(f"\033[92mRouter {router_id} Routing Table: {paths}\033[0m")
    time.sleep(0.5)

# Step 6: Visualize the entire network graph once
print("\n--- Visualizing Network Topology ---")
pos = {
    "A": (0, 2),
    "B": (1, 3),
    "C": (2, 2),
    "D": (3, 3),
    "E": (4, 2),
    "F": (5, 1),
    "G": (3, 1),
    }

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}
)
plt.title("Shared Network Topology (All Routers)")
plt.show()
