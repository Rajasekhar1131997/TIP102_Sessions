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