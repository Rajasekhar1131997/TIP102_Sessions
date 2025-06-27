#Problem 1
"""
#U:
- i/o: we're taking a list of dictionaries as input, we need to output the names from each dictionary in a list
- edge cases: 
    empty dictionary --> empty list
    dictionary doesn't have name key --> empty list
    happy case: a short list of dictionaries which all have a name key
#M:
- Lists and dictionaries
#P:
- Create an empty list which will store our answer
- 
#I:
#R:
#E:
"""
def extract_nft_names1(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

  
#Problem 2
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

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))


"""
#U:i/o = list of dictionaries/ list of popular creators
#M: lists, dictionaries
#P: 1. Initialize a list
#   2. Create a hashmap of artists and number of times they appear
#   3. Go through hashmap and check if value is greater than 1, then append to list
#   4. return list


#R:
#E:

"""
#Problem 3
#I:
def identify_popular_creators(nft_collection):
    res = []
    hm = {}
    
    for nft in nft_collection:
        creator_name = nft["creator"]
        hm[creator_name] = hm.get(creator_name, 0)+1
            
    for key,value in hm.items():
        if value > 1:
            res.append(key)
    return res

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

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))

#Problem 4
"""
U
    i/o: list of dictionaries for input, outputting an float
    edge cases:empty -> 0
    happy case:nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
    ] -> 5.7

M
    lists and dictionaries
P:
    1. Calculate the length of the collection or list
    2. If the length is 0, we return 0
    3. Initialize total = 0.0
    4. loop through each value in nft_collection
        add that value to the total
    5. calculate the average 
    6. return the average
    
Implement

R

E

"""
def average_nft_value(nft_collection):
    n = len(nft_collection)
    if n == 0:
        return 0
    total = 0.0
    for value in nft_collection:
        total += value["value"]
    
    return total / n


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

#Problem 5
"""
U: i: list of dcitionaries where the tag is a list / o: list of names
M: lists, dictionaries
P: 
    1. initialize an empty list res
    2. iterate through list of dictionaries
        if tag contains keyword given
            append to list res
    3. return list
I
R
E
"""
def search_nft_by_tag(nft_collections, tag):
    res = []
    for nfts in nft_collections:
        if nfts["tags"] == tag:
            res.append(nfts["name"])
    return res

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

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))