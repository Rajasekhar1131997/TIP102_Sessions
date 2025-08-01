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

def max_pumpkins_path(root):
    if not root:
        return None

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
    pass

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

print(count_clusters(themes))