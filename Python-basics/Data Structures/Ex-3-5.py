#Create a set of all unique stations in the system.
# Define stations for each train line
red_line = {"Central Station", "Main Street", "University", "Airport"}
blue_line = {"North End", "City Center", "Museum District", "South Park"}
green_line = {"Westside", "Stadium", "Downtown", "Eastside"}
yellow_line = {"Harbor", "Business District", "Grand Avenue", "Sunset Boulevard"}
purple_line = {"Tech Park", "Convention Center", "Shopping Mall", "Residential Area"}

# Use a set union to combine all unique stations
all_unique_stations = red_line | blue_line | green_line | yellow_line | purple_line  # Union operation

print(all_unique_stations)
