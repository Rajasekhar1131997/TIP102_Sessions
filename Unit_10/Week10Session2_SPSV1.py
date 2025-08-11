"""
Problem 1: Can Rebook Flight
Oh no! You're flight has been cancelled and you need to rebook. Given an adjacency matrix of today's flights flights where each flight is 
labeled 0 to n-1 and flights[i][j] = 1 indicates that there is an available flight from location i to location j, return True if there exists 
a path from your current location source to your final destination dest. Otherwise return False.
Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time complexity.
"""
from collections import deque
def can_rebook(flights, source, dest):
    n = len(flights)
    if not flights:
        return False
    queue = deque([source])
    visited = set([source])
    while queue:
        current = queue.popleft()

        if current == dest:
            return True
        
        for flight in range(n):
            if flights[current][flight] == 1 and flight not in visited:
                queue.append(flight)
                visited.add(flight)
    return False
    

print("--------Problem 1---------")
flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2))
print("Space Complexity: O(N^2)")
print("Space Complexity: O(N)")

"""
Problem 2: Can Rebook Flight II
If you solved the above problem can_rebook() using Breadth First Search, try solving it using Depth First Search. If you solved it using 
Depth First Search, solve it using Breadth First Search.
Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated 
time complexity.
"""
def can_rebook(flights, source, dest):
    visited = set()
    def dfs(current):
        if current == dest:
            return True
        visited.add(current)
        for flight, connected in enumerate(flights[current]):
            if connected == 1 and flight not in visited:
                if dfs(flight):
                    return True
                
        return False
    return dfs(source)


print("--------Problem 2---------")
flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2))
print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")

"""
Problem 3: Number of Flights
You are a travel planner and have an adjacency matrix flights with n airports labeled 0 to n-1 where flights[i][j] = 1 indicates CodePath 
Airlines offers a flight from airport i to airport j. You are planning a trip for a client and want to know the minimum number of 
flights (edges) it will take to travel from airport start to their final destination airport destination on CodePath Airlines.
Return the minimum number of flights needed to travel from airport i to airport j. If it is not possible to fly from airport i to airport j, 
return -1.
"""
def counting_flights(flights, i, j):
    n = len(flights)
    if i == j:
        return 0
    queue = deque([(i, 0)])
    visited = set([i])
    while queue:
        current, num_flights = queue.popleft()
        for next_airport in range(n):
            if flights[current][next_airport] == 1 and next_airport not in visited:
                if next_airport == j:
                    return num_flights + 1
                queue.append((next_airport, num_flights+1))
                visited.add(next_airport)
    return -1

print("--------Problem 3---------")
# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")

"""
Problem 4: Number of Airline Regions
CodePath Airlines operates in different regions around the world. Some airports are connected directly with flights, while others are not. 
However, if airport a is connected directly to airport b, and airport b is connected directly to airport c, then airport a is indirectly 
connected to airport c. An airline region is a group of directly or indirectly connected airports and no other airports outside of the group.
You are given an n x n matrix is_connected where is_connected[i][j] = 1 if CodePath Airlines offers a direct flight between airport i and 
airport j, and is_connected[i][j] = 0 otherwise.
Return the total number of airline regions operated by CodePath Airlines.
"""
def num_airline_regions(is_connected):
    pass


is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 
print("Time Complexity: ")
print("Space Complexity: ")