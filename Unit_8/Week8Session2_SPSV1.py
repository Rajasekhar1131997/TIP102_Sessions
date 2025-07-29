"""
Problem 1: Monstera Madness
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of 
Monstera leaves that have an odd number of splits.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
from collections import deque
class TreeNode():
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

def count_odd_splits(root):
    if not root or root is None:
        return 0
    left_subtree = count_odd_splits(root.left)
    right_subtree = count_odd_splits(root.right)
    if root.val %2 != 0:
        return 1 + left_subtree + right_subtree
    else:
        return left_subtree + right_subtree

print("--------Problem 1---------")
"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
print("Time Complexity: O(N)")
print("Space Complexity: O(H)")

"""
Problem 2: Flower Finding
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) 
where each node represents a plant in the store. The plants are organized according to their names (vals) in alphabetical order in the BST.
Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True 
if the flower is present in the garden and False otherwise.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    if name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)

print("--------Problem 2---------")
"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower"))
print("Time Complexity: O(H) where H is the height of the tree, O(N) in the worst case for skewed tree, O(log N) for the average case")
print("Space Complexity: O(H) due to recursive call stack, O(N) in the worst case, O(log N) for the average case")

"""
Problem 3: Flower Finding II
Consider the following function non_bst_find_flower() which accepts the root of a binary tree inventory and a flower name, and returns True 
if a flower (node) with name exists in the binary tree. Unlike the previous problem, this tree is not a binary search tree.
Compare your solution to find_flower() in Problem 2 to the following solution. Discuss with your group: How is the code different? Why?
What is the time complexity of non_bst_find_flower()? How does it compare to the time complexity of find_flower() in Problem 2?
How would the time complexity of find_flower() from Problem 2 change if the tree inventory was not balanced?
"""
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def non_bst_find_flower(root, name):
#     if root is None:
#         return False
    
#     if root.val == name:
#         return True

#     return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def non_bst_find_flower(inventory, name):
    if not inventory:
        return False
    if inventory.val == name:
        return True
    left_subtree = non_bst_find_flower(inventory.left, name)
    right_subtree = non_bst_find_flower(inventory.right, name)
    return left_subtree or right_subtree

print("--------Problem 3---------")
"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower"))
print("Time Complexity: O(N)")
print("Space Complexity: O(H)")

"""
Problem 4: Adding a New Plant to the Collection
You have just purchased a new houseplant and are excited to add it to your collection! Your collection is meticulously organized 
using a Binary Search Tree (BST) where each node in the tree represents a houseplant in your collection, and houseplants are organized 
alphabetically by name (val).
Given the root of your BST collection and a new houseplant name, insert a new node with value name into your collection. Return the root 
of your updated collection. If another plant with name already exists in the tree, add the new node in the existing node's right subtree.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if root is None or not root:
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

def add_plant(collection, name):
    if not collection or collection is None:
        return TreeNode(name)
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else:
        collection.right = add_plant(collection.right, name)
    return collection

print("--------Problem 4---------")
"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
print_tree(add_plant(collection, "Aloe"))
print("Time Complexity: O(H), where H is the height of the tree and O(N) in the worst case")
print("Space Complexity: O(H), due to recursive call stack and, O(N) is the worst case")

"""
Problem 5: Sorting Plants by Rarity
You are going to a plant swap where you can exchange cuttings of your plants for new plants from other plant enthusiasts. You want to 
bring a mix of cuttings from both common and rare plants in your collection. You track your plant collection in a BST where each node 
has a key and a val. The val contains the plant name, and the key is an integer representing the plant's rarity. 
Plants are organized in the BST by their key.
To help choose which plants to bring, write a function sort_plants() which takes in the BST root collection and returns an array of plant 
nodes as tuples in the form (key, val) sorted from least to most rare. Sorted order can be achieved by performing an inorder traversal 
of the BST.
"""
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key      # Plant price
        self.val = value      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    result = []
    def inorder_traversal(node):
        if not node:
            return #exits the function early
        inorder_traversal(node.left)
        result.append((node.val, node.key))
        inorder_traversal(node.right)

    inorder_traversal(collection)
    return result


print("--------Problem 5---------")
"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 6: Finding a New Plant Within Budget
You are looking for a new plant and have a max budget. The plant store that you are shopping at stores their inventory in a BST where 
each node has a key representing the price of the plant and value cntains the plant's name. Plants are ordered by their prices. 
You want to find a plant that is close to but lower than your budget.
Given the root of the BST inventory and an integer budget, write a function pick_plant() that returns the plant with the highest price 
below budget. If no plant with a price strictly below budget exists, the function should return None.
"""
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def pick_plant(root, budget):
    closest = None
    while root:
        if root.val < budget:
            closest = root
            root = root.right
        else:
            root = root.left
    return closest.key if closest else None

print("--------Problem 6---------")
"""
               (50, "Fiddle Leaf Fig")
             /                       \
    (25, "Monstera")           (70, "Snake Plant")
       /        \                   /         \
(15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")
"""

# Using build_tree() function at the top of page
values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

print(pick_plant(inventory, 50)) 
print(pick_plant(inventory, 25)) 
print(pick_plant(inventory, 15))
print("Time Complexity: O(H), where H is the height of the tree, O(N) in the worst case if the tree is skewed. ")
print("Space Complexity: O(1)")


"""
Problem 7: Remove Plant
A plant in your houseplant collection has become infested with aphids, and unfortunately you need to throw it out. Given the root of a 
BST collection where each node represents a plant in your collection, and a plant name, remove the plant node with value name from the 
collection. Return the root of the modified collection. Plants are organized alphabetically in the tree by value.
If the node with name has two children in the tree, replace it with its inorder predecessor (rightmost node in its left subtree). 
You do not need to maintain a balanced tree. Pseudocode has been provided for you.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    # Find the node to remove
    # If the node has no children
        # Remove the node by setting parent pointer to None
    # If the node has one child
        # Replace the node with its child
    # If the node has two children
        # Find the inorder predecessor 
        # Replace the node's value with inorder predecessor value
        # Remove inorder predecessor
    # Return root of updated tree
    if not collection:
        return None
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        if collection is None and collection.right is None:
            return None
        if collection.left is None:
            return collection.right
        if collection.right is None:
            return collection.left
        predecessor = max_value_node(collection.left)
        collection.val = predecessor.val
        collection.left = remove_plant(collection.left,predecessor.val)

    return collection

def max_value_node(node):
    if not node:
        return None
    current = node
    while current.right:
        current = current.right
    return current


print("--------Problem 7---------")
"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))
print("Time Complexity: O(H), H is the height of the tree, O(log N) in worst case and if it's a balanced BST")
print("Space Complexity: O(H), due to recursive call stack, O(N) in the worst case")