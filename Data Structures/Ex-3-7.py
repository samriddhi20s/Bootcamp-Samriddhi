#Create a dictionary where each key is a route, and the value is a list of tuples representing scheduled stops (time, station).
# Dictionary mapping routes to scheduled stops
transit_schedule = {
    "Route 1 (Bus)": [
        ("6:00 AM", "Downtown"),
        ("6:15 AM", "Central Park"),
        ("6:30 AM", "Airport"),
        ("7:00 AM", "Downtown"),
        ("7:15 AM", "Central Park"),
        ("7:30 AM", "Airport")
    ],
    "Route 2 (Bus)": [
        ("6:30 AM", "City Center"),
        ("6:45 AM", "Library"),
        ("7:00 AM", "University"),
        ("7:30 AM", "City Center"),
        ("7:45 AM", "Library"),
        ("8:00 AM", "University")
    ],
    "Red Line (Train)": [
        ("5:00 AM", "Central Station"),
        ("5:10 AM", "Main Street"),
        ("5:20 AM", "University"),
        ("5:30 AM", "Airport"),
        ("6:00 AM", "Central Station"),
        ("6:10 AM", "Main Street"),
        ("6:20 AM", "University"),
        ("6:30 AM", "Airport")
    ],
    "Blue Line (Train)": [
        ("5:30 AM", "North End"),
        ("5:40 AM", "City Center"),
        ("5:50 AM", "Museum District"),
        ("6:00 AM", "South Park"),
        ("6:30 AM", "North End"),
        ("6:40 AM", "City Center"),
        ("6:50 AM", "Museum District"),
        ("7:00 AM", "South Park")
    ]
}

# Print schedule for a specific route
for time, station in transit_schedule["Red Line (Train)"]:
    print(f"Red Line Train - {time} at {station}")
