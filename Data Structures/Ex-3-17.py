#Utilize Counter from the collections module to analyze data.
from collections import Counter

# Sample Data
passenger_data = [
    "Central Station", "West End", "Central Station", "North Gate",
    "Central Station", "West End", "South Terminal", "North Gate",
    "Central Station", "South Terminal"
]

passenger_times = ["08:00 AM", "08:30 AM", "08:00 AM", "09:00 AM", "08:00 AM", "09:30 AM"]

passenger_names = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Eve"]

# Count occurrences
station_counts = Counter(passenger_data)
time_counts = Counter(passenger_times)
name_counts = Counter(passenger_names)

# Display results
print("Passenger Count per Station:")
print(station_counts)
print("\nMost Common Station:", station_counts.most_common(1))

print("\nPassenger Count per Time Slot:")
print(time_counts)
print("\nBusiest Time Slot:", time_counts.most_common(1))

print("\nPassenger Name Frequency:")
print(name_counts)
print("\nMost Frequent Passengers:", name_counts.most_common(2))
