# Data Structures in Python

This document explores fundamental data structures in Python by modeling a transportation system. The focus is on organizing, managing, and analyzing bus routes, train lines, and schedules.

## Basic Data Structures
- Create a list of bus routes.
- Create a dictionary mapping train lines to their respective stations.

## Using Sets for Unique Elements
- Create a set of all unique stations in the transportation system.

## Nested Data Structures 
- Create a dictionary where each key is a route, and the value is a list of tuples representing scheduled stops (time, station).

## Aggregating Data
- Calculate the total number of unique stations served by both buses and trains.

## Using Named Tuples for Structure
- Define a named tuple `Schedule` with fields for `time` and `station`.
- Refactor schedules to use named tuples.

## Default Dictionaries for Missing Keys
- Create a default dictionary for tracking the number of passengers per station.

## Handling Complex Nesting
- Create a nested data structure that maps a transport line to its schedule, and each schedule to a list of passengers (by name).

## Data Analysis with Counter
- Use a `Counter` to find the most frequented stations in the network.

## Custom Sorting
- Sort the bus routes based on the number of stops using a custom sorting function.

## Building a Comprehensive Transportation Model
- Create a `TransportNetwork` class that integrates all previous data structures.
- Implement methods to add routes, update schedules, and add passengers.

This provides practical experience with Python's core data structures while modeling a real-world system.


