"""
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string 
is a suit in Stark's collection, count the total number of suits in the list.
Implement the solution iteratively without the use of the len() function.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
"""
def count_suits_iterative(suits):
    if not suits:
        return 0
    length = 0
    for suit in suits:
        length += 1
    return length

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])

print("--------Problem 1---------")
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
print("Time Complexity for Iterative Approach: O(n)")
print("Space Complexity for Iterative Approach: O(1)")
print("Time Complexity for Recursive Approach: O(n)")
print("Space Complexity for Recursive Approach: O(n)")

"""
Problem 2: Collecting Infinity Stones
Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, 
return the total power using a recursive approach.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

print("--------Problem 2---------")
print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, 
count the total number of unique suits in the list.
Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def count_suits_iterative(suits):
    if not suits:
        return 0
    seen = set()
    for suit in suits:
        if suit not in seen:
            seen.add(suit)
    return len(seen)

def count_suits_recursive(suits):
    if not suits:
        return 0
    first = suits[0]
    rest = count_suits_recursive(suits[1:])
    if first in suits[1:]:
        return rest
    else:
        return 1 + rest

print("--------Problem 3---------")
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark II", "Mark II", "Mark III"]))
print("Time Complexity for Iterative Approach: O(n)")
print("Space Complexity for Iterative Approach: O(n)")
print("Time Complexity for Recursive Approach: O(n^2)")
print("Space Complexity for Recursive Approach: O(n)")

"""
Problem 4: Calculating Groot's Growth
Groot grows according to a pattern similar to the Fibonacci sequence. Given n, find the height of Groot after n months using a 
recursive method.
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number 
is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for why 
you believe your solution has the stated time complexity.
"""
def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci_growth(n-1) + fibonacci_growth(n-2)

print("--------Problem 4---------")
print(fibonacci_growth(5))
print(fibonacci_growth(8))
print("Time Complexity: O(n^2)")
print("Space Complexity: O(n)")

"""
Problem 5: Calculating the Power of the Fantastic Four
The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. 
Write a recursive function that calculates the power of 4 raised to the nth power to determine their training level.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def power_of_four(n):
    if n == 0:
        return 1
    if n > 0:
        return 4 * power_of_four(n-1)
    else:
        return 1 / (4 * power_of_four(-n-1))
    
print("--------Problem 5---------")
print(power_of_four(3))
print(power_of_four(-2))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 6: Strongest Avenger
The Avengers need to determine who is the strongest. Given a list of their strengths, find the maximum strength using a 
recursive approach without using the max() function.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def strongest_avenger(strengths):
    if not strengths:
        return 0
    if len(strengths) == 1:
        return strengths[0]
    max_strength = strengths[0]
    rest = strongest_avenger(strengths[1:])
    if max_strength > rest:
        return max_strength
    else:
        return rest

print("--------Problem 6---------")
print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 7: Counting Vibranium Deposits
In Wakanda, vibranium is the most precious resource, and it is found in several deposits. Each deposit is represented by a 
character in a string (e.g., "V" for vibranium, "G" for gold, etc.)
Given a string resources, write a recursive function count_deposits() that returns the total number of distinct vibranium 
deposits in resources.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def count_deposits(resources):
    if not resources:
        return 0
    if resources[0] == 'V':
        return 1 + count_deposits(resources[1:])
    else:
        return count_deposits(resources[1:])

print("--------Problem 7---------")
print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 8: Merging Missions
The Avengers are planning multiple missions, and each mission has a priority level represented as a node in a linked list. 
You are given the heads of two sorted linked lists, mission1 and mission2, where each node represents a mission with its priority level.
Implement a recursive function merge_missions() which merges these two mission lists into one sorted list, ensuring that the 
combined list maintains the correct order of priorities. The merged list should be made by splicing together the nodes from 
the first two lists.
Return the head of the merged mission linked list.
"""
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    if not mission1:
        return mission2
    if not mission2:
        return mission1
    if mission1.value < mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2

print("--------Problem 8---------")
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))
print("Time Complexity: O(m+n)")
print("Space Complexity: O(m+n)")

"""
Problem 9: Merging Missions II
Below is an iterative solution to the merge_missions() function from the previous problem. Compare your recursive solution to the 
iterative solution below.
Discuss with your podmates. Which solution do you prefer?
"""
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions_iterative(mission1, mission2):
    temp = Node()  # Temporary node to simplify the merging process
    tail = temp

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return temp.next  # Return the head of the merged linked list