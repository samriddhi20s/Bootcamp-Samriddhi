#Refactor the earlier schedules to use Schedule named tuples.
from collections import namedtuple

# Define a named tuple for Schedule
Schedule = namedtuple("Schedule", ["time", "station"])

# Define bus routes using Schedule named tuples
bus_routes = {
    "Route 1": [
        Schedule("6:00 AM", "Downtown"),
        Schedule("6:15 AM", "Central Park"),
        Schedule("6:30 AM", "Airport")
    ],
    "Route 2": [
        Schedule("6:30 AM", "City Center"),
        Schedule("6:45 AM", "Library"),
        Schedule("7:00 AM", "University")
    ]
}

# Define train lines using Schedule named tuples
train_lines = {
    "Red Line": [
        Schedule("5:00 AM", "Central Station"),
        Schedule("5:10 AM", "Main Street"),
        Schedule("5:20 AM", "University"),
        Schedule("5:30 AM", "Airport")
    ],
    "Blue Line": [
        Schedule("5:30 AM", "North End"),
        Schedule("5:40 AM", "City Center"),
        Schedule("5:50 AM", "Museum District")
    ]
}

print("Bus Routes Schedule:")
for route, stops in bus_routes.items():
    for stop in stops:
        print(f"{route} - {stop.time} at {stop.station}")

print("\nTrain Lines Schedule:")
for line, stops in train_lines.items():
    for stop in stops:
        print(f"{line} - {stop.time} at {stop.station}")
