"""
Problem 1: Meme Length Filter
You need to filter out memes that are too long from your dataset. Memes that exceed a certain length are less likely to go viral.
Write the filter_meme_lengths() function, which filters out memes whose lengths exceed a given limit. 
The function should return a list of meme texts that are within the acceptable length.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def filter_meme_lengths(memes, max_length):
    result = []
    if not memes:
        return []
    for meme in memes:
        if len(meme) <= max_length:
            result.append(meme)
    return result


memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

print("--------Problem 1---------")
print(filter_meme_lengths(memes, 20))
print(filter_meme_lengths(memes_2, 15))
print(filter_meme_lengths(memes_3, 10))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 2: Top Meme Creators
You want to identify the top meme creators based on the number of memes they have created.
Write the count_meme_creators() function, which takes a list of meme dictionaries and returns 
the creators' names and the number of memes they have created.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def count_meme_creators(memes):
    dictionary = {}
    if not memes:
        return {}
    if len(memes) < 2:
        return memes
    for meme in memes:
        creator_name = meme["creator"]
        dictionary[creator_name] = dictionary.get(creator_name, 0) + 1
    return dictionary

memes = [
    {"creator": "Alex", "text": "Meme 1"},
    {"creator": "Jordan", "text": "Meme 2"},
    {"creator": "Alex", "text": "Meme 3"},
    {"creator": "Chris", "text": "Meme 4"},
    {"creator": "Jordan", "text": "Meme 5"}
]

memes_2 = [
    {"creator": "Sam", "text": "Meme 1"},
    {"creator": "Sam", "text": "Meme 2"},
    {"creator": "Sam", "text": "Meme 3"},
    {"creator": "Taylor", "text": "Meme 4"}
]

memes_3 = [
    {"creator": "Blake", "text": "Meme 1"},
    {"creator": "Blake", "text": "Meme 2"}
]

print("--------Problem 2---------")
print(count_meme_creators(memes))
print(count_meme_creators(memes_2))
print(count_meme_creators(memes_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 3: Meme Trend Identification
You're tasked with identifying trending memes. A meme is considered "trending" if it appears in the dataset multiple times.
Write the find_trending_memes() function, which takes a list of meme texts and returns a list of trending memes, 
where a trending meme is defined as a meme that appears more than once in the list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_trending_memes(memes):
    result = []
    dictionary = {}
    if not memes:
        return []
    if len(memes) < 2:
        return memes
    for meme in memes:
        dictionary[meme] = dictionary.get(meme, 0) + 1
    for meme, value in dictionary.items():
        if value > 1:
            result.append(meme)
    return result


memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print("--------Problem 3---------")
print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 4: Reverse Meme Order
You want to see how memes would trend if they were posted in reverse order.
Write the reverse_memes() function, which takes a list of memes (representing the order they were posted) 
and returns a new list with the memes in reverse order.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
# if we need to make use of new list, below is the approach
def reverse_memes(memes):
    if not memes:
        return []
    if len(memes) < 2:
        return memes
    result = []
    for meme in memes[::-1]:
        result.append(meme)
    return result

#this is more simplied version of the above code or we can use reversed function
def reverse_memes(memes):
    if not memes:
        return []
    if len(memes) < 2:
        return memes
    return memes[::-1]

memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print("--------Problem 4---------")
print(reverse_memes(memes))
print(reverse_memes(memes_2))
print(reverse_memes(memes_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 5: Trending Meme Pairs
You've been given partially completed code to identify pairs of memes that frequently appear together in posts. 
However, before you can complete the implementation, you need to ensure the plan is correct and then review 
the provided code to identify and fix any potential issues.
Your task is to:
Plan:
Write a detailed plan (pseudocode or step-by-step instructions) on how you would approach solving this problem. Consider how you would:
Iterate through each post.
Generate pairs of memes.
Count the frequency of each pair.
Identify pairs that appear more than once.
Ensure the final result is accurate and efficient.

Review:
Examine the provided code and answer the following questions:
Are there any logical errors in the code? If so, what are they, and how would you fix them?
Are there any inefficiencies in the code that could be improved? If so, how would you optimize it?
Does the code correctly handle edge cases, such as an empty list of posts or posts with only one meme?
"""
def find_trending_meme_pairs(meme_posts):
    pair_count = {}

    for post in meme_posts:
        for i in range(len(post)):
            for j in range(i+1, len(post)):
                meme1 = post[i]
                meme2 = post[j]

                if meme1 > meme2:
                    meme1, meme2 = meme2, meme1
                pair = (meme1, meme2)
                pair_count[pair] = pair_count.get(pair, 0) + 1

    trending_pairs = []
    for pair, count in pair_count.items():
        if count >= 2:
            trending_pairs.append(pair)

    return trending_pairs

meme_posts_1 = [
    ["Dogecoin to the moon!", "Distracted boyfriend"],
    ["One does not simply walk into Mordor", "Dogecoin to the moon!"],
    ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"],
    ["Distracted boyfriend", "One does not simply walk into Mordor"]
]

meme_posts_2 = [
    ["Surprised Pikachu", "This is fine"],
    ["Expanding brain", "Surprised Pikachu"],
    ["This is fine", "Expanding brain"],
    ["Surprised Pikachu", "This is fine"]
]

meme_posts_3 = [
    ["Y U No?", "First world problems"],
    ["Philosoraptor", "Bad Luck Brian"],
    ["First world problems", "Philosoraptor"],
    ["Y U No?", "First world problems"]
]

print("--------Problem 5---------")
print(find_trending_meme_pairs(meme_posts_1))
print(find_trending_meme_pairs(meme_posts_2))
print(find_trending_meme_pairs(meme_posts_3))
print("Time Complexity: O(n^2)")
print("Space Complexity: O(n^2)")

"""
Problem 6: Meme Popularity Queue
You're tasked with analyzing the order in which memes gain popularity. Memes are posted in a sequence, 
and their popularity grows as they are reposted.
Write the simulate_meme_reposts() function, which takes a list of memes (representing their initial posting order) 
and simulate their reposting by processing each meme in the queue. Each meme can be reposted multiple times, and for each repost, 
it should be added back to the queue. The function should return the final order in which all reposts are processed.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
from collections import deque
def simulate_meme_reposts(memes, reposts):
    q = deque((meme, count) for meme, count in zip(memes, reposts))
    result = []
    while q:
        meme_id, remianing = q.popleft()
        result.append(meme_id)
        if remianing > 1:
            q.append((meme_id, remianing-1))
    return result

memes = ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"]
reposts1 = [2, 1 , 3]

memes_2 = ["Surprised Pikachu", "This is fine", "Expanding brain"]
reposts2 = [1, 2, 2]

memes_3 = ["Y U No?", "Philosoraptor"]
reposts3 = [3, 1]

print("--------Problem 6---------")
print(simulate_meme_reposts(memes, reposts1))
print(simulate_meme_reposts(memes_2, reposts2))
print(simulate_meme_reposts(memes_3, reposts3))
print("Time Complexity: O(n+R)")
print("Space Complexity: O(n+R)")

"""
Problem 7: Search for Viral Meme Groups
You're interested in identifying groups of memes that, when combined, have a total popularity score closest to a target value. 
Each meme has an associated popularity score, and you want to find the two memes whose combined popularity score is closest to the target value. 
The list of memes is already sorted by their popularity scores.
Write the find_closest_meme_pair() function, which takes a sorted list of memes (each with a name and a popularity score) 
and a target popularity score. The function should return the names of the two memes whose combined popularity score is closest to the target.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_closest_meme_pair(memes, target):
    left, right = 0, len(memes) - 1
    best_diff = float('inf')
    best_pair = (None, None)

    while left < right:
        name_left, score_left = memes[left]
        name_right, score_right = memes[right]
        score = score_left + score_right
        difference = abs(score-target)

        if difference < best_diff:
            best_diff = difference
            best_pair = (name_left, name_right)
        if score < target:
            left += 1
        else:
            right -= 1
    return best_pair

memes_1 = [("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7), ("One does not simply walk into Mordor", 12)]
memes_2 = [("Surprised Pikachu", 2), ("This is fine", 6), ("Expanding brain", 9), ("Y U No?", 15)]
memes_3 = [("Philosoraptor", 1), ("Bad Luck Brian", 4), ("First world problems", 8), ("Y U No?", 13)]

print("--------Problem 7---------")
print(find_closest_meme_pair(memes_1, 13))
print(find_closest_meme_pair(memes_2, 10))
print(find_closest_meme_pair(memes_3, 12))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 8: Analyze Meme Trends
You need to analyze the trends of various memes over time. You have a dataset where each meme has a name, 
a list of daily popularity scores (number of reposts each day), and other metadata.
Write the find_trending_meme() function, which takes in a list of memes (each with a name and a list of daily repost counts) 
and a time range (represented by a start and end day, inclusive). The function should return the name of the meme 
with the highest average reposts over the specified period. If there is a tie, return the meme that appears first in the list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_trending_meme(memes, start_day, end_day):
    if not memes:
        return None
    best_name = None
    best_avg = float('-inf')
    window_size = end_day - start_day + 1
    for meme in memes:
        segment = meme["reposts"][start_day : end_day + 1]
        average = sum(segment) / window_size
        if average > best_avg:
            best_avg = average
            best_name = meme["name"]
    return best_name

memes = [
    {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
    {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
    {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}
]

memes_2 = [
    {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
    {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
    {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
]

memes_3 = [
    {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
    {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
]

print("--------Problem 8---------")
print(find_trending_meme(memes, 1, 3))
print(find_trending_meme(memes_2, 0, 2))
print(find_trending_meme(memes_3, 2, 4))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")