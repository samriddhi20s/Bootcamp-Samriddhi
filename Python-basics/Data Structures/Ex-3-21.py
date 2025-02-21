#Combine different data structures to model a comprehensive transportation system.
#Create a class TransportNetwork that integrates all the previous data structures and provides methods to add routes, update schedules, and add passengers.
from collections import defaultdict, Counter
from datetime import datetime
import json

class TransportNetwork:
    def __init__(self):
        # Routes: Maps transport line -> list of stops
        self.routes = defaultdict(list)
        
        # Schedules: Maps transport line -> time slot -> list of passengers
        self.schedules = defaultdict(lambda: defaultdict(list))
        
        # Passenger Counts: Tracks most frequented stations
        self.station_visits = Counter()

    # Add a route with stops
    def add_route(self, line, stops):
        self.routes[line] = stops
        print(f"Added route: {line} with stops {stops}")

    # Add a schedule time slot for a route
    def add_schedule(self, line, time_slot):
        if line not in self.routes:
            print(f"Route {line} does not exist. Add it first.")
            return
        self.schedules[line][time_slot] = []
        print(f"Added schedule for {line} at {time_slot}")

    # Add a passenger to a specific route and time
    def add_passenger(self, line, time_slot, passenger, station=None):
        if line in self.schedules and time_slot in self.schedules[line]:
            self.schedules[line][time_slot].append(passenger)
            if station:
                self.station_visits[station] += 1
            print(f"Added passenger {passenger} to {line} at {time_slot}")
        else:
            print(f"Schedule {time_slot} for {line} does not exist.")

    # Get busiest stations
    def busiest_stations(self, top_n=3):
        return self.station_visits.most_common(top_n)

    # Get peak travel times
    def peak_travel_times(self, top_n=3):
        time_counts = Counter()
        for line in self.schedules:
            for time_slot, passengers in self.schedules[line].items():
                time_counts[time_slot] += len(passengers)
        return time_counts.most_common(top_n)

    # Sort routes by number of stops
    def sort_routes_by_stops(self, descending=False):
        return sorted(self.routes.items(), key=lambda x: len(x[1]), reverse=descending)

    
    def display_network(self):
        print("\nTransport Routes & Stops:")
        print(json.dumps(self.routes, indent=2))
        print("\nSchedules & Passengers:")
        print(json.dumps(self.schedules, indent=2))
        print("\nMost Frequented Stations:", self.busiest_stations())
        print("Peak Travel Times:", self.peak_travel_times())

# Example 
network = TransportNetwork()
network.add_route("Blue Line", ["Central Station", "West End", "North Gate"])
network.add_route("Red Line", ["Downtown", "Central Station", "South Terminal"])
network.add_schedule("Blue Line", "08:00 AM")
network.add_schedule("Red Line", "09:30 AM")
network.add_passenger("Blue Line", "08:00 AM", "Alice", "Central Station")
network.add_passenger("Blue Line", "08:00 AM", "Bob", "West End")
network.add_passenger("Red Line", "09:30 AM", "Charlie", "Downtown")

network.display_network()

# Sort routes by number of stops
print("\nRoutes sorted by number of stops:", network.sort_routes_by_stops())
