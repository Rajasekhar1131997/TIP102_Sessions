"""
Problem 1: NFT Name Extractor
You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs 
from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, 
and current value.
Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity.
"""
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print("--------Problem 1---------")
print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


"""
Problem 2: NFT Collection Review
You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. 
One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. 
A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.
Task:
Review the provided code and identify the bug(s).
Explain what the bug is and how it affects the output.
Refactor the code to fix the bug(s) and provide the correct implementation.
"""
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print("--------Problem 2---------")
print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 3: Identify Popular Creators
You have been tasked with identifying the most popular NFT creators in your collection. 
A creator is considered "popular" if they have created more than one NFT in the collection.
Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe 
your solution has the stated time and space complexity.
"""
def identify_popular_creators(nft_collection):
    result = []
    dictionary = {}

    for nft in nft_collection:
        creator = nft["creator"]
        dictionary[creator] = dictionary.get(creator, 0) + 1

    for key, value in dictionary.items():
        if value > 1:
            result.append(key)
    return result


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print("--------Problem 3---------")
print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 4: NFT Collection Statistics
You want to provide an overview of the NFT collection to potential buyers. One key statistic is the average value of the NFTs in the collection. 
However, if the collection is empty, the average value should be reported as 0.
Write the average_nft_value function, which calculates and returns the average value of the NFTs in the collection.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def average_nft_value(nft_collection):
    n = len(nft_collection)
    if n == 0:
        return 0
    total = 0.0
    for value in nft_collection:
        total += value["value"]
    return total / n


print("--------Problem 4---------")
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 5: NFT Tag Search
Some NFTs are grouped into collections, and each collection might contain multiple NFTs. 
Additionally, each NFT can have a list of tags describing its style or theme (e.g., "abstract", "landscape", "modern"). 
You need to search through these nested collections to find all NFTs that contain a specific tag.
Write the search_nft_by_tag() function, which takes in a nested list of NFT collections and a tag to search for. 
The function should return a list of NFT names that have the specified tag.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe 
your solution has the stated time and space complexity.
"""
def search_nft_by_tag(nft_collections, tag):
    result = []
    for nfts in nft_collections:
        for i in nfts:
             if tag in i["tags"]:
                  result.append(i["name"])
    return result


nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print("--------Problem 5---------")
print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))
print("Time Complexity: O(n x t) where t is the average number of tags per NFT")
print("Space Complexity: O(n)")

"""
Problem 6: NFT Queue Processing
NFTs are added to a processing queue before they are displayed. The queue processes NFTs in a First-In, First-Out (FIFO) manner. 
Each NFT has a processing time, and you need to determine the order in which NFTs should be processed based on their initial position in the queue.
Write the process_nft_queue() function, which takes a list of NFTs. The function should return a list of NFT names in the order they were processed.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
for why you believe your solution has the stated time and space complexity.
"""
def process_nft_queue(nft_queue):
    result = []
    for nft in nft_queue:
        result.append(nft["name"])
    return result


print("--------Problem 6---------")
nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 7: Validate NFT Addition
You want to ensure that NFTs are added in a balanced way. For example, every "add" action must be properly 
closed by a corresponding "remove" action.
Write the validate_nft_actions() function, which takes a list of actions (either "add" or "remove") 
and returns True if the actions are balanced, and False otherwise.
A sequence of actions is considered balanced if every "add" has a corresponding "remove" and no "remove" occurs before an "add".
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def validate_nft_actions(actions):
    if not actions:
        return False
    if len(actions) < 2:
        return False
    balance = 0
    for action in actions:
        if action == "add":
            balance += 1
        elif action == "remove":
            if balance == 0:
                return False
            balance -= 1
        else:
            return False
    return balance == 0


actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print("--------Problem 7---------")
print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))
print("Time Complexity: O(n)")
print("Space Compelxity: O(1)")

"""
Problem 8: Find Closest NFT Values
Buyers often look for NFTs that are closest in value to their budget. Given a sorted list of NFT values and a budget, 
you need to find the two NFT values that are closest to the given budget: 
one that is just below or equal to the budget and one that is just above or equal to the budget. 
If an exact match exists, it should be included as one of the values.
Write the find_closest_nft_values() function, which takes a sorted list of NFT values and a budget, 
and returns the pair of the two closest NFT values.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_closest_nft_values(nft_values, budget):
    n = len(nft_values)
    low = None
    high = None

    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if nft_values[mid] == budget:
            return (budget, budget)
        elif nft_values[mid] < budget:
            low = nft_values[mid]
            l = mid + 1
        else:
            r = mid - 1

    if l < n:
        high = nft_values[l]

    return (low, high)

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print("--------Problem 8---------")
print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")