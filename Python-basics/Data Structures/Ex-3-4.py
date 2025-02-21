#Use sets to handle unique elements in the transportation system.
bus_stops = {
    "Downtown", "Airport", "City Center", "University", 
    "Main Street", "Shopping Mall", "Eastside", "Westside"
}

# Adding a new stop (won't add duplicates)
bus_stops.add("Train Station")
bus_stops.add("Downtown") 
print(bus_stops)

red_line = {"Central Station", "Main Street", "University", "Airport"}
blue_line = {"North End", "City Center", "Museum District", "South Park"}
green_line = {"Westside", "Stadium", "Downtown", "Eastside"}
yellow_line = {"Harbor", "Business District", "Grand Avenue", "Sunset Boulevard"}

# Get all unique stations across all lines
all_train_stations = red_line | blue_line | green_line | yellow_line  # Union of sets

print(all_train_stations)

 # Finds common stations between Red and Blue lines
interchange_stations = red_line & blue_line 
print(f"Interchange stations between Red and Blue lines: {interchange_stations}")


