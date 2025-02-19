#Create a nested data structure that maps a transport line to its schedule, and each schedule to a list of passengers (by name).
from collections import defaultdict

# Function to create a nested defaultdict of lists
def nested_list():
    return defaultdict(list)

# Main transport structure
transport_schedule = defaultdict(nested_list)

# Example data: Adding passengers
transport_schedule["Blue Line"]["08:00 AM"].extend(["Alice", "Bob"])
transport_schedule["Blue Line"]["09:00 AM"].append("Charlie")
transport_schedule["Red Line"]["08:30 AM"].extend(["Dave", "Eve"])
transport_schedule["Green Line"]["10:00 AM"].append("Frank")

# Accessing data
print(transport_schedule["Blue Line"]["08:00 AM"])  # Output: ['Alice', 'Bob']
print(transport_schedule["Red Line"]["08:30 AM"])   # Output: ['Dave', 'Eve']

# Convert to a regular dictionary for better readability
import json
print(json.dumps(transport_schedule, indent=2))
