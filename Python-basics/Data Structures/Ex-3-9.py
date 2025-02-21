#Calculate the total number of unique stations served by both buses and trains.
# Bus routes with stops
bus_routes = {
    "Route 1": ["Downtown", "Central Park", "Airport"],
    "Route 2": ["City Center", "Library", "University"]
}

# Train lines with stations
train_lines = {
    "Red Line": ["Central Station", "Main Street", "University", "Airport"],
    "Blue Line": ["North End", "City Center", "Museum District"]
}

# Create a set to store all unique stations
unique_stations = set()

# Add bus stops to the set
for stops in bus_routes.values():
    unique_stations.update(stops)

# Add train stations to the set
for stations in train_lines.values():
    unique_stations.update(stations)

# Calculate total number of unique stations
total_unique_stations = len(unique_stations)

print("Total number of unique stations:", total_unique_stations)
print("List of unique stations:", sorted(unique_stations))  # Sorted for readability
