"""
Problem 1: Matrix Addition
Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2. 
The function should return an n x m matrix sum_matrix that is the sum of the given matrices such 
that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.
"""
def add_matrices(matrix1, matrix2):
    m = len(matrix1)
    n = len(matrix1[0])
    p = len(matrix2)
    q = len(matrix2[0])
    sum_matrix = []
    if (m == p and n == q):
        for i in range(m):
            row = [0] * n
            for j in range(n):
                row[j] = matrix1[i][j] + matrix2[i][j]
            sum_matrix.append(row)
    return sum_matrix

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))

"""
Problem 2: Two-Pointer Palindrome
Write a function is_palindrome() that takes in a string s as a parameter and returns True 
if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.
The function must use the two-pointer approach, which is a common technique in which we 
initialize two variables (also called a pointer in this context) to track different indices or places in a 
list or string, then moves the pointers to point at new indices based on certain conditions. 
In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning 
of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards 
through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
"""
def is_palindrome(s):
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

s = "madam"
print(is_palindrome(s))

s = "madamweb"
print(is_palindrome(s))

"""
Problem 3: Squash Spaces
Write a function squash_spaces() that takes in a string s as a parameter and returns a new string 
with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, 
but in the result should be trimmed. Do not use any of the built-in trim methods.
"""
def squash_spaces(s):
    new_string = ""
    in_space = True
    for i in range(len(s)):
        if s[i] != " ":
            new_string+=s[i]
            in_space = False
        else:
            if in_space == False:
                new_string += " "
                in_space = True
    return new_string.strip()

s = "   Up,     up,   and  away! "
print(squash_spaces(s))

s = "With great power comes great responsibility."
print(squash_spaces(s))

"""
Problem 4: Two-Pointer Two Sum
Use the two pointer approach to implement a function two_sum() that takes in a sorted list of integers nums 
and an integer target as parameters and returns the indices of the two numbers that add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice. 
You can return the indices in any order.
"""
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))

"""
Problem 5: Three Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n -1
        while left < right:
            sum = nums[i] + nums[left] + nums [right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result
    
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))

"""
Problem 6: Insert Interval
Implement a function insert_interval() that accepts an array of non-overlapping intervals 
intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and 
intervals is sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] 
that represents the start and end of another interval.
Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals 
still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
You don't need to modify intervals in-place. You can make a new array and return it.
"""
def insert_interval(intervals, new_interval):
    result = []
    for i in range(len(intervals)):
        if new_interval[1] < intervals[i][0]:
            result.append(new_interval)
            return result + intervals[i:]
        elif new_interval[0] > intervals[i][1]:
            result.append(intervals[i])
        else:
            new_interval =[min(new_interval[0],intervals[i][0]), max(new_interval[1],intervals[i][1])]
    result.append(new_interval)
    return result

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
print(insert_interval(intervals, new_interval))