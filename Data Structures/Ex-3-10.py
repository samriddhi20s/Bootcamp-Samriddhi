#Implement named tuples for more structured data.
from collections import namedtuple

# Define named tuples for structured data
BusStop = namedtuple("BusStop", ["time", "station"])
TrainStop = namedtuple("TrainStop", ["time", "station"])

# Define bus routes with named tuples
bus_routes = {
    "Route 1": [
        BusStop("6:00 AM", "Downtown"),
        BusStop("6:15 AM", "Central Park"),
        BusStop("6:30 AM", "Airport")
    ],
    "Route 2": [
        BusStop("6:30 AM", "City Center"),
        BusStop("6:45 AM", "Library"),
        BusStop("7:00 AM", "University")
    ]
}

# Define train lines with named tuples
train_lines = {
    "Red Line": [
        TrainStop("5:00 AM", "Central Station"),
        TrainStop("5:10 AM", "Main Street"),
        TrainStop("5:20 AM", "University"),
        TrainStop("5:30 AM", "Airport")
    ],
    "Blue Line": [
        TrainStop("5:30 AM", "North End"),
        TrainStop("5:40 AM", "City Center"),
        TrainStop("5:50 AM", "Museum District")
    ]
}

# Print structured data
print("Bus Routes Schedule:")
for route, stops in bus_routes.items():
    for stop in stops:
        print(f"{route} - {stop.time} at {stop.station}")

print("\nTrain Lines Schedule:")
for line, stops in train_lines.items():
    for stop in stops:
        print(f"{line} - {stop.time} at {stop.station}")
