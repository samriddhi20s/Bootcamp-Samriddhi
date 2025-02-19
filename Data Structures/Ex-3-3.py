#Create a dictionary mapping train lines to their respective stations.
train_lines = {
    "Red Line": ["Central Station", "Main Street", "University", "Airport"],
    "Blue Line": ["North End", "City Center", "Museum District", "South Park"],
    "Green Line": ["Westside", "Stadium", "Downtown", "Eastside"],
    "Yellow Line": ["Harbor", "Business District", "Grand Avenue", "Sunset Boulevard"],
    "Purple Line": ["Tech Park", "Convention Center", "Shopping Mall", "Residential Area"]
}

# Print all train lines and their stations
for line, stations in train_lines.items():
    print(f"{line}: {', '.join(stations)}")
