"""
Problem 1: Clone Detection
You have just started a new job working the night shift at a local hotel, but strange things have been happening and you're starting to 
think it might be haunted. Lately, you think you've been seeing double of some of the guests.
Given the roots of two binary trees guest1 and guest2 each representing a guest at the hotel, write a function that returns True 
if they are clones of each other and False otherwise.
Two binary trees are considered clones if they are structurally identical, and the nodes have the same values.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_clone(guest1, guest2):
    if not guest1 and not guest2:
        return True
    if not guest1 or not guest2:
        return False
    
    return (guest1.val == guest2.val and is_clone(guest1.left, guest2.left) and is_clone(guest1.right, guest2.right))


print("--------Problem 1---------")
"""
     John Doe               John Doe
     /      \             /       \
  6 ft    Brown Eyes      6ft      Brown Eyes
"""
guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))

"""
     John Doe         John Doe
     /                       \
   6 ft                     6 ft
"""
guest3 = TreeNode("John Doe", TreeNode("6 ft"))
guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))

print(is_clone(guest1, guest2))
print(is_clone(guest3, guest4))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 2: Mapping a Haunted Hotel
Guests have been coming to check out of rooms that you're pretty sure don't exist in the hotel... or are you imagining things? 
To make sure, you want to explore the entire hotel and make your own map.
Given the root of a binary tree hotel where each node represents a room in the hotel, write a function map_hotel() that returns a 
list of each room value in the hotel. You should explore the hotel level by level from left to right.
Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has 
the stated time complexity. Assume the input tree is balanced when calculating time complexity.
Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem, 
we recommend that you reference these functions as little as possible while implementing your solution.
"""
from collections import deque
class Room():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def map_hotel(hotel):
    if not hotel:
        return []
    result = []
    queue = deque([hotel])
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


print("--------Problem 2---------")
"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
   /                \ 
 301                302
"""

hotel = Room("Lobby", 
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))

print(map_hotel(hotel))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 3: Minimum Depth of Secret Path
You've found a strange door in the hotel and aren't sure where it leads. Given the root of a binary tree door where each node represents 
a destination along a path behind the door, return the minimum depth of the tree.
The minimum depth is the number of nodes along the shortest path from from the root node down to the nearest leaf node.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class Room():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def min_depth(door):
    if not door:
        return 0
    if not door.left and not door.right:
        return 1
    if not door.left:
        return 1 + min_depth(door.right)
    if not door.right:
        return 1 + min_depth(door.left)
    return 1 + min(min_depth(door.left), min_depth(door.right))
    

print("--------Problem 3---------")
"""
     Door
    /    \
 Attic    Cursed Room
         /       \
      Crypt     Haunted Cellar
"""

door = Room("Door", Room("Attic"), Room("Cursed Room", Room("Crypt"), Room("Haunted Cellar")))

print(min_depth(door))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 4: Minimum Depth of Secret Path II
If you used a breadth first search approach to solve the previous problem, reimplement your solution using a depth first search approach. 
If you used a depth first search approach, try using a breadth first search approach.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class Room():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def min_depth(door):
    if not door:
        return 0
    queue = deque([(door, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

print("--------Problem 4---------")
"""
     Door
    /    \
 Attic    Cursed Room
         /       \
      Crypt     Haunted Cellar
"""

door = Room("Door", Room("Attic"), Room("Cursed Room", Room("Crypt"), Room("Haunted Cellar")))

print(min_depth(door))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 5: Reverse Odd Levels of the Hotel
A poltergeist has been causing mischief and reversed the order of rooms on odd level floors. Given the root of a binary tree hotel where 
each node represents a room in the hotel and the root, restore order by reversing the node values at each odd level in the tree.
For example, suppose the rooms on level 3 have values [308, 307, 306, 305, 304, 303, 302, 301]. It should become [301, 302, 303, 304, 305, 306, 307, 308].
Return the root of the altered tree. A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
The level of a node is the number of edges along the path between it and the root node. Evaluate the time complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is 
balanced when calculating time complexity.
"""
class Room():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Using Depth First Search Approach
def reverse_odd_levels(hotel):
    if not hotel:
        return None
    
    def dfs(node1, node2, level):
        if not node1 or not node2:
            return
        if level % 2 == 1:
            node1.val, node2.val = node2.val, node1.val
        dfs(node1.left, node2.right, level+1)
        dfs(node1.right, node2.left, level+1)

    dfs(hotel.left, hotel.right, 1)
    return hotel

# Using Breadth First Search Approach
def reverse_odd_levels(hotel):
    if not hotel:
        return None
    queue = deque([hotel])
    level = 0
    while queue:
        level_size = len(queue)
        result = []
        for i in range(level_size):
            node = queue.popleft()
            result.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
            if level % 2 == 1:
                i, j = 0, len(result) - 1
                while i < j:
                    result[i].val, result[j].val = result[j].val, result[i].val
                    i += 1
                    j -= 1
        level += 1
    return hotel
    

print("--------Problem 5---------")
"""
        Lobby
      /      \
     102     101
     / \     /  \
   201 202 203 204 
"""
hotel = Room("Lobby", 
            Room(102, Room(201), Room (202)), 
                Room(101, Room(203), Room(204)))

# Using print_tree() function included at the top
print_tree(reverse_odd_levels(hotel))
print("Time Complexity For DFS Approach: O(N)")
print("Space Complexity for DFS Approach: O(log N) due to recursive stack on the balanced Binary search Tree")
print("Time Complexity for BFS Approach: O(N)")
print("Space Complexity for BFS Approach: O(N)")

"""
Problem 6: Kth Spookiest Room in the Hotel
Over time, your hotel has gained a reputation for being haunted, and you now have customers coming specifically for a spooky experience. 
You are given the root of a binary search tree (BST) with n nodes where each node represents a room in the hotel and each node has an 
integer key representing the spookiness of the room (1 being most spooky and n being least spooky) and val representing the room number. 
The tree is organized according to its keys. Given the root of a BST and an integer k write a function kth_spookiest() that returns the 
value of the kth spookiest room (smallest key, 1-indexed) of all the rooms in the hotel.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def kth_spookiest(root, k):
    count = 0
    result = None
    def inorder(root):
        nonlocal count, result
        if not root or result is not None:
            return
        inorder(root.left)
        count += 1
        if count == k:
            result = root.val
        inorder(root.right)
    
    inorder(root)
    return result

print("--------Problem 6---------")
"""
    (3, Lobby) 
   /         \
(1, 101)   (4, 102)
     \
     (2, 201)
"""

# Using build_tree() function at the top of the page
rooms = [(3, "Lobby"), (1, 101), (4, 102), None, (2, 201)]
hotel1 = build_tree(rooms)


"""
            (5, Lobby) 
            /         \
        (3, 101)   (6, 102)
        /      \
    (2, 201)  (4, 202)
    /
(1, 301)
"""
rooms = [(5, 'Lobby'), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]
hotel2 = build_tree(rooms)

print(kth_spookiest(hotel1, 1))
print(kth_spookiest(hotel2, 3))
print("Time Complexity: O(N)")
print("Space Complexity: O(H)")