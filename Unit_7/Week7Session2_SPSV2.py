"""
Problem 1: Finding the Perfect Song
Abby Lee of Dance Moms is looking for the perfect song to choreograph a group routine to and needs a song of a specified length. 
Given a specific song length length and a list of song lengths playlist sorted in ascending order, use the binary search algorithm 
to return the index of the song in playlist with length. If no song with the target length exists, return -1.
"""
def find_perfect_song(playlist, length):
	if not playlist:
		return -1
	left = 0
	right = len(playlist) - 1
	while left <= right:
		mid = left + (right-left) // 2
		if playlist[mid] == length:
			return mid
		elif length > playlist[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return -1

print("--------Problem 1---------")
print(find_perfect_song([101, 102, 103, 104, 105], 103))
print(find_perfect_song([201, 202, 203, 204, 205], 206))
print("Time Complexity: O(Log N)")
print("Space Complexity: O(1)")

"""
Problem 2: Finding Tour Dates
Your favorite artist is doing a short residency in your city and you're hoping to attend one of their concerts! But because of school, 
you're only free one day this month 😭. Given a sorted list of integers tour_dates representing the days this month your favorite artist 
is playing, and an integer available representing the day you are available, write a recursive function can_attend() that returns True 
if you will be able to attend one of their concerts (some date in tour_dates matches available) and False otherwise.
Your solution must have O(log n) time complexity.
"""
def can_attend(tour_dates, available):
	if not tour_dates:
		return False
	left = 0
	right = len(tour_dates) - 1
	while left <= right:
		mid = left + (right-left) // 2
		if tour_dates[mid] == available:
			return True
		elif available > tour_dates[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return False

print("--------Problem 2---------")
print(can_attend([1, 3, 7, 10, 12], 12))
print(can_attend([1, 3, 7, 10, 12], 5))
print("Time Complexity: O(Log N)")
print("Space Complexity: O(1)")

"""
Problem 3: Sqrt(x)
Given a non-negative integer x, use binary search to return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You may not use any built-in exponent function or operator. You may not use any external libraries like math.
For example, do not use pow(x, 0.5) or x ** 0.5.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def my_sqrt(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	left = 0
	right = x // 2
	while left <= right:
		mid = left + (right-left) // 2
		if mid ** 2 == x:
			return mid
		elif x > mid ** 2:
			left = mid + 1
		else:
			right = mid - 1
	return right

print("--------Problem 3---------")
print(my_sqrt(4))
print(my_sqrt(8))
print("Time Complexity: O(Log N)")
print("Space Complexity: O(1)")

"""
Problem 4: Granting Backstage Access
You're helping manage a music tour, and you have an array of integers group_sizes where each element represents a group of friends 
attending tonight's concert together. The artist has time to meet two sets of fans backstage before the show. You want to choose 
two groups such that the combined number of people is the highest possible while still strictly below a threshold room_capacity. 
Given the list group_sizes and integer room_capacity, use binary search to return the maximum sum of two distinct groups 
in group_sizes where the sum is less than room_capacity. If no such pair exists, return -1.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def get_group_sum(group_sizes, room_capacity):
	if not group_sizes:
		return -1
	group_sizes.sort()
	max_sum = -1
	for i in range(len(group_sizes)):
		left = 0
		right = len(group_sizes) - 1
		while left <= right:
			mid = left + (right-left) // 2
			current_sum = group_sizes[i] + group_sizes[mid]
			if current_sum < room_capacity:
				max_sum = max(current_sum,max_sum)
				left = mid + 1
			else:
				right = mid - 1
				
	return max_sum
				
print("--------Problem 4---------")
print(get_group_sum([1,20,10,14,3,5,4,2], 12))
print(get_group_sum([10,20,30], 15))
print("Time Complexity: O(N LogN)")
print("Space Complexity: O(1)")

"""
Problem 5: Harmonizing Two Musical Tracks
You're working as a music producer and have two tracks track1 and track2, each represented by a sorted list of pitch values. 
Using the divide-and-conquer approach, merge the pitch values into a single, sorted sequence and return the resulting list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def merged_tracks(track1, track2):
	merged_list = []
	i, j = 0, 0
	if not track1:
		return track2
	if not track2:
		return track1
	while i < len(track1) and j < len(track2):
		if track1[i] < track2[j]:
			merged_list.append(track1[i])
			i += 1
		else:
			merged_list.append(track2[j])
			j += 1
	while i < len(track1):
		merged_list.append(track1[i])
		i += 1
	while j < len(track2):
		merged_list.append(track2[j])
		j += 1
	return merged_list
		

print("--------Problem 5---------")
track1 = [1, 3, 5]
track2 = [2, 4, 6]
track3 = [10, 20]
track4 = [15, 30]

print(merged_tracks(track1, track2))
print(merged_tracks(track3, track4))
print("Time Complexity: O(M+N)")
print("Space Complexity: O(M+N)")

"""
Problem 6: Merge Sort Playlist
Given a list of strings playlist, use merge sort to write a recursive merge_sort_playlist() function that accepts that returns 
the list of songs sorted in alphabetical order.
Pseudocode has been provided for you
"""
def merge_sort_helper(left_arr, right_arr):
    # Create an empty list to store merged result list
    # Use pointers to iterate through left_arr and right_arr
        # Compare their elements, and add the smaller element to result list
        # Increment pointer of list with smaller element
    # Add any remaining elements from the left half
    # Add any remaining elements from the right half
    # Return the merged list
	merged_list = []
	i, j = 0, 0
	while i < len(left_arr) and j < len(right_arr):
		if left_arr[i] < right_arr[j]:
			merged_list.append(left_arr[i])
			i += 1
		else:
			merged_list.append(right_arr[j])
			j += 1
	while i < len(left_arr):
		merged_list.append(left_arr[i])
		i += 1
	while j < len(right_arr):
		merged_list.append(right_arr[j])
		j += 1
	return merged_list

def merge_sort_playlist(playlist):
    # Base Case: 
    # If the list has 1 or 0 elements, it's already sorted

    # Recursive Cases:
    # Divide the list into two halves
    # Merge sort first half
    # Merge sort second half
    # Use the recursive helper to merge the sorted halves (pass in sorted left half, and sorted right half)
    # Return the merged list
	if not playlist:
		return []
	if len(playlist) <= 1:
		return playlist
	mid = len(playlist) // 2
	left_half = merge_sort_playlist(playlist[:mid])
	right_half = merge_sort_playlist(playlist[mid:])
	return merge_sort_helper(left_half, right_half)
		


print("--------Problem 6---------")
print(merge_sort_playlist(["Formation", "Crazy in Love", "Halo"]))
print(merge_sort_playlist(["Single Ladies", "Love on Top", "Irreplaceable"]))
print("Time Complexity: O(N LogN)")
print("Space Complexity: O(n)")