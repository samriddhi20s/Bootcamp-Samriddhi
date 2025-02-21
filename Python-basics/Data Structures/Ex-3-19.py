#Apply custom sorting to collection data.
#Sort Stations by Number of Visits (Descending Order)
from collections import Counter

# Sample station visit data
station_visits = [
    "Central Station", "West End", "Central Station", "North Gate",
    "Central Station", "West End", "South Terminal", "North Gate",
    "Central Station", "South Terminal", "West End", "West End",
    "South Terminal", "West End", "Central Station"
]

# Count occurrences of each station
station_counts = Counter(station_visits)

# Sort stations by most visits (Descending order)
sorted_stations = sorted(station_counts.items(), key=lambda x: x[1], reverse=True)

print("Stations sorted by frequency:")
for station, count in sorted_stations:
    print(f"{station}: {count} visits")

#Sort Passengers Alphabetically Within Each Time Slot
from collections import defaultdict

# Sample transport schedule with passenger lists
transport_schedule = {
    "08:00 AM": ["Charlie", "Alice", "Bob"],
    "09:30 AM": ["Eve", "Dave", "Bob"],
    "10:00 AM": ["Frank", "Alice", "Eve"]
}

# Sort passengers alphabetically for each time slot
sorted_schedule = {time: sorted(passengers) for time, passengers in transport_schedule.items()}

print("\nSorted Passengers per Time Slot:")
for time, passengers in sorted_schedule.items():
    print(f"{time}: {passengers}")

# Sort Train Lines by Earliest Departure Time
from datetime import datetime

# Sample train schedule with departure times
train_schedule = {
    "Blue Line": "10:30 AM",
    "Red Line": "08:15 AM",
    "Green Line": "09:45 AM",
    "Yellow Line": "07:30 AM"
}

# Convert time to datetime format and sort
sorted_trains = sorted(train_schedule.items(), key=lambda x: datetime.strptime(x[1], "%I:%M %p"))

print("\nTrain Lines Sorted by Departure Time:")
for line, time in sorted_trains:
    print(f"{line}: {time}")
