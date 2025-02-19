#Define a named tuple Schedule with fields for time and station.
from collections import namedtuple

# Define a named tuple for Schedule
Schedule = namedtuple("Schedule", ["time", "station"])

# Example usage: Creating bus and train schedules
bus_schedule = [
    Schedule("6:00 AM", "Downtown"),
    Schedule("6:15 AM", "Central Park"),
    Schedule("6:30 AM", "Airport")
]

train_schedule = [
    Schedule("5:00 AM", "Central Station"),
    Schedule("5:10 AM", "Main Street"),
    Schedule("5:20 AM", "University"),
    Schedule("5:30 AM", "Airport")
]

# Print schedules
print("Bus Schedule:")
for stop in bus_schedule:
    print(f"At {stop.time}, arriving at {stop.station}")

print("\nTrain Schedule:")
for stop in train_schedule:
    print(f"At {stop.time}, arriving at {stop.station}")
