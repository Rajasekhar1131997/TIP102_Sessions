"""
Problem 1: Haunted Mirror
A vampire has come to stay at the haunted hotel, but he can't see his reflection! What's more, he doesn't seem to be able to see the 
reflection of anything in the mirror! He's asked you to come to his aid and help him see the reflections of different thngs.
Given the root of a binary tree vampire, return the mirror image of the tree. The mirror image of a tree is obtained by flipping the tree 
along its vertical axis, meaning that the left and right children of all non-leaf nodes are swapped.
Evaluate the time complexity of your function. Define your variables and provide a rationale for why you 
believe your solution has the stated time complexity.
"""
from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
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


def mirror_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)

    return root

print("--------Problem 1---------")
"""
      🧛‍♂️
     /   \
    💪🏼    🤳
    /      \
   👟       👞
"""
# Using build_tree() function included at the top of the page
body_parts = [1, 2, 3, 4, None, None, 5]
vampire = build_tree(body_parts)


"""
      🎃
     /   \
    😈    🕸️
         /  \
       🧟‍♂️    👻
"""
spooky_objects = [5, 6, 7, None, None, 8, 9]
spooky_tree = build_tree(spooky_objects)

# Using print_tree() function included at the top of the page
print_tree(mirror_tree(vampire))
print_tree(mirror_tree(spooky_tree))
print("Time Complexity: O(N)")
print("Space Complexity: O(N) for skewed trees")

"""
Problem 2: Pumpkin Patch Path
Leaning into the haunted hotel aesthetic, you've begun growing a pumpkin patch behind the hotel for the upcoming Halloween season. 
Given the root of a binary tree where each node represents a section of a pumpkin patch with a certain number of pumpkins, 
find the root-to-leaf path that yields the largest number of pumpkins. Return a list of the node values along the maximum pumpkin path.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# Using DFS Approach:
def max_pumpkins_path(root):
    if not root:
        return []
    left_path = max_pumpkins_path(root.left)
    right_path = max_pumpkins_path(root.right)

    if sum([root.val] + left_path) > sum([root.val] + right_path):
        return [root.val] + left_path
    else:
        return [root.val] + right_path

#Using BFS Approach:
def max_pumpkins_path(root):
    if not root:
        return []
    max_sum = float('-inf')
    max_path = []
    queue = deque()
    queue.append((root, [root.val], root.val))
    while queue:
        node, path, total = queue.popleft()

        if not node.left and not node.right:
            if total > max_sum:
                max_sum = total
                max_path = path
        else:
            if node.left:
                queue.append((node.left, path + [node.left.val], node.left.val))
            if node.right:
                queue.append((node.right, path +[node.right.val], node.right.val))
    return max_path

print("--------Problem 2---------")

"""
    7
   / \
  3   10
 /   /  \
1   5    15
"""
# Using build_tree() function includedd at the top of the page
pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
root1 = build_tree(pumpkin_quantities)

"""
    12
   /  \
  3     8
 / \     \
4   50    10
"""
pumpkin_quantities = [12,3, 8, 4, 50, None, 10]
root2 = build_tree(pumpkin_quantities)

print(max_pumpkins_path(root1))
print(max_pumpkins_path(root2))
print("Time Complexity using DFS Approach: O(N)")
print("Space Complexity using DFS Approach: O(N)")

"""
Problem 3: Largest Pumpkin in each Row
Given the root of a binary tree pumpkin_patch where each node represents a pumpkin in the patch and each node value represents the 
pumpkin's size, return an array of the largest pumpkin in each row of the pumpkin patch. Each level in the tree represents a row of pumpkins.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def largest_pumpkins(pumpkin_patch):
    if not pumpkin_patch:
        return []
    result = []
    max_size = float('-inf')
    queue = deque([pumpkin_patch])
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            max_size = max(max_size, node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(max_size)
    return result

print("--------Problem 3---------")
"""
    1
   /  \
  3    2
 / \    \   
5   3    9
"""
# Using build_tree() function included at the top of the page
pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
pumpkin_patch = build_tree(pumpkin_sizes)

print(largest_pumpkins(pumpkin_patch))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 4: Counting Room Clusters
Given the root of a binary tree hotel where each node represents a room in the hotel and each node value represents the theme of the room, 
return the number of distinct clusters in the hotel. A distinct cluster is defined as a group of connected rooms (connected by edges) 
where each room has the same theme (val).
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_clusters(hotel):
    def dfs(node,parent_val):
        if not node:
            return 0
        count = 1 if node.val != parent_val else 0

        count += dfs(node.left, node.val)
        count += dfs(node.right, node.val)
        
        return count
    return dfs(hotel, None)

print("--------Problem 4---------")
"""
     👻
   /    \
  👻     🧛🏾
 /  \      \
👻  🧛🏾      🧛🏾
"""
# Using build_tree() function included at the top of the page
themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
hotel = build_tree(themes)

print(count_clusters(hotel))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 5: Purging Unwanted Guests
There are unwanted visitors lurking in the rooms of your haunted hotel, and it's time for a clear out. Given the root of a binary tree 
hotel where each node represents a room in the hotel and each node value represents the guest staying in that room. 
You want to systematically remove visitors in the following order:
Collect the guests (values) of all leaf nodes and store them in a list. The leaf nodes may be stored in any order.
Remove all the leaf nodes.
Repeat until the hotel (tree) is empty.
Return a list of lists, where each inner list represents a collection of leaf nodes.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def purge_hotel(hotel):
    def collect_leaves(node, parent, is_left):
        if not node:
            return False
        if not node.left and not node.right:
            leaves.append(node.val)
            if parent:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            return True
        collect_leaves(node.left, node, True)
        collect_leaves(node.right, node, False)
        return False
    result = []
    while hotel:
        leaves = []
        if collect_leaves(hotel, None, False):
            hotel = None
        result.append(leaves)
    return result

print("--------Problem 5---------")
"""
      👻
     /  \
   😱   🧛🏾‍♀️
  /  \
 💀  😈
"""

# Using build_tree() function included at the top of the page
guests = [1, 2, 3, 4, 5]
hotel = build_tree(guests)

# Using print_tree() function included at the top of the page
print_tree(hotel)
print(purge_hotel(hotel))
print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")

"""
Problem 6: Sectioning Off Cursed Zones
You've been hearing mysterious wailing and other haunting noises emanating from the deepest depths of the hotel. To keep guests safe, 
you want to section off the deepest parts of the hotel but keep as much of the hotel open as possible.
Given the root of a binary tree hotel where each node represents a room in the hotel, return the root of the smallest subtree in the 
hotel such that it contains all the deepesnt nodes of the original tree.
The depth of a room (node) is the shortest distance from it to the root. A room is called the deepest if it has the largest depth possible 
among any rooms in the entire hotel. The subtree of a room is a tree consisting of that room, plus the set of all its descendants.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def smallest_subtree_with_deepest_rooms(hotel):
    pass


"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
        /  \ 
      😱   👻
"""
# Using build_tree() included at top of page
rooms = ["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"]
hotel1 = build_tree(rooms)

"""
      Lobby
     /     \
   101     102
     \
     💀
"""
rooms = ["Lobby", 101, 102, None, "💀"]
hotel2 = build_tree(rooms)

# Using print_tree() function included at top of page
print_tree(smallest_subtree_with_deepest_rooms(hotel1))
print_tree(smallest_subtree_with_deepest_rooms(hotel2))