#Handle complex nesting in data structures.
from collections import defaultdict

# Function to create a deeply nested defaultdict
def nested_dict():
    return defaultdict(nested_dict)

# Initialize the complex structure
passenger_data = nested_dict()

# Example usage: Adding passenger counts
passenger_data["Blue Line"]["Central Station"]["08:00 AM"] += 10
passenger_data["Red Line"]["West End"]["09:30 AM"] += 5
passenger_data["Blue Line"]["Central Station"]["09:00 AM"] += 7

# Accessing data safely
print(passenger_data["Blue Line"]["Central Station"]["08:00 AM"])  # Output: 10
print(passenger_data["Red Line"]["West End"]["09:30 AM"])  # Output: 5

# Converting to a regular dictionary for readability
import json
print(json.dumps(passenger_data, indent=2))
