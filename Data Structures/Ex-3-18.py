#Use a Counter to find the most frequented stations in the network.
from collections import Counter

# Sample station visit data (each entry represents a passenger visiting a station)
station_visits = [
    "Central Station", "West End", "Central Station", "North Gate",
    "Central Station", "West End", "South Terminal", "North Gate",
    "Central Station", "South Terminal", "Central Station", "West End",
    "West End", "South Terminal", "West End", "Central Station"
]

# Count occurrences of each station
station_counts = Counter(station_visits)

# Display the station visit counts
print("Station Visit Counts:")
for station, count in station_counts.items():
    print(f"{station}: {count}")

# Find the most frequented stations
most_frequented = station_counts.most_common(3)  # Top 3 busiest stations

print("\nMost Frequented Stations:")
for station, count in most_frequented:
    print(f"{station}: {count} visits")
