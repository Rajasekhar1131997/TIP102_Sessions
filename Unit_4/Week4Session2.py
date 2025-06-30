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
print("Time Complexity: ")
print("Space Complexity: ")