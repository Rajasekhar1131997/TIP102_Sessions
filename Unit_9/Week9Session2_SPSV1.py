"""
Problem 1: Balanced Baked Goods Display
Given the root of a binary tree display representing the baked goods on display at your store, return True if the tree is balanced 
and False otherwise. A balanced display is a binary tree in which the difference in the height of the two subtrees of every node never 
exceeds one. Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your 
solution has the stated time complexity.
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

def is_balanced(display):
    def check_balance(node):
        if not node:
            return True, 0

        left_subtree, left_height = check_balance(node.left)
        right_subtree, right_height = check_balance(node.right)

        is_balanced = left_subtree and right_subtree and (abs(left_height-right_height)<=1)
        height = max(left_height, right_height) + 1

        return is_balanced, height
    is_balanced, length = check_balance(display)
    return is_balanced

print("--------Problem 1---------")
"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)

print(is_balanced(display1)) 
print(is_balanced(display2))
print("Time Complexity: O(N)")
print("Space Complexity: O(N) in the worst case")

"""
Problem 2: Sum of Cookies Sold Each Day
Your bakery stores each customer order in a binary tree, where each node represents a different customer's order and each node value 
represents the number of cookies ordered. Each level of the tree represents the orders for a given day.
Given the root of a binary tree orders, return a list of the sums of all cookies ordered in each day (level) of the tree.
Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you 
believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_each_days_orders(orders):
    if not orders:
        return []
    result = []
    queue = deque([orders])
    while queue:
        sum = 0
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(sum) 
    return result

print("--------Problem 2---------")
"""
      4
     / \
    2   6
   / \  
  1   3
"""

# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

print(sum_each_days_orders(orders))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 3: Sweetness Difference
You are given the root of a binary tree chocolates where each node represents a chocolate in a box of chocolates and each node value represents 
the sweetness level of the chocolate. Write a function that returns a list of the absolute differences between the highest and lowest sweetness 
levels in each row of the chocolate box. The sweetness difference in a row with only one chocolate is 0.
Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
    if not chocolates:
        return []
    result = []
    queue = deque([chocolates])
    while queue:
        min_val = float('inf')
        max_val = float('-inf')
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            diff = abs(max_val - min_val)
        
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(diff)
    return result

print("--------Problem 3---------")
"""
  3
 / \
9  20
   / \
  15  7
"""
# Using build_tree() function included at top of page
sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)

"""
    1
   / \
  2   3
 / \   \
4   5   6

"""
sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)

print(sweet_difference(chocolate_box1))  
print(sweet_difference(chocolate_box2))
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

"""
Problem 4: Transformable Bakery Orders
In your bakery, customer orders are each represented by a binary tree. The value of each node in the tree represents a type of cupcake, 
and the tree structure represents how the order is organized in the delivery box. Sometimes, orders don't get picked up.
Given two orders, you want to see if you can rearrange the first order that didn't get picked up into the second order so as not to waste 
any cupcakes. You can swap the left and right subtrees of any cupcake (node) in the order.
Given the roots of two binary trees order1 and order2, write a function can_rearrange_orders() that returns True if the tree represented 
by order1 can be rearranged to match the tree represented by order2 by doing any number of swaps of order1’s left and right branches.
Evaluate the time complexity of your function. Define your variables and provide a rationale for why 
you believe your solution has the stated time complexity.
"""
class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def can_rearrange_orders(order1, order2):
    if not order1 and not order2:
        return True
    if not order1 or not order2:
        return False
    if order1.val != order2.val:
        return False
    
    return (
        (can_rearrange_orders(order1.left, order2.left) and can_rearrange_orders(order1.right, order2.right)) or
        (can_rearrange_orders(order1.left, order2.right) and can_rearrange_orders(order1.right, order2.left)))

print("--------Problem 4---------")
"""
              Red Velvet                             Red Velvet
             /          \                           /           \
        Vanilla         Lemon                   Lemon            Vanilla
        /      \        /   \                  /     \           /      \
      Ube    Almond  Chai   Carrot       Carrot      Chai    Almond    Ube 
                     /   \        \       /          /   \      
                 Chai   Maple   Smore   Smore    Maple   Chai
"""

# Using build_tree() function included at top of page
flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot", 
            None, None, None, None, "Chai", "Maple", None, "Smore"]
flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)

print(can_rearrange_orders(order1, order2))
print("Time Complexity: O(M * N), where M and N are the nodes of the trees")
print("Space Complexity: O(H1+H2) where H is the height of the trees")

"""
Problem 5: Larger Order Tree
You have the root of a binary search tree orders, where each node in the tree represents an order and each node's value represents the 
number of cupcakes the customer ordered. Convert the tree to a 'larger order tree' such that the value of each node in tree is equal to 
its original value plus the sum of all node values greater than it. As a reminder a BST satisfies the following constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
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

def larger_order_tree(orders):
    def reverse_inorder(node, respective_sum):
        if not node:
            return respective_sum
        
        respective_sum = reverse_inorder(node.right, respective_sum)
        node.val += respective_sum
        respective_sum = node.val

        return reverse_inorder(node.left, respective_sum)
    reverse_inorder(orders, 0)
    return orders

print("--------Problem 5---------")
"""
         4
       /   \
      /     \
     1       6
    / \     / \
   0   2   5   7
        \       \
         3       8   
"""
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))
print("Time Complexity: O(N)")
print("Space Complexity: O(H)")

"""
Problem 6: Find Next Order to Fulfill Today
You store each customer order at your bakery in a binary tree where each node represents a different order. Each level of the tree 
represents a different day's orders. Given the root of a binary tree order_tree and an Treenode object order representing the order 
you are currently fulfilling, return the next order to fulfill that day. The next order to fulfill is the nearest node on the same level. 
Return None if order is the last order of the day (rightmost node of the level).
Note: Because we must pass in a reference to a node in the tree, you cannot use the build_tree() function for testing. 
You must manually create the tree.
"""
class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def find_next_order(order_tree, order):
    if not order_tree:
        return None
    queue = deque([order_tree])
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            if node == order:
                if i == level_length - 1:
                    return None
                else:
                    return queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return None

print("--------Problem 6---------")
"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)
print(next_order1.val)
print(next_order2)
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")