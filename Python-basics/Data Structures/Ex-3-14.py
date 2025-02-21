#Create a default dictionary for tracking the number of passengers per station.
from collections import defaultdict

# Default dictionary to track passengers per station
passenger_count = defaultdict(int)

# Example usage
passenger_count["Central Station"] += 5
passenger_count["West End"] += 3

print(passenger_count)
