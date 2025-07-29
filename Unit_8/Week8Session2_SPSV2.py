"""
Problem 1: Find Lonely Cichlids
Sibling cichlid fish often form strong bonds after hatching, staying close to each other for protection. Given the root of a binary tree 
representing a family of cichlids where each node is a cichlid, return an array containing the values of all lonely cichlids in the family. 
A lonely cichlid is a fish (node) that is the only child of its parent. The matriarch (root) is not lonely because it does not have a parent. 
Return the array in any order.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
from collections import deque
class Cichlid:
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
  root = Cichlid(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = Cichlid(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = Cichlid(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def find_lonely_cichlids(root):
    if not root:
        return []
    lonely = []

    def dfs(node):
        if not node:
            return
        if node.left and not node.right:
            lonely.append(node.left.val)
        if node.right and not node.left:
            lonely.append(node.right.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return lonely
"""
     A
    / \
   B   C
  /   / \ 
 D   E   F
          \
           G
"""

print("--------Problem 1---------")
"""
    A
   / \
  B   C
   \
    D
"""

# Using build_tree() function at the top of page
values = ['A', 'B', 'C', None, 'D']
family_1 = build_tree(values)

"""
     A
    / \
   B   C
  /   / \ 
 D   E   F
          \
           G
"""

values = ['A', 'B', 'C', None, 'D', None, 'E', 'F', None, None, None, None, None, 'G']
family_2 = build_tree(values)

"""
                 A
                / \
               B   C
              /     \ 
             D       E
            /         \
           F           G
          /             \
         H               I  
"""

values = ["A", "B", "C", "D", None, None, "E", "F", None, None, "G", "H", None, None, "I"]
family_3 = build_tree(values)

print(find_lonely_cichlids(family_1))
print(find_lonely_cichlids(family_2))
print(find_lonely_cichlids(family_3))
print("Time Complexity: O(N), since we visisted each node in the tree")
print("Space Complexity: O(H), due to recursive call stack, O(N) in the worst case and the tree is skewed.")

"""
Problem 2: Searching Ariel's Treasures
The mermaid princess Ariel is looking for a specific item in the grotto where she collects all the various objects from the human world 
she finds. Ariel's collection of human treasures is stored in a binary search tree (BST) where each node represents a different item in 
her collection. The items are organized according to their names (vals) in alphabetical order in the BST.
Given the root of the binary search tree grotto and a target object treasure, write a function locate_treasure() that returns True 
if treasure is present in the garden and False otherwise.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def locate_treasure(grotto, treasure):
    if not grotto:
        return False
    if grotto.val == treasure:
        return True
    left_subtree = locate_treasure(grotto.left, treasure)
    right_subtree = locate_treasure(grotto.right, treasure)

    return left_subtree or right_subtree

# # Iterative Approach
# def locate_treasure(grotto, treasure):
#     if not grotto:
#         return False
#     current = grotto
#     while current is not None:
#         if current.val == treasure:
#             return True
#         elif treasure < current.val:
#             current = current.left
#         else:
#             current = current.right
#     return False
# print("Time Complexity: O(H), For Balanced BST search operation will take O(log N)")
# print("Space Complexity: O(1)")


print("--------Problem 2---------")
"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""


# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
grotto = build_tree(values)

print(locate_treasure(grotto, "Dinglehopper"))  
print(locate_treasure(grotto, "Thingamabob"))
print("Time Complexity: O(N), since, we are traversing each node")
print("Space Complexity: O(H), due to recursive call stack")

"""
Problem 3: Add New Treasure to Collection
The mermaid princess Ariel and her pal Flounder visited a new shipwreck and found an exciting new human artifact to add to her collection. 
Ariel's collection of human treasures is stored in a binary search tree (BST) where each node represents a different item in her collection. 
Items are organized according to their names (vals) in alphabetical order in the BST.
Given the root of the binary search tree grotto and a string new_item, write a function locate_treasure() that adds a new node with value 
new_item to the collection and returns the root of the modified tree. If a node with value new_item already exists within the tree, 
return the original tree unmodified. You do not need to maintain balance in the tree.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode():
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

def add_treasure(grotto, new_item):
    if not grotto or grotto is None:
        return TreeNode(new_item)
    if grotto.val == new_item:
        return grotto
    if new_item < grotto.val:
        grotto.left = add_treasure(grotto.left, new_item)
    else:
        grotto.right = add_treasure(grotto.right, new_item)
    return grotto


print("--------Problem 3---------")
"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""

# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", "Whozit"]
grotto = build_tree(values)

# Using print_tree() function included at top of page
print_tree(add_treasure(grotto, "Thingamabob"))
print("Time Complexity: O(H) where H is the height of the tree, O(log N) for the balanced BST, for insertion operation")
print("Space Complexity: O(H) due to recursive call stack, in the worst case it will be O(N)")

"""
Problem 4: Sorting Pearls by Size
You have a collection of pearls harvested from a local oyster bed. The pearls are organized by their size in a BST, where each node in 
the BST represents the size of a pearl.
A function smallest_to_largest_recursive() which takes in the BST root pearls and returns an array of pearl sizes sorted from smallest 
to largest has been provided for you.
Implement a new function smallest_to_largest_iterative() which provides a iterative solution, taking in the BST root pearls and returning 
an array of pearl sizes sorted from smallest to largest has been provided for you.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def smallest_to_largest_recursive(pearls):
    sorted_list = []
    
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)   
            sorted_list.append(node.val) 
            inorder_traversal(node.right)  
    
    inorder_traversal(pearls)
    return sorted_list

def smallest_to_largest_iterative(pearls):
    if not pearls:
        return []
    result = []
    stack = []
    current = pearls
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


print("--------Problem 4---------")
"""
        3
       / \
      /   \ 
     1     5
      \   / \
       2 4   8
"""

# Use build_tree() function at top of page
values = [3, 1, 5, None, 2, 4, 8]
pearls = build_tree(values)

print(smallest_to_largest_recursive(pearls))
print(smallest_to_largest_iterative(pearls))
print("Time Complexity for recursive approach is O(N)")
print("Space Complexity for recursive approach is O(H)")
print("Time Complexity for Iterative Approach is O(N)")
print("Space Complexity for Iterative Approach is O(H)")


"""
Problem 5: Smallest Pearl Above Minimum Size
You have a collection of pearls stored in a BST where each node represents a pearl with size val. You are looking for a pearl to gift 
the sea goddess, Yemaya. So as to not anger her, the pearl must be larger than min_size.
Given the root of a BST pearls, write a function pick_pearl() that returns the pearl with the smallest size above min_size. 
If no pearl with a size above min_size exists, the function should return None.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def pick_pearl(pearls, min_size):
    gift = None
    current = pearls
    while current:
        if current.val > min_size:
            gift = current
            current = current.left
        else:
            current = current.right
    return gift.val if gift else None

print("--------Problem 5---------")
"""
        3
       / \
      /   \ 
     1     5
      \   / \
       2 4   8
"""
# Use build_tree() function at top of page
values = [3, 1, 5, None, 2, 4, 8]
pearls = build_tree(values)

print(pick_pearl(pearls, 3))
print(pick_pearl(pearls, 7))
print(pick_pearl(pearls, 8))
print("Time Complexity: O(H) and O(log N) for a balanced BST")
print("Space Complexity: O(1)")

"""
Problem 6: Remove Invasive Species
As a marine ecologist, you are worried about invasive species wreaking havoc on the local ecosystem. Given the root of a BST ecosystem 
where each node represents a species in a marine ecosystem, and an invasive species name, remove the species with value name from the 
ecosystem. Return the root of the modified ecosystem. Species are organized alphabetically in the tree by name (val).
If the node with name has two children in the tree, replace it with its inorder successor (leftmost node in its right subtree). 
You do not need to maintain a balanced tree. Pseudocode has been provided for you.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_species(ecosystem, name):
    # Find the node to remove
    # If the node has no children
        # Remove the node by setting parent pointer to None
    # If the node has one child
        # Replace the node with its child
    # If the node has two children
        # Find the inorder successor
        # Replace the node's value with inorder successor value
        # Remove inorder successor
    # Return root of updated tree
    if not ecosystem:
        return None
    if name < ecosystem.val:
        ecosystem.left = remove_species(ecosystem.left,name)
    elif name > ecosystem.val:
        ecosystem.right = remove_species(ecosystem.right, name)
    else:
        if not ecosystem.left:
            return ecosystem.right
        elif not ecosystem.right:
            return ecosystem.left
        else:
            successor = min_val_node(ecosystem.left)
            ecosystem.val = successor.val
            ecosystem.left = remove_species(ecosystem.left,successor.val)
    return ecosystem

def min_val_node(node):
    if not node:
        return None
    current = node
    while current.left:
        current = current.left
    return current


print("--------Problem 6---------")
"""
                Dugong
             /         \
       Brain Coral   Lionfish
              \       /       \
         Clownfish Giant Clam  Seagrass
"""
# Use build_tree() function at top of page
values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
ecosystem = build_tree(values)

# Using print_tree() function at top of page
print_tree(remove_species(ecosystem, "Lionfish"))
print("Time Complexity: O(H)")
print("Space Complexity: O(H)")


"""
Problem 7: Minimum Difference in Pearl Size
You are analyzing your collection of pearls stored in a BST where each node represents a pearl with a specific size (val). 
You want to see if you have two pearls of similar size that you can make into a pair of earrings.
Write a function min_diff_in_pearl_sizes() that acceps the root of a BST pearls, and returns the minimum difference between the sizes of 
any two different pearls in the collection.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""

class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(pearls):
    if not pearls:
        return None


print("--------Problem 7---------")
"""
        4
       / \
      2   6
     / \   \
    1   3   8
"""
# Use build_tree() function at top of page
values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)

print(min_diff_in_pearl_sizes(pearls))  