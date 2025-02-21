#Explore default dictionaries for handling missing keys gracefully.
from collections import defaultdict, namedtuple

# Define a named tuple for structured scheduling
Schedule = namedtuple("Schedule", ["time", "station"])

# Create a defaultdict with a default value of an empty list
bus_routes = defaultdict(list)
train_lines = defaultdict(list)

# Populate bus schedules
bus_routes["Route 1"].extend([
    Schedule("6:00 AM", "Downtown"),
    Schedule("6:15 AM", "Central Park"),
    Schedule("6:30 AM", "Airport")
])

bus_routes["Route 2"].extend([
    Schedule("6:30 AM", "City Center"),
    Schedule("6:45 AM", "Library"),
    Schedule("7:00 AM", "University")
])

# Populate train schedules
train_lines["Red Line"].extend([
    Schedule("5:00 AM", "Central Station"),
    Schedule("5:10 AM", "Main Street"),
    Schedule("5:20 AM", "University"),
    Schedule("5:30 AM", "Airport")
])

train_lines["Blue Line"].extend([
    Schedule("5:30 AM", "North End"),
    Schedule("5:40 AM", "City Center"),
    Schedule("5:50 AM", "Museum District")
])

# Accessing a non-existent route (no KeyError due to defaultdict)
print("Checking a missing bus route:")
print(bus_routes["Route 99"])  # Returns [] 

print("\nBus Routes Schedule:")
for route, stops in bus_routes.items():
    for stop in stops:
        print(f"{route} - {stop.time} at {stop.station}")

print("\nTrain Lines Schedule:")
for line, stops in train_lines.items():
    for stop in stops:
        print(f"{line} - {stop.time} at {stop.station}")
