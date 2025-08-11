"""
Problem 1: Hollywood Stars
The following graph illustrates connections between different Hollywood stars. Each node represents a celebrity, and an edge between two nodes 
indicates that the celebrities know each other.
Create a variable hollywood_stars that represents the undirected graph below as an adjacency dictionary, 
where each node's value is represented by a string with the airport's name (ex. "Kevin Bacon").
"""

class GraphNode:
    def __init__(self, value, edges = None):
        self.val = value
        if not self.edges:
            self.edges = []
        else:
            self.edges = edges

hollywood_stars = {
    'Kevin Bacon': ['Laverne Cox', 'Sofia Vergara'],
    'Meryl Streep': ['Idris Elba', 'Sofia Vergara'],
    'Idris Elba': ['Meryl Streep', 'Laverne Cox'],
    'Laverne Cox': ['Kevin Bacon', 'Idris Elba'],
    'Sofia Vergara': ['Sofia Vergara', 'Meryl Streep']
}

print("--------Problem 1---------")
print(list(hollywood_stars.keys()))
print(list(hollywood_stars.values()))
print(hollywood_stars["Kevin Bacon"])
print("Time Complexity: O(V+E)")
print("Space Complexity: O(V+E)")

"""
Problem 2: The Feeling is Mutual
You are given an insider look into the Hollywood gossip with an adjacency matrix celebrities where each node labeled 0 to n represents a 
celebrity. celebrities[i][j] = 1 indicates that celebrity i likes celebrity j and celebrities[i][j] = 0 indicates that celebrity i 
dislikes or doesn't know celebrity j. Write a function is_mutual() that returns True if all relationships between celebrities are mutual 
and False otherwise. A relationship between two celebrities is mutual if for any celebrity i that likes celebrity j, celebrity j also likes 
celebrity i.
"""
def is_mutual(celebrities):
    if not celebrities:
        return False
    n = len(celebrities)
    for i in range(n):
        for j in range(n):
            if celebrities[i][j] == 1 and celebrities[j][i] == 0:
                return False
    return True

print("--------Problem 2---------")
celebrities1 = [
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

print(is_mutual(celebrities1))
print(is_mutual(celebrities2))
print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")

"""
Problem 3: Closest Friends
You are a talented actor looking for your next big movie and want to leverage your connections to see if there are any good roles available. 
To increase your chances, you want to ask your closest friends first.
You have a 2D list contacts where contacts[i] = [celebrity_a, celebrity_b] indicates that there is a mutual relationship (undirected edge) 
between celebrity_a and celebrity_b. Given a celebrity celeb, return a list of the celebrity's closest friends.
celebrity_b is a close friend of celebrity_a if they are neighbors in the graph.
"""
def get_close_friends(contacts, celeb):
    if not contacts:
        return []
    graph = {}
    for contact in contacts:
        celebrity_a, celebrity_b = contact
        if celebrity_a not in graph:
            graph[celebrity_a] = []
        if celebrity_b not in graph:
            graph[celebrity_b] = []
        graph[celebrity_a].append(celebrity_b)
        graph[celebrity_b].append(celebrity_a)
    
    return graph.get(celeb, [])


print("--------Problem 3---------")
contacts = [["Lupita Nyong'o", "Jordan Peele"], ["Meryl Streep", "Jordan Peele"], ["Meryl Streep", "Lupita Nyong'o"], 
["Greta Gerwig", "Meryl Streep"], ["Ali Wong", "Greta Gergwig"]]

print(get_close_friends(contacts, "Lupita Nyong'o"))
print(get_close_friends(contacts, "Greta Gerwig"))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 4: Network Lookup
You work for a talent agency and have a 2D list clients where clients[i] = [celebrity_a, celebrity_b] indicates that celebrity_a and celebrity_b 
have worked with each other. You want to create a more efficient lookup system for your agency by transforming clients into an equivalent 
adjacency matrix.
Given contacts:
Create a map of each unique celebrity in contacts to an integer ID with values 0 through n.
Using the celebrities' IDs, create an adjacency matrix where matrix[i][j] = 1 indicates that celebrity with ID i has worked with celebrity 
with ID j. Otherwise, matrix[i][j] should have value 0. Return both the dictionary mapping celebrities to their ID and the adjacency matrix.
"""
def get_adj_matrix(clients):
    if not clients:
        return {}, []
    unique_celebs = set()
    for pair in clients:
        unique_celebs.update(pair)

    celeb_to_ids = {}
    for index, celebrity in enumerate(unique_celebs):
        celeb_to_ids[celebrity] = index
    
    n = len(celeb_to_ids)
    adj_matrix = [[0] * n for _ in range(n)]

    for celeb_a, celeb_b in clients:
        id_a = celeb_to_ids[celeb_a]
        id_b = celeb_to_ids[celeb_b]
        adj_matrix[id_a][id_b] = 1
        adj_matrix[id_b][id_a] = 1
    
    return celeb_to_ids, adj_matrix

print("--------Problem 4---------")
clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]

id_map, adj_matrix = get_adj_matrix(clients)
print(id_map)
print(adj_matrix)
print("Time Complexity: O(N)")
print("Space Complexity: O(N^2) for storing adjacency matrix and O(N) for mapping dictionary")

"""
Problem 5: Secret Celebrity
A new reality show is airing in which a famous celebrity pretends to be a non-famous person. As contestants get to know each other, 
they have to guess who the celebrity among them is to win the show. An even bigger twist: there might be no celebrity at all! 
The show has n contestants labeled from 1 to n.
If the celebrity exists, then:
The celebrity trusts none of the contestants.
Due to the celebrity's charisma, all the contestants trust the celebrity.
There is exactly one person who satisfies rules 1 and 2.
You are given an array trust where trust[i] = [a, b] indicates that contestant a trusts contestant b. If a trust relationship does not exist 
in trust array, then such a trust relationship does not exist.
Return the label of the celebrity if they exist and can be identified. Otherwise, return -1.
"""
def identify_celebrity(trust, n):
    trust_count = [0] * (n+1)
    trusted_by = [0] * (n+1)

    for a, b in trust:
        trust_count[b] += 1
        trusted_by[a] += 1

    for i in range(1, n+1):
        if trust_count[i] == n-1 and trusted_by[i] == 0:
            return i
    
    return -1

print("--------Problem 5---------")
trust1 = [[1,2]]
trust2 = [[1,3],[2,3]]
trust3 = [[1,3],[2,3],[3,1]]

print(identify_celebrity(trust1, 2))
print(identify_celebrity(trust2, 3))
print(identify_celebrity(trust3, 3))
print("Time Complexity: O(N+T)")
print("Space Complexity: O(N)")

"""
Problem 6: Casting Call Search
You are a casting agent for a major Hollywood production and the director has a certain celebrity in mind for the lead role. You have an 
adjacency matrix celebs where celebs[i][j] = 1 means that celebrity i has a connection with celebrity j, and celebs[i][j] = 0 means they don't. 
Connections are directed meaning that celebs[i][j] = 1 does not automatically mean celebs[j][i] = 1.
Given a celebrity you know start_celeb and the celebrity the director wants to hire target_celeb, use Breadth First Search to return True 
if you can find a path of connections from start_celeb to target_celeb. Otherwise, return False.
"""
from collections import deque
def have_connection(celebs, start_celeb, target_celeb):
    n = len(celebs)
    queue = deque([start_celeb])
    visited = set([start_celeb])

    while queue:
        current = queue.popleft()

        if current == target_celeb:
            return True
        
        for neighbor in range(n):
            if celebs[current][neighbor] == 1 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return False

print("--------Problem 6---------")
celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0], # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0], # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0], # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]  # Celeb 7
            ]

print(have_connection(celebs, 0, 6))
print(have_connection(celebs, 3, 5))
print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")

"""
Problem 7: Casting Call Search II
You are a casting agent for a major Hollywood production and the director has a certain celebrity in mind for the lead role. You have an 
adjacency matrix celebs where celebs[i][j] = 1 means that celebrity i has a connection with celebrity j, and celebs[i][j] = 0 means they don't. 
Connections are directed meaning that celebs[i][j] = 1 does not automatically mean celebs[j][i] = 1.
Given a celebrity you know start_celeb and the celebrity the director wants to hire target_celeb, use Depth First Search to return True if 
you can find a path of connections from start_celeb to target_celeb. Otherwise, return False.
"""
def have_connection(celebs, start_celeb, target_celeb):
    visited = set()

    def dfs(current):
        if current == target_celeb:
            return True
        visited.add(current)
        for neighbor, connected in enumerate(celebs[current]):
            if connected == 1 and neighbor not in visited:
                if dfs(neighbor):
                    return True
    return dfs(start_celeb)


print("--------Problem 7---------")
celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0], # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0], # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0], # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]  # Celeb 7
            ]

print(have_connection(celebs, 0, 6))
print(have_connection(celebs, 3, 5))
print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")

"""
Problem 8: Copying Seating Arrangements
You are organizing the seating arrangement for a big awards ceremony and want to make a copy for your assistant. The seating arrangement is 
stored in a graph where each Node value val is the name of a celebrity guest at the ceremony and its array neighbors are all the guests 
sitting in seats adjacent to the celebrity. Given a reference to a Node in the original seating arrangement seat, make a deep copy (clone) 
of the seating arrangement. Return the copy of the given node. We have provided a function compare_graphs() to help with testing this function. 
To use this function, pass in the given node seat and the copy of that node your function copy_seating() returns. If the two graphs are 
clones of each other, the function will return True. Otherwise, the function will return False.
"""
class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Function to test if two seating arrangements (graphs) are identical
def compare_graphs(node1, node2, visited=None):
    if visited is None:
        visited = set()
    
    if node1.val != node2.val:
        return False
    
    visited.add(node1)

    if len(node1.neighbors) != len(node2.neighbors):
        return False
    
    for n1, n2 in zip(node1.neighbors, node2.neighbors):
        if n1 not in visited and not compare_graphs(n1, n2, visited):
            return False

    return True

def copy_seating(seat):
    old_to_new = {}

    def dfs(node):
        if node is None:
            return None
        if node in old_to_new:
            return old_to_new[node]
        
        copy = Node(node.val)
        old_to_new[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy
    
    return dfs(seat)

print("--------Problem 8---------")
lily = Node("Lily Gladstone")
mark = Node("Mark Ruffalo")
cillian = Node("Cillian Murphy")
danielle = Node("Danielle Brooks")
lily.neighbors.extend([mark, danielle])
mark.neighbors.extend([lily, cillian])
cillian.neighbors.extend([danielle, mark])
danielle.neighbors.extend([lily, cillian])

copy = copy_seating(lily)
print(compare_graphs(lily, copy))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")