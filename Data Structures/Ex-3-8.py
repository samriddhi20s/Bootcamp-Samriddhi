#Aggregate data from different structures.
# Bus routes with scheduled stops (list of tuples)
bus_routes = {
    "Route 1": [("6:00 AM", "Downtown"), ("6:15 AM", "Central Park"), ("6:30 AM", "Airport")],
    "Route 2": [("6:30 AM", "City Center"), ("6:45 AM", "Library"), ("7:00 AM", "University")]
}

# Train lines with scheduled stations (list of tuples)
train_lines = {
    "Red Line": [("5:00 AM", "Central Station"), ("5:10 AM", "Main Street"), ("5:20 AM", "University")],
    "Blue Line": [("5:30 AM", "North End"), ("5:40 AM", "City Center"), ("5:50 AM", "Museum District")]
}

# Unique locations (Set - removes duplicates)
all_stations = set()
for stops in bus_routes.values():
    for _, station in stops:
        all_stations.add(station)

for stations in train_lines.values():
    for _, station in stations:
        all_stations.add(station)

# Aggregated transportation system
transportation_system = {
    "bus_routes": bus_routes,
    "train_lines": train_lines,
    "all_stations": all_stations
}

# Display the aggregated data
print("Aggregated Transportation System Data:\n")
for category, data in transportation_system.items():
    if category == "all_stations":
        print(f"{category}: {sorted(data)}")  # Sorting for readability
    else:
        for route, schedule in data.items():
            print(f"{route}: {schedule}")
