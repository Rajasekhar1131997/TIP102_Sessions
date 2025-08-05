"""
Problem 1: Graphing Flights
The following graph represents the different flights offered by CodePath Airlines. Each node or vertex represents an airport 
(JFK - New York City, LAX - Los Angeles, DFW - Dallas Fort Worth, and ATL - Atlanta), and an edge between two vertices indicates that 
CodePath airlines offers flights between those two airports.
Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is 
represented by a string with the airport's name (ex. "JFK").
"""
class GraphNode:
    def __init__(self, value, edges = None):
        self.val = value
        if not edges:
            self.edges = []
        else:
            self.edges = edges

print("--------Problem 1---------")
"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
flights = {
    "LAX": ["JFK"],
    "JFK": ["LAX", "DFW"],
    "DFW": ["JFK", "ATL"],
    "ATL" : ["DFW"]
}

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])
print("Time Complexity: O(V+E)")
print("Space Complexity: O(V+E)")

"""
Problem 2: There and Back
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID 
of a different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination 
in flights[i]. Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j 
there also exists a flight from destination j to destination i. Return False otherwise.
"""
def bidirectional_flights(flights):
    if not flights:
        return False
    n = len(flights)
    for i in range(n):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


print("--------Problem 2---------")
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
print("Time Complexity: O(N+E)")
print("Space Complexity: O(N+E)")

"""
Problem 3: Finding Direct Flights
Given an adjacency matrix flights of size n x n where each of the n nodes in the graph represent a distinct destination and n[i][j] = 1 
indicates that there exists a flight from destination i to destination j and n[i][j] = 0 indicates that no such flight exists. 
Given flights and an integer source representing the destination a customer is flying out of, return a list of all destinations the customer 
can reach from source on a direct flight. You may return the destinations in any order.
A customer can reach a destination on a direct flight if that destination is a neighbor of source.
"""
def get_direct_flights(flights, source):
    if not flights:
        return []
    result = []
    n = len(flights)
    for destination in range(n):
        if flights[source][destination] == 1:
            result.append(destination)
    return result

print("--------Problem 3---------")
flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 4: Converting Flight Representations
Given a list of edges flights where flights[i] = [a, b] denotes that there exists a bidirectional flight (incoming and outgoing flight) 
from city a to city b, return an adjacency dictionary adj_dict representing the same flights graph where adj_dict[a] is an array denoting 
there is a flight from city a to each city in adj_dict[a].
"""
def get_adj_dict(flights):
    if not flights:
        return {}
    graph = {}
    for source, destination in flights:
        graph.setdefault(source, []).append(destination)
        graph.setdefault(destination, []).append(source)
    return graph


print("--------Problem 4---------")
flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
print("Time Complexity: O(E)")
print("Space Complexity: O(V+E)")

"""
Problem 5: Find Center of Airport
You are a pilot navigating a new airport and have a map of the airport represented as an undirected star graph with n nodes where each node 
represents a terminal in the airport labeled from 1 to n. You want to find the center terminal in the airport where the pilots' lounge is 
located. Given a 2D integer array terminals where each terminal[i] = [u, v] indicates that there is a path (edge) between terminal u and v, 
return the center of the given airport. 
A star graph is a graph where there is one center node and exactly n-1 edges connecting the center node ot every other node.
"""
def find_center(terminals):
    if not terminals:
        return None
    count = {}
    for source, destination in terminals:
        count[source] = count.get(source, 0) + 1
        count[destination] = count.get(destination, 0) + 1
    for terminal, center in count.items():
        if center > 1:
            return terminal

print("--------Problem 5---------")
terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 6: Finding All Reachable Destinations
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a 
starting airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, 
and the corresponding value is a list of other destinations that are reachable through a direct flight.
Given a starting location start, return a list of all destinations reachable from the start location either through a direct flight or 
connecting flights with layovers. The list should be provided in ascending order by number of layovers required.
"""
# Breadth First Search Traversal of a graph
from collections import deque
def get_all_destinations(flights, start):
    if not flights:
        return []
    queue = deque([start])
    visited = set([start])

    reachable = []
    while queue:
        current = queue.popleft()
        reachable.append(current)

        for neighbor in flights.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return reachable

print("--------Problem 6---------")
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
print("Time Complexity: O(V+E)")
print("Space Complexity: O(V)")

"""
Problem 7: Finding All Reachable Destinations II
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a 
starting airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, 
and the corresponding value is a list of other destinations that are reachable through a direct flight.
Given a starting location start, write a function get_all_destinations() that uses Depth First Search (DFS) to return a list of all 
destinations that can be reached from start. The list should include both direct and connecting flights and should be ordered based 
on the order in which airports are visited in DFS.
"""
# Depth First Search Traversal of a graph
def get_all_destinations(flights, start):
    if not flights:
        return []
    result = []
    visited = set()
    def dfs(airport):
        visited.add(airport)
        result.append(airport)
        for neighbor in flights.get(airport, []):
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)

    return result

print("--------Problem 7---------")
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
print("Time Complexity: O(V+E)")
print("Space Complexity: O(V)")

"""
Problem 8: Find Itinerary
You are a traveler about to embark on a multi-leg journey with multiple flights to arrive at your final travel destination. 
You have all your boarding passes, but their order has gotten all messed up! You want to organize your boarding passes in the order you will 
use them, from your first flight all the way to your last flight that will bring you to your final destination.
Given a list of edges boarding_passes where each element boarding_passes[i] = (departure_airport, arrival_airport) represents a flight 
from departure_airport to arrival_airport, return an array with the itinerary listing out the airports you will pass through in the order 
you will visit them. Assume that departure is scheduled from every airport except the final destination, and each airport is visited only once 
(i.e., there are no cycles in the route).
"""
def find_itinerary(boarding_passes):
    if not boarding_passes:
        return []
    


print("--------Problem 8---------")
boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))