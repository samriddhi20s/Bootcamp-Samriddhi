from graph import Graph

# Step 1: Create a Graph and add nodes and edges
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")

# Step 2: Serialize the Graph to JSON
json_representation = graph.to_json()
print("Serialized JSON:\n", json_representation)

# Step 3: Deserialize JSON back into a Graph object
deserialized_graph = Graph.from_json(json_representation)
print("\nDeserialized Graph Object:", deserialized_graph)
