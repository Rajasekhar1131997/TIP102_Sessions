"""
Problem 1: Transpose Matrix
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.
"""
def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = []
    for i in range(n):
        row = [0] * m
        new_matrix.append(row)
    for i in range(m):
        for j in range(n):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))

"""
Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. 
The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
Instead, use the two-pointer approach, which is a common technique in which we initialize 
two variables (also called a pointer in this context) to track different indices or places in a list or string, 
then moves the pointers to point at new indices based on certain conditions. 
In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a 
list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through 
the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
"""
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        word = lst[left]
        lst[left] = lst[right]
        lst[right] = word
        left += 1
        right -= 1
    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

"""
Problem 3: Remove Duplicates
Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place 
such that each element appears only once. Return the length of the modified array. You may not create another array; 
your implementation must modify the original input array items.
"""
def remove_dupes(items):
    left = 0
    right = 1
    for right in range(len(items)):
        if items[right] != items[left]:
            left += 1
            items[left] = items[right]
    return (left+1)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))

"""
Problem 4: Sort Array by Parity
Given an integer array nums, write a function sort_by_parity() that moves all the even integers 
at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
"""
def sort_by_parity(nums):
    left = 0
    right = len(nums) -1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 !=0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
    return nums

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))

"""
Problem 5: Container with Most Honey
Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts 
an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most honey.
Return the maximum amount of honey a container can store.
Notice that you may not slant the container.
"""
def most_honey(height):
    result = 0
    left, right = 0, len(height) - 1
    while left < right:
        area = (right-left) * min(height[left],height[right])
        result = max(result,area)

        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left +=1
    return result


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))

"""
Problem 6: Merge Intervals
Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
def merge_intervals(intervals):
    intervals.sort(key = lambda x:x[0])
    merged = []
    for a, b in intervals:
        if not merged or a > merged[-1][1]:
            merged.append([a,b])
        else:
            merged[-1][1] = max(merged[-1][1],b)
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))