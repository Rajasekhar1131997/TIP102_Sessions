"""
Problem 1: Track Podcast Episodes by Length
You are managing a podcast and need to analyze the lengths of the episodes. Given a list of episodes where 
each episode is represented by its duration in minutes, you want to determine how many episodes fall into each of the following time ranges: 
less than 30 minutes, 30 to 60 minutes, and more than 60 minutes.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def track_episode_lengths(episode_lengths):
    if not episode_lengths:
        return ()
    if len(episode_lengths) < 2:
        return (1)
    count1, count2, count3 = 0, 0, 0
    for length in episode_lengths:
        if length < 30:
            count1 += 1
        elif length >= 30 and length < 60:
            count2 += 1
        else:
            count3 += 1
    return (count1, count2, count3)

print("--------Problem 1---------")
episode_lengths = [15, 45, 32, 67, 22, 59, 70]
print(track_episode_lengths(episode_lengths))

episode_lengths_2 = [10, 25, 30, 45, 55, 65, 80]
print(track_episode_lengths(episode_lengths_2))

episode_lengths_3 = [30, 30, 30, 30, 30]
print(track_episode_lengths(episode_lengths_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 2: Identify Longest Episode
Given a list of episode durations from a podcast series, your task is to identify the longest episode. 
If there are multiple episodes with the maximum duration, return the duration of the longest episode.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def identify_longest_episode(durations):
    if not durations:
        return 0
    if len(durations) < 2:
        return durations
    durations.sort()
    return max(durations)

def identify_longest_episode(durations):
    if not durations:
        return 0
    if len(durations) == 1:
        return durations[0]
    max_duration = durations[0]
    for duration in durations[1:]:
        if duration > max_duration:
            max_duration = duration
    return max_duration

print("--------Problem 2---------")
print(identify_longest_episode([30, 45, 60, 45, 30]))
print(identify_longest_episode([20, 30, 40, 40, 30, 20]))  
print(identify_longest_episode([55, 60, 55, 60, 60]))
print("Time Complexity: is O(n logn) when used sort() function, otherwise O(n)")
print("Space Complexity: O(1)")

"""
Problem 3: Find Most Frequent Episode Length
You are given a list of episode lengths from a podcast series. Your task is to determine which episode length occurs most frequently. 
If there are multiple lengths with the same highest frequency, return the smallest episode length.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def most_frequent_length(episode_lengths):
    if not episode_lengths:
        return 0
    if len(episode_lengths) == 1:
        return episode_lengths[0]
    dictionary = {}
    for episode in episode_lengths:
        dictionary[episode] = dictionary.get(episode, 0) + 1
    max_count = max(dictionary.values())
    final_episode = [episode for episode, length in dictionary.items() if length == max_count]
    return min(final_episode)


print("--------Problem 3---------")
print(most_frequent_length([30, 45, 30, 60, 45, 30])) 
print(most_frequent_length([20, 20, 30, 30, 40, 40, 40])) 
print(most_frequent_length([60, 70, 80, 90, 100, 50]))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 4: Find Median Episode Length
Given a list of episode durations from a podcast series, find the median episode length. The median is the middle value when the list is sorted. 
If the list has an even number of elements, return the average of the two middle values.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_median_episode_length(durations):
    n = len(durations)
    if not durations:
        return 0
    if n == 1:
        return durations[0]
    durations.sort()
    if n %2 != 0:
        median = durations[n//2]
        return median
    else:
        sum = durations[n//2] + durations[(n-1)//2]
        median = sum / 2
        return median

print("--------Problem 4---------")
print(find_median_episode_length([45, 30, 60, 30, 90])) 
print(find_median_episode_length([90, 80, 60, 70, 50]))
print(find_median_episode_length([30, 10, 20, 40, 30, 50]))
print(find_median_episode_length([10, 20, 30, 40, 50, 60, 70, 80]))
print("Time Complexity: O(n logn)")
print("Space Complexity: O(1)")

"""
Problem 5: Find Unique Genres with Minimum Episode Length
Given a list of podcast episodes, each with a genre and length, find the unique genres where the 
shortest episode length is greater than or equal to a specified threshold. Return a list of these genres sorted alphabetically.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def unique_genres_with_min_length(episodes, threshold):
    if not episodes:
        return []
    if len(episodes) == 1:
        episode,genre,length = episodes[0]
        if length >= threshold:
            return [genre]
    result = []
    for episode,genre,length in episodes:
        if length >= threshold:
            if genre not in result:
                result.append(genre)
    result.sort()
    return result


print("--------Problem 5 (with List)---------")
print(unique_genres_with_min_length([("Episode 1", "Tech", 30), ("Episode 2", "Health", 45), ("Episode 3", "Tech", 35), ("Episode 4", "Entertainment", 60)], 30))  
print(unique_genres_with_min_length([("Episode A", "Science", 40), ("Episode B", "Science", 50), ("Episode C", "Art", 25), ("Episode D", "Art", 30)], 30)) 
print(unique_genres_with_min_length([("Episode X", "Music", 20), ("Episode Y", "Music", 15), ("Episode Z", "Drama", 25)], 20))
print(unique_genres_with_min_length([("Episode X", "Music", 20)], 20))
print("Time Complexity: O(n^2)")
print("Space Complexity: O(n)")

def unique_genres_with_min_length(episodes, threshold):
    if not episodes:
        return []
    seen = set()
    for episode, genre, length in episodes:
        if length >= threshold:
            seen.add(genre)
    return sorted(seen)


print("--------Problem 5 (with set)---------")
print(unique_genres_with_min_length([("Episode 1", "Tech", 30), ("Episode 2", "Health", 45), ("Episode 3", "Tech", 35), ("Episode 4", "Entertainment", 60)], 30))  
print(unique_genres_with_min_length([("Episode A", "Science", 40), ("Episode B", "Science", 50), ("Episode C", "Art", 25), ("Episode D", "Art", 30)], 30)) 
print(unique_genres_with_min_length([("Episode X", "Music", 20), ("Episode Y", "Music", 15), ("Episode Z", "Drama", 25)], 20))
print(unique_genres_with_min_length([("Episode X", "Music", 20)], 20))
print("Time Complexity: O(n logn)")
print("Space Complexity: O(n)")

"""
Problem 6: Find Recent Podcast Episodes
You are developing a podcast management system and need to keep track of the most recent podcast episodes. 
Given a list of episodes where each episode is represented by a unique ID, you need to implement a function that retrieves 
the most recent n episodes from the list in the order they were added.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def get_recent_episodes(episodes, n):
    if not episodes or n <= 0:
        return []
    if len(episodes) == 1:
        return episodes
    episodes.sort(reverse = True)
    n_length = len(episodes)
    if n > n_length:
        n = n_length
    result = []
    for i in range(0,n):
        result.append(episodes[i])
    return result


print("--------Problem 6---------")
episodes1 = ['episode1', 'episode2', 'episode3', 'episode4']
n = 3
print(get_recent_episodes(episodes1, n))

episodes2 = ['ep1', 'ep2', 'ep3']
n = 2
print(get_recent_episodes(episodes2, n))

episodes3 = ['a', 'b', 'c', 'd']
n = 5
print(get_recent_episodes(episodes3, n))
print("Time Complexity: O(n logn) ")
print("Space Complexity: O(n)")

def get_recent_episodes(episodes, n):
    if not episodes or n <= 0:
        return []
    if len(episodes) == 1:
        return episodes
    return episodes[-n:][::-1] #[-n:] takes the last n elements in original order and [::-1] reverses the list


print("--------Problem 6(Optimized code)---------")
episodes1 = ['episode1', 'episode2', 'episode3', 'episode4']
n = 3
print(get_recent_episodes(episodes1, n))

episodes2 = ['ep1', 'ep2', 'ep3']
n = 2
print(get_recent_episodes(episodes2, n))

episodes3 = ['a', 'b', 'c', 'd']
n = 5
print(get_recent_episodes(episodes3, n))
print("Time Complexity: O(n) ")
print("Space Complexity: O(n)")

"""
Problem 7: Reorder Podcast Episodes
You are designing a feature for a podcast app that allows users to reorder their list of episodes. 
The episodes are initially in a stack (LIFO order). Write a function to reorder the episodes based on a list of indices specifying the new order. 
The indices are 0-based and represent the new position of each episode in the stack.
For instance, if the stack contains episodes [A, B, C, D] and the indices are [2, 0, 3, 1], it means that the episode 
originally at index 0 should move to index 2, the episode at index 1 should move to index 0, and so on.
The function should return the reordered list of episodes.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def reorder_stack(stack, indices):
    if not stack and not indices:
        return []
    if len(stack) == 1 and len(indices) == 1:
        return stack
    if len(stack) == len(indices):
        dictionary = dict(zip(stack,indices))
        sorted_dictionary = sorted(dictionary.items(), key=lambda x:x[1])
    return [episode for episode, index in sorted_dictionary]

def reorder_stack(stack, indices):
    if not stack and not indices:
        return []
    if len(stack) == 1 and len(indices) == 1:
        return stack
    if len(stack) == len(indices):
        result = [None] * len(stack)
        for old_pos, episode in enumerate(stack):
            new_pos = indices[old_pos]
            result[new_pos] = episode
    return result

print("--------Problem 7---------")
stack1 = ['Episode1', 'Episode2', 'Episode3', 'Episode4']
indices = [2, 0, 3, 1]
print(reorder_stack(stack1, indices)) 

stack2 = ['A', 'B', 'C', 'D']
indices = [1, 2, 3, 0]
print(reorder_stack(stack2, indices)) 

stack3 = ['Alpha', 'Beta', 'Gamma']
indices = [0, 2, 1]
print(reorder_stack(stack3, indices)) 
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 8: Find Longest Consecutive Listen Gaps
You are building a feature for a podcast app that helps users identify the longest period of time between listening to 
consecutive episodes of a podcast. Given a list of episode listen timestamps (in minutes since midnight) sorted in ascending order, 
your task is to determine the longest gap between consecutive listens.
Write a function to find the longest gap between consecutive listens.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_longest_gap(timestamps):
    n = len(timestamps)
    if not timestamps:
        return 0
    if n < 2:
        return 0
    max_difference = float('-inf')
    prev_value = timestamps[0]
    for time in range(1,n):
        current_value = timestamps[time]
        difference = abs(current_value - prev_value)
        if difference > max_difference:
            max_difference = difference
        prev_value = timestamps[time]
    return max_difference

print("--------Problem 8---------")
timestamps1 = [30, 50, 70, 100, 120, 150]
print(find_longest_gap(timestamps1))

timestamps2 = [10, 20, 30, 50, 60, 90]
print(find_longest_gap(timestamps2))

timestamps3 = [5, 10, 15, 25, 35, 45]
print(find_longest_gap(timestamps3))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")