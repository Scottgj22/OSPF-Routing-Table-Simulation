import networkx as nx

def build_graph_from_lsdb(lsdb):
    G = nx.Graph()
    for router_id, links in lsdb.items():
        for neighbor, cost in links.items():
            G.add_edge(router_id, neighbor, weight=cost)
    return G
