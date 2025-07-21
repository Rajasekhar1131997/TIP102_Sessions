"""
Problem 1: Finding the Perfect Cruise
It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, 
use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.
"""
def find_cruise_length(cruise_lengths, vacation_length):
    if not cruise_lengths:
        return False
    left = 0
    right = len(cruise_lengths) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif vacation_length < cruise_lengths[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

print("--------Problem 1---------")
print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
print("Time Complexity: O(Log N)")
print("Space Complexity: O(1)")

"""
Problem 2: Booking the Perfect Cruise Cabin
As part of your cruise planning, you have a list of available cabins sorted in ascending order by their deck level. 
Given the list of available cabins represented by deck level, cabins, and an integer preferred_deck, write a recursive function 
find_cabin_index() that returns the index of preferred_deck. If a cabin with your preferred_deck does not exist in cabins, 
return the index where it would be if it were added to the list to maintain the sorted order.
Your algorithm must have O(log n) time complexity.
"""
def find_cabin_index(cabins, preferred_deck):
    return find_cabin(cabins, preferred_deck, 0, len(cabins)-1)

def find_cabin(cabins,preferred_deck,left,right):
    if left > right:
        return left
    mid = left + (right-left) // 2
    if cabins[mid] == preferred_deck:
        return mid
    elif preferred_deck > cabins[mid]:
        return find_cabin(cabins,preferred_deck,mid+1, right)
    else:
        return find_cabin(cabins,preferred_deck,left,mid-1)

print("--------Problem 2---------")
print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))
print("Time Complexity: O(Log N)")
print("Space Complexity: O(Log N)")

"""
Problem 3: Count Checked In Passengers
As a cruise ship worker, you're in charge of tracking how many passengers have checked in to their rooms thus far. 
You are given a list of rooms where passengers are either checked in (represented by a 1) or not checked in (represented by a 0). 
The list is sorted, so all the 0s appear before any 1s.
Write a function count_checked_in_passengers() that efficiently counts and returns the total number of checked-in passengers (1s) 
in the list in O(log n) time.
"""
def count_checked_in_passengers_iterative(rooms):
    if not rooms:
        return 0
    count = 0
    for room in rooms:
        if room == 1:
            count += 1
    return count

print("--------Problem 3---------")
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers_iterative(rooms1)) 
print(count_checked_in_passengers_iterative(rooms2))
print(count_checked_in_passengers_iterative(rooms3))
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")

def count_checked_in_passengers_recursive(rooms):
    if not rooms:
        return 0
    n = len(rooms)
    left = 0
    right = n-1
    first_one_index = n #assuming there are no 1's initially
    while left <=right:
        mid = left + (right-left) // 2
        if rooms[mid] == 1:
            first_one_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return n - first_one_index

print("--------Problem 3 (Recursive)---------")
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers_recursive(rooms1)) 
print(count_checked_in_passengers_recursive(rooms2))
print(count_checked_in_passengers_recursive(rooms3))
print("Time Complexity: O(Log N)")
print("Space Complexity: O(1)")

"""
Problem 4: Determining Profitability of Excursions
As the activities director on a cruise ship, you’re organizing excursions for the passengers. You have a sorted list of 
non-negative integers excursion_counts, where each number represents the number of passengers who have signed up for 
various excursions at your next cruise destination. The list is considered profitable if there exists a number x such that 
there are exactly x excursions that have at least x passengers signed up.
Write a function that detrmines whether excursion_counts is profitable. If it is profitable, return the value of x. 
If it is not profitable, return -1. It can be proven that if excursion_counts is profitable, the value for x is unique.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def is_profitable(excursion_counts):
    if not excursion_counts:
        return -1
    n = len(excursion_counts)
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right-left) // 2
        x = n - mid
        if excursion_counts[mid] >= x:
            if mid == 0 or excursion_counts[mid-1] < x:
                return x

print("--------Problem 4---------")
print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
