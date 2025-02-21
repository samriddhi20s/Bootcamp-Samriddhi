#Understand nested data structures by organizing schedules
# Transit schedule with nested dictionaries
transit_schedule = {
    "Bus Routes": {
        "Route 1": {
            "stops": ["Downtown", "Central Park", "Airport"],
            "schedule": {
                "Weekdays": ["6:00 AM", "8:00 AM", "10:00 AM", "12:00 PM"],
                "Weekends": ["7:00 AM", "9:00 AM", "11:00 AM"]
            }
        },
        "Route 2": {
            "stops": ["City Center", "Library", "University"],
            "schedule": {
                "Weekdays": ["6:30 AM", "8:30 AM", "10:30 AM", "12:30 PM"],
                "Weekends": ["7:30 AM", "9:30 AM", "11:30 AM"]
            }
        }
    },
    "Train Lines": {
        "Red Line": {
            "stations": ["Central Station", "Main Street", "University", "Airport"],
            "schedule": {
                "Weekdays": ["5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM"],
                "Weekends": ["6:00 AM", "7:00 AM", "8:00 AM"]
            }
        },
        "Blue Line": {
            "stations": ["North End", "City Center", "Museum District", "South Park"],
            "schedule": {
                "Weekdays": ["5:30 AM", "6:30 AM", "7:30 AM", "8:30 AM"],
                "Weekends": ["6:30 AM", "7:30 AM", "8:30 AM"]
            }
        }
    }
}

# Accessing data
print("Bus Route 1 Stops:", transit_schedule["Bus Routes"]["Route 1"]["stops"])
print("Red Line Weekday Schedule:", transit_schedule["Train Lines"]["Red Line"]["schedule"]["Weekdays"])
