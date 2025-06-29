"""
Problem 1: Final Costs After a Supply Discount
You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, 
where costs[i] is the cost of the ith supply item.
There is a special discount available during the expedition. If you purchase the ith item, you will receive a discount equivalent to costs[j], 
where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.
Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, considering the special discount.
"""
def final_supply_costs(costs):
    n = len(costs)
    final_costs = [0] * n
    if not costs:
        return []
    if len(costs) == 1:
        return costs
    for i in range(n):
        discount = 0
        for j in range(i+1, n):
            if costs[j] <= costs[i]:
                discount = costs[j]
                break
        final_costs[i] = costs[i] - discount
    return final_costs


print("--------Problem 1 (Brute force Approach)---------")
print(final_supply_costs([8, 4, 6, 2, 3]))
print(final_supply_costs([1, 2, 3, 4, 5]))
print(final_supply_costs([10, 1, 1, 6]))
print(final_supply_costs([1]))

#solving the problem using stacks (Yet to solve)
def final_supply_costs(costs):
    n = len(costs)
    final_costs = list(costs)
    if not costs:
        return []
    if len(costs) == 1:
        return costs


print("--------Problem 1---------")
print(final_supply_costs([8, 4, 6, 2, 3]))
print(final_supply_costs([1, 2, 3, 4, 5]))
print(final_supply_costs([10, 1, 1, 6]))
print(final_supply_costs([1]))

"""
Problem 2: Find First Symmetrical Landmark Name
During your global expedition, you encounter a series of landmarks, each represented by a string in the array landmarks. 
Your task is to find and return the first symmetrical landmark name. If there is no such name, return an empty string "".
A landmark name is considered symmetrical if it reads the same forward and backward.
"""
def first_symmetrical_landmark(landmarks):
    for word in landmarks:
        if word[::-1] == word:
            return word
    return ""

print("--------Problem 2 (Brute force Approach)---------")
print(first_symmetrical_landmark(["canyon","forest","rotor","saas","mountain"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff"])) 

def first_symmetrical_landmark(landmarks):
    for word in landmarks:
        if symmetrical(word):
            return word
    return ""

def symmetrical(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
print("--------Problem 2 (Two pointer and helper function approach)---------")
print(first_symmetrical_landmark(["canyon","forest","rotor","saas","mountain"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff"]))

"""
Problem 3: Terrain Elevation Match
During your global expedition, you are mapping out the terrain elevations, where the elevation of each point is represented by an integer. 
You are given a string terrain of length n, where:
terrain[i] == 'I' indicates that the elevation at the ith point is lower than the elevation at the i+1th point (elevation[i] < elevation[i + 1]).
terrain[i] == 'D' indicates that the elevation at the ith point is higher than the elevation at the i+1th point (elevation[i] > elevation[i + 1]).
Your task is to reconstruct the elevation sequence and return it as a list of integers. If there are multiple valid sequences, return any of them.
Hint: Try using two variables: one to track the smallest available number and one for the largest. 
As you process each character in the string, assign the smallest number when the next elevation should increase ('I'), and assign the largest number when the next elevation should decrease ('D').
"""
def terrain_elevation_match(terrain):
    return 0
    

print("--------Problem 3---------")
print(terrain_elevation_match("IDID")) 
print(terrain_elevation_match("III")) 
print(terrain_elevation_match("DDI"))


"""
Problem 4: Find the Expedition Log Concatenation Value
You are recording journal entries during a global expedition, where each entry is represented by a 0-indexed integer array, logs. 
The concatenation of two journal entries means combining their numerals into one.
For example, concatenating the numbers 15 and 49 results in 1549.
Your task is to calculate the total concatenation value of all the journal entries, which starts at 0. 
To do this, perform the following steps until no entries remain:
1. If there are at least two entries in the logs, concatenate the first and last entries, add the result to the current concatenation value, 
and then remove these two entries.
2. If there is only one entry left, add its value to the concatenation value and remove it from the array.
3. Return the final concatenation value after all entries have been processed.
"""
# implementing the solution using Queue
from collections import deque
def find_the_log_conc_val(logs):
    total = 0
    n = len(logs)
    if n == 0:
        return total
    if n == 1:
        return logs[0]
    q = deque(logs)
    while len(q)>=2:
        left = q.popleft()
        right = q.pop()
        concatenated = int(str(left) + str(right))
        total += concatenated
        if len(q) == 1:
            total += q.pop()
    return total


print("--------Problem 4 (Queue)---------")
print(find_the_log_conc_val([7, 52, 2, 4])) 
print(find_the_log_conc_val([5, 14, 13, 8, 12])) 
print(find_the_log_conc_val([1]))

# implementing the solution using Two Pointer Approach
def find_the_log_conc_val(logs):
    total = 0
    left = 0
    right = len(logs) - 1
    while left < right:
        total += int(str(logs[left]) + str(logs[right]))
        left += 1
        right -= 1
    if left == right:
        total += logs[left]
    return total


print("--------Problem 4 (Two Pointer Approach)---------")
print(find_the_log_conc_val([7, 52, 2, 4])) 
print(find_the_log_conc_val([5, 14, 13, 8, 12])) 
print(find_the_log_conc_val([1]))

"""
Problem 5: Number of Explorers Unable to Gather Supplies
During a global expedition, explorers must gather supplies from a limited stockpile, which includes two types of resources: 
type 0 (e.g., food rations) and type 1 (e.g., medical kits). The explorers are lined up in a queue, 
each with a specific preference for one of the two types of resources.
The number of supplies in the stockpile is equal to the number of explorers. The supplies are stacked in a pile. At each step:
If the explorer at the front of the queue prefers the resource on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave the resource and go to the end of the queue.
This process continues until no explorer in the queue wants to take the top resource, leaving some explorers 
unable to gather the supplies they need.
You are given two integer arrays explorers and supplies, where supplies[i] is the type of the ith resource 
in the stack (i = 0 is the top of the stack) and explorers[j] is the preference of the jth explorer in the initial queue 
(j = 0 is the front of the queue). Return the number of explorers that are unable to gather their preferred supplies.
"""
def count_explorers(explorers, supplies):
    need_0 = explorers.count(0)
    need_1 = explorers.count(1)
    for s in supplies:
        if s == 0 and need_0 > 0:
            need_0 -= 1
        elif s ==1 and need_1 > 0:
            need_1 -= 1
        else:
            break
    return need_0 + need_1


print("--------Problem 5---------")
print(count_explorers([1, 1, 0, 0], [0, 1, 0, 1]))  
print(count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))

"""
Problem 6: Count Balanced Terrain Subsections
During your global expedition, you are analyzing a binary terrain string, terrain, where 0 represents a valley and 1 represents a hill. 
You need to count the number of non-empty balanced subsections in the terrain. A balanced subsection is defined as a 
contiguous segment of the terrain where an equal number of valleys (0s) and hills (1s) appear, and all the 0s and 1s are grouped consecutively.
Your task is to return the total number of these balanced subsections. Note that subsections that occur multiple times 
should be counted each time they appear.
"""
def count_balanced_terrain_subsections(terrain):
    return 0


print("--------Problem 6---------")
print(count_balanced_terrain_subsections("00110011")) 
print(count_balanced_terrain_subsections("10101"))


"""
Problem 7: Check if a Signal Occurs as a Prefix in Any Transmission
During your global expedition, you are monitoring various transmissions, each consisting of some signals separated by a single space. 
You are given a searchSignal and need to check if it occurs as a prefix to any signal in a transmission.
Return the index of the signal in the transmission (1-indexed) where searchSignal is a prefix of this signal. 
If searchSignal is a prefix of more than one signal, return the index of the first signal (minimum index). 
If there is no such signal, return -1.
A prefix of a string s is any leading contiguous substring of s.
"""
def is_prefix_of_signal(transmission, searchSignal):
    new_transmission = transmission.split(" ")
    for i, signal in enumerate(new_transmission):
        if signal.startswith(searchSignal):
            return i
    return -1

print("--------Problem 7---------")
print(is_prefix_of_signal("i love eating burger", "burg")) 
print(is_prefix_of_signal("this problem is an easy problem", "pro")) 
print(is_prefix_of_signal("i am tired", "you"))