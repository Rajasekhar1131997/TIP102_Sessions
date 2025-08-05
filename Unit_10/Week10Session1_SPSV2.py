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