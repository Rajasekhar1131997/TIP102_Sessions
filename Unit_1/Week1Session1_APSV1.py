# Problem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. 
# The function accepts a list items and a target value as parameters. 
# The function should return the first index of target in items, and -1 if target is not in the lst. 
# Do not use any built-in functions.
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))

# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! 
# Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.
def final_value_after_operations(operations):
    tigger = 1
    for i in operations:
        if i in ["bouncy","flouncy"]:
            tigger +=1
        if i in ["trouncy","pouncy"]:
            tigger -=1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a 
# string word and returns a new string that removes any substrings t, i, gg, and er from word. 
# The function should be case insensitive.
def tiggerfy(word):
    word = word.lower()
    word = word.replace("t","")
    word = word.replace("i","")
    word = word.replace("gg","")
    word = word.replace("er","")
    return word

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))

# Problem 4: Non-decreasing Array
# Given an array nums with n integers, write a function non_decreasing() that checks if nums 
# could become non-decreasing by modifying at most one element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2)
def non_decreasing(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            count +=1
            if count > 1:
                return False
    return True

nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))

# Problem 5: Missing Clues
# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. 
# Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. 
# The function accepts two integers lower and upper and a unique integer array clues. 
# All elements in clues are within the inclusive range [lower, upper].
# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.
# Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
# That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.
def find_missing_clues(clues, lower, upper):
    result = []
    clues = sorted(clues)
    previous = lower-1
    for num in clues+[upper+1]:
        if  num - previous >=2:
            start = previous+1
            end = num - 1
            result.append([start,end])
        previous = num
    return result


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))

# Problem 6: Vegetable Harvest
# Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. 
# Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns 
# the number of of carrots that are ready to harvest in the vegetable patch. 
# A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.
# Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.
def harvest(vegetable_patch):
    n = len(vegetable_patch)
    count = 0
    for i in range(n):
        m = len(vegetable_patch[i])
        for j in range(m):
            if vegetable_patch[i][j] == 'c':
                count +=1
    return count

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch))

# Problem 7: Eeyore's House
# Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose 
# lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 
# and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. 
# The function should return the number of good pairs.
# A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. 
# Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1.
def good_pairs(pile1, pile2, k):
    p1 = len(pile1)
    p2 = len(pile2)
    count = 0
    for i in range(p1):
        for j in range(p2):
            if (pile1[i] % (pile2[j] * k) == 0):
                count +=1
    return count

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))

# Problem 8: Local Maximums
# Write a function local_maximums() that accepts an n x n integer matrix grid and returns 
# an integer matrix local_maxes of size (n - 2) x (n - 2) such that:
# local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
def local_maximums(grid):
    n = len(grid)
    local_maxes = []
    for i in range(n-2):
        row = []
        for j in range(n-2):
            max_val = max(
                grid[i][j],grid[i][j+1],grid[i][j+2],
                grid[i+1][j], grid[i+1][j+1],grid[i+1][j+2],
                grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]
            )
            row.append(max_val)
        local_maxes.append(row)
    return local_maxes

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))