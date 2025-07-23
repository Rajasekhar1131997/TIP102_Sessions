"""
Problem 1: Building an Underwater Kingdom
Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.
The root, or topmost node in the tree TreeNode("Poseidon") has been provided for you.
           Poseidon
          /         \
      Atlantis      Oceania
      /     \       /     \
  Coral     Pearl  Kelp    Reef
"""
from collections import deque
class TreeNode:
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

print("--------Problem 1---------")
root = TreeNode("Poseidon")
# Add your code here
root.left = TreeNode("Atlantis")
root.right = TreeNode("Oceania")
root.left.left = TreeNode("Coral")
root.left.right = TreeNode("Pearl")
root.right.left = TreeNode("Kelp")
root.right.right = TreeNode("Reef")

# Using print_tree() included at the top of this page
print_tree(root)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")

"""
Problem 2: Are Twins?
Given the root of a binary tree that has at most three nodes: the root, its left child, and its right child.
Return True if the root's children are twins (have equal value) and False otherwise. If the root has no children, return False.
Evaluate the time complexity of your function. Define your variables and provide a rationale for why 
you believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def mertwins(root):
    if not root:
        return False
    if not root.left or not root.right:
        return False
    return root.left.val == root.right.val

print("--------Problem 2---------")
"""
      Mermother
       /    \
    Coral   Coral
"""
root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))

"""
      Merpapa
       /    \
   Calypso  Coral
"""
root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))

"""
      Merenby
           \    
         Calypso  
"""
root3 = TreeNode("Merenby", None, TreeNode("Calypso"))

print(mertwins(root1))
print(mertwins(root2))
print(mertwins(root3))
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")

"""
Problem 3: Poseidon's Decision
Poseidon has received advice on an important matter from his council of advisors. Help him evaluate the advice from his council 
to make a final decision. You are given the advice as the root of a binary tree representing a boolean expression that has at most three nodes. 
The root may have exactly 0 or 2 children. Leaf nodes have a boolean value of either True or False.
Non-leaf nodes have a string value of either AND or OR. The evaluation of a node is as follows:
If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.
Evaluate the time complexity of your function. Define your variables and provide a rationale for \
why you believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(root):
    if not root:
        return False
    if root.left is None and root.right is None:
        return root.val
    if root.val == 'OR':
        return root.left.val or root.right.val
    if root.val == 'AND':
        return root.left.val and root.right.val

print("--------Problem 3---------")
"""
        OR
      /    \
    True  False
"""
expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

"""
       False
"""
expression2 = TreeNode(False)

print(get_decision(expression1))
print(get_decision(expression2))
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")

"""
Problem 4: Escaping the Sea Caves
You are given the root of a binary tree representing possible route through a system of sea caves. You recall that so long as you 
take the leftmost branch at every fork in the route, you'll find your way back home. Write a function leftmost_path() that returns 
an array with the value of each node in the leftmost path.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    if not root:
        return []
    result = []
    current = root
    while current:
        result.append(current.val)
        if current.left:
            current = current.left
        else:
            break
    return result

print("--------Problem 4---------")
"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))
print("Time Complexity: O(H)")
print("Space Complexity: O(H)")

"""
Problem 5: Escaping the Sea Caves II
If you implemented leftmost_path() iteratively in the previous problem, implement it recursively. If you implemented it recursively, 
implement it iteratively.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    if not root:
        return []
    return [root.val] + leftmost_path(root.left)


print("--------Problem 5---------")
"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))
print("Time Complexity: O(H)")
print("Space Complexity: O(H)")

"""
Problem 6: Documenting Reefs
You are exploring a vast coral reef system. The reef is represented as a binary tree, where each node corresponds to a specific coral 
formation. You want to document the reef as you encounter it, starting from the root or main entrance of the reef.
Write a function explore_reef() that performs a preorder traversal of the reef and returns a list of the names of the coral formations in the
 order you visited them. In a preorder exploration, you explore the current node first, then the left subtree, and finally the right subtree.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def explore_reef(root):
    if not root:
        return []
    left_subtree = explore_reef(root.left)
    right_subtree = explore_reef(root.right)
    return [root.val] + left_subtree + right_subtree

print("--------Problem 6---------")
"""
         CoralA
        /     \
     CoralB  CoralC
     /   \      
 CoralD CoralE  
"""

reef = TreeNode("CoralA", 
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                          TreeNode("CoralC"))

print(explore_reef(reef))
print("Time Complexity: O(N)")
print("Space Complexity: O(H)")

"""
Problem 7: Coral Count
Due to climate change, you have noticed that coral has been dying in the reef near Atlantis. You want to ensure there is still a 
healthy level of coral in the reef. Given the root of a binary tree where each node represents a coral in the reef, write a function 
count_coral() that returns the number of corals in the reef.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_coral(root):
    if not root or root is None:
        return 0
    left_subtree = count_coral(root.left)
    right_subtree = count_coral(root.right)
    return 1 + left_subtree + right_subtree


print("--------Problem 7---------")
"""
          Staghorn
         /        \
        /          \
    Sea Fan      Sea Whip
    /     \       /   
 Bubble  Table  Star
  /
Fire
"""
reef1 = TreeNode("Staghorn", 
                TreeNode("Sea Fan", TreeNode("Bubble", TreeNode("Fire")), TreeNode("Table")),
                        TreeNode("Sea Whip", TreeNode("Star")))

"""
     Fire
    /    \
   /      \ 
Black    Star
        /  
     Lettuce 
           \
        Sea Whip
"""
reef2 = TreeNode("Fire", 
                TreeNode("Black"), 
                        TreeNode("Star", 
                                  TreeNode("Lettuce", None, TreeNode("Sea Whip"))))

print(count_coral(reef1))
print(count_coral(reef2))
print("Time Complexity: O(N)")
print("Space Complexity: O(H)")

"""
Problem 8: Ocean Layers
Given the root of a binary tree that represents different sections of the ocean, write a function count_ocean_layers() that returns the depth 
of the ocean. The depth or height of the tree can be defined as the number of nodes on the longest path from the root node to a leaf node.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def ocean_depth(root):
    if root is None or not root:
        return 0
    left_subtree = ocean_depth(root.left)
    right_subtree = ocean_depth(root.right)
    return 1+left_subtree if left_subtree > right_subtree else 1+right_subtree

print("--------Problem 8---------")
"""
                Sunlight
               /        \
              /          \
          Twilight      Squid
         /       \           \   
      Abyss  Anglerfish    Giant Squid
      /
  Trenches
"""
ocean = TreeNode("Sunlight", 
                TreeNode("Twilight", 
                        TreeNode("Abyss", 
                                TreeNode("Trenches")), TreeNode("Anglerfish")),
                                        TreeNode("Squid", TreeNode("Giant Squid")))

"""
    Spray Zone
    /         \
   /           \ 
Beach       High Tide
            /  
      Middle Tide
              \
            Low Tide
"""
tidal_zones = TreeNode("Spray Zone", 
                      TreeNode("Beach"), 
                              TreeNode("High Tide", 
                                      TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))
print("Time Complexity: O(N)")
print("Space Complexity: O(H)")