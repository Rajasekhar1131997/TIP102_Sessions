"""
Problem 1: Finding the Perfect Cruise
It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order,
use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.
"""


"""
Understand:
    Input: Its an array of integers, target length
    Output: Boolean (True if target in arr, false otherwise)

    Edge cases: if empty arr, return False

    Time: O(log N)
    Space: O(n) due to using of recursion stack and slicing


Match: Binary search

Plan:
get length of arr,
set left = 0, right = length of arr - 1

mid = left + (right-left)//2

then check if target = arr[mid]: return true
    else: update mid and left or right pointers and check again

if left > right:
    end of arr, still not found then return False


Implement:

"""
# "def find_cruise_length(cruise_lengths, vacation_length):
#     length = len(cruise_lengths)
#     left = 0
#     right = length - 1
#     mid = left + (right-left) // 2

#     if left > right:
#         return False
        
#     if cruise_lengths[mid] == vacation_length:
#         return True
#     else:
#         if vacation_length > cruise_lengths[mid]:
#             return find_cruise_length(cruise_lengths[mid+1:], vacation_length)  
#         else:
#             return find_cruise_length(cruise_lengths[:mid], vacation_length)
      
# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

"""
Problem 2: Booking the Perfect Cruise Cabin
As part of your cruise planning, you have a list of available cabins sorted in ascending order by their deck level. 
Given the list of available cabins represented by deck level, cabins, and an integer preferred_deck, 
write a recursive function find_cabin_index() that returns the index of preferred_deck. If a cabin with your preferred_deck 
does not exist in cabins, return the index where it would be if it were added to the list to maintain the sorted order.
Your algorithm must have O(log n) time complexity.
"""
"""
Understand:
    Input: Its an array of integers, preferred deck
    Output: index if the preferred deck in the array, return the position where it would fit in the array

    Edge cases: if empty arr, return 0

    Time: O(log N)
    Space: O(log N)


Match: Binary search

Plan:
get length of arr,
set left = 0, right = length of arr - 1
mid = left + (right-left)//2

then check if preferred_deck = arr[mid]: return index
    else: update mid and left or right pointers and check again

if left > right:
    end of arr, still not found then return 
    index where it would fit, the last left or right index
"""
"""
def find_cabin(cabins,preferred_deck,left,right):
    
    if left > right:
        return left
    mid = left + (right-left) // 2
    if cabins[mid] == preferred_deck:
        return mid
    if preferred_deck < cabins[mid]:
        return find_cabin(cabins,preferred_deck,left,mid-1)
    else:
        return find_cabin(cabins, preferred_deck,mid+1,right)
    
def find_cabin_index(cabins, preferred_deck):
    return find_cabin(cabins,preferred_deck,0,len(cabins)-1)

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))
"""

"""
Problem 3: Count Checked In Passengers
As a cruise ship worker, you're in charge of tracking how many passengers have checked in to their rooms thus far. You are given a list of rooms where passengers are either checked in (represented by a 1) or not checked in (represented by a 0). The list is sorted, so all the 0s appear before any 1s.
Write a function count_checked_in_passengers() that efficiently counts and returns the total number of checked-in passengers (1s) in the list in O(log n) time.
"""
"""
Understand:
    Input: Its an array of integers
    Output: integer, we need to return the count of checked in passengers

    Edge cases: if empty arr, return 0

    Time: O(log N)
    Space: O(log N)


Match: Binary search

Plan:
get length of arr,
set left = 0, right = length of arr - 1
mid = left + (right-left)//2

if arr[mid] == 1:
    set right = mid - 1

else:
    left = mid + 1


final count of 1s can be len(arr) - left
"""


def count_checked_in_passengers(rooms):

    left = 0
    right = len(rooms) - 1

    while left < right:
        mid = left + (right-left) // 2

        if rooms[left] != rooms[right]:
            return len(rooms) - left



        if rooms[mid] == 1:
            right = mid - 1

        
        else:
            left = mid + 1
    
    return 0

    





rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))