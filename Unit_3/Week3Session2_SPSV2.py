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
    

print("--------Problem 3---------")
print(terrain_elevation_match("IDID")) 
print(terrain_elevation_match("III")) 
print(terrain_elevation_match("DDI"))