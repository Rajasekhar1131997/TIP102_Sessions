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

