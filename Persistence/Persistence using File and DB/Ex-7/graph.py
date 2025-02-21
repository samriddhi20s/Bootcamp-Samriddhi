import json

class Graph:
    def __init__(self):
        self.nodes = []  
        self.edges = {}  

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.edges[node1].append(node2)
            self.edges[node2].append(node1)

    def to_json(self):
        return json.dumps({"nodes": self.nodes, "edges": self.edges}, indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)  # Parse JSON string
        graph = cls()  
        graph.nodes = data["nodes"]
        graph.edges = data["edges"]
        return graph  # Return reconstructed object

    def __repr__(self):
        return f"Graph(nodes={self.nodes}, edges={self.edges})"
