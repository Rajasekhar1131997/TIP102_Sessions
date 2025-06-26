"""
Problem 1: Time Needed to Stream Movies
There are n users in a queue waiting to stream their favorite movies, where the 0th user is at the front of the queue 
and the (n - 1)th user is at the back of the queue.
You are given a 0-indexed integer array movies of length n where the number of movies that the ith user would like to stream is movies[i].
Each user takes exactly 1 second to stream a movie. A user can only stream 1 movie at a time 
and has to go back to the end of the queue (which happens instantaneously) in order to stream more movies. 
If a user does not have any movies left to stream, they will leave the queue.
Return the time taken for the user at position k (0-indexed) to finish streaming all their movies.
"""
from collections import deque
def time_required_to_stream(movies, k):
    q = deque()
    for i in range(len(movies)):
        q.append((i, movies[i]))
    time = 0
    while q:
        user_id, remaining = q.popleft()
        remaining -= 1
        time += 1
        if user_id == k and remaining == 0:
            return time
        if remaining > 0:
            q.append((user_id, remaining))

print("--------Problem 1---------")
print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0))

"""
Problem 2: Reverse Watchlist
You are given a list watchlist representing a list of shows sorted by popularity for a particular user. 
The user wants to discover new shows they haven't heard of before by reversing the list to show the least popular shows first.
Using the two-pointer approach, implement a function reverse_watchlist() that reverses the order of the watchlist in-place. 
This means that the first show in the given list should become the last, the second show should become the second to last, and so on. 
Return the reversed list.
Do not use list slicing (e.g., watchlist[::-1]) to achieve this.
"""

def reverse_watchlist(watchlist):
    if not watchlist:
        return []
    if len(watchlist) == 0 or len(watchlist) == 1:
        return watchlist
    left = 0
    right = len(watchlist) - 1
    while left < right:
        watchlist[left], watchlist[right] = watchlist[right], watchlist[left]
        left += 1
        right -= 1
    return watchlist

print("--------Problem 2---------")
watchlist1 = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]
watchlist2 = []
watchlist3 = ["A"]
watchlist4 = ["A","B"]
print(reverse_watchlist(watchlist1))
print(reverse_watchlist(watchlist2))
print(reverse_watchlist(watchlist3))
print(reverse_watchlist(watchlist4))

"""
Problem 3: Remove All Adjacent Duplicate Shows
You are given a string schedule representing the lineup of shows on a streaming platform, 
where each character in the string represents a different show. 
A duplicate removal consists of choosing two adjacent and equal shows and removing them from the schedule.
We repeatedly make duplicate removals on schedule until no further removals can be made.
Return the final schedule after all such duplicate removals have been made. The answer is guaranteed to be unique.
"""
def remove_duplicate_shows(schedule):
    stack = []
    if not schedule:
        return ""
    if len(schedule) == 1:
        return schedule
    for char in schedule:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

print("--------Problem 3---------")
print(remove_duplicate_shows("abbaca")) 
print(remove_duplicate_shows("azxxzy"))

"""
Problem 4: Minimum Average of Smallest and Largest View Counts
You manage a collection of view counts for different shows on a streaming platform. 
You are given an array view_counts of n integers, where n is even.
You repeat the following procedure n / 2 times:
Remove the show with the smallest view count, min_view_count, and the show with the largest view count, max_view_count, from view_counts.
Add (min_view_count + max_view_count) / 2 to the list of average view counts average_views.
Return the minimum element in average_views.
"""
def minimum_average_view_count(view_counts):
    n = len(view_counts)
    if n == 0:
        return 0
    view_counts.sort()
    q = deque(view_counts)
    averages = []
    for i in range(n//2):
        min_avg = q.popleft()
        max_avg = q.pop()
        avg = (min_avg+max_avg) / 2
        averages.append(avg)
    return min(averages)

print("--------Problem 4---------")
print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1])) 
print(minimum_average_view_count([1, 9, 8, 3, 10, 5])) 
print(minimum_average_view_count([1, 2, 3, 7, 8, 9]))

"""
Problem 5: Minimum Remaining Watchlist After Removing Movies
You have a watchlist consisting only of uppercase English letters representing movies. Each movie is represented by a unique letter.
You can apply some operations to this watchlist where, in one operation, you can remove any 
occurrence of one of the movie pairs "AB" or "CD" from the watchlist.
Return the minimum possible length of the modified watchlist that you can obtain.
Note that the watchlist concatenates after removing the movie pair and could produce new "AB" or "CD" pairs.
"""
def min_remaining_watchlist(watchlist):
    stack = []
    if not watchlist:
        return 0
    if len(watchlist) == 1:
        return 1
    for char in watchlist:
        if stack and ((stack[-1] == "A" and char == "B") or (stack[-1] == "C" and char == "D")):
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

print("--------Problem 5---------")
print(min_remaining_watchlist("ABFCACDB")) 
print(min_remaining_watchlist("ACBBD"))

"""
Problem 6: Apply Operations to Show Ratings
You are given a 0-indexed array ratings of size n consisting of non-negative integers. 
Each integer represents the rating of a show in a streaming service.
You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), 
you will apply the following on the ith element of ratings:
If ratings[i] == ratings[i + 1], then multiply ratings[i] by 2 and set ratings[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.
For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array of ratings.
"""
def apply_rating_operations(ratings):
  pass

print("--------Problem 6---------")
print(apply_rating_operations([1, 2, 2, 1, 1, 0])) 
print(apply_rating_operations([0, 1])) 