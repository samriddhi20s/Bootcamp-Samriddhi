#Sort the bus routes based on the number of stops, using a custom sorting function.
#Sorting Bus Routes by Number of Stops
# Sample bus routes with their stop counts
bus_routes = {
    "Route A": ["Stop 1", "Stop 2", "Stop 3", "Stop 4"],
    "Route B": ["Stop 1", "Stop 2"],
    "Route C": ["Stop 1", "Stop 2", "Stop 3"],
    "Route D": ["Stop 1", "Stop 2", "Stop 3", "Stop 4", "Stop 5", "Stop 6"],
}

# Sort routes based on the number of stops
sorted_routes = sorted(bus_routes.items(), key=lambda x: len(x[1]))

# Display results
print("Bus Routes Sorted by Number of Stops:")
for route, stops in sorted_routes:
    print(f"{route}: {len(stops)} stops")
  
#Sorting in Descending Order (Most Stops First)
sorted_routes_desc = sorted(bus_routes.items(), key=lambda x: len(x[1]), reverse=True)

print("\nBus Routes Sorted by Most Stops First:")
for route, stops in sorted_routes_desc:
    print(f"{route}: {len(stops)} stops")
