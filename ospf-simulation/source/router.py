class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.neighbors = {}  # neighbor_id: cost
        self.lsdb = {}

    def add_neighbor(self, neighbor_id, cost):
        self.neighbors[neighbor_id] = cost

    def generate_lsa(self):
        return {
            "router_id": self.router_id,
            "links": self.neighbors
        }

    def receive_lsa(self, lsa):
        self.lsdb[lsa['router_id']] = lsa['links']
