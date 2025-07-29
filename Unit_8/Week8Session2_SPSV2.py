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
         
def add_treasure(grotto, new_item):
    pass


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