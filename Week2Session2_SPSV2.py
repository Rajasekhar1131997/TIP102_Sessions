"""
Problem 1: Filter Destinations
You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. 
Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary destinations 
and a rating_threshold as parameters. The function should iterate through the dictionary and remove all destinations 
that have a rating strictly below the rating_threshold. Return the updated dictionary.
"""
def remove_low_rated_destinations(destinations, rating_threshold):
    new_dictionary = {}
    for city, rating in destinations.items():
        if rating >= rating_threshold:
            new_dictionary[city] = rating
    return new_dictionary

destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print("--------Problem 1---------")
print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))

"""
Problem 2: Unique Travel Souvenirs
As a seasoned traveler, you've collected a variety of souvenirs from different destinations. 
You have an array of string souvenirs, where each string represents a type of souvenir. 
You want to know if the number of occurrences of each type of souvenir in your collection is unique.
Write a function that takes in an array souvenirs and returns True if the number of occurrences of each value 
in the array is unique, or False otherwise.
"""
def unique_souvenir_counts(souvenirs):
    if not souvenirs:
        return False
    frequency = {}
    for i in souvenirs:
        frequency[i] = frequency.get(i, 0) + 1
    seen = set()
    for value in frequency.values():
        if value in seen:
            return False
        else:
            seen.add(value)
    return True

souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print("--------Problem 2---------")
print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))

"""
Problem 3: Secret Beach
You make friends with a local at your latest destination, and they give you a coded message with the name of a secret beach 
most tourists don't know about! You are given the strings key and message which represent a cipher key and a secret message, respectively. 
The steps to decode the message are as follows:
Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "travel the world" (an actual key would have at least one instance of each letter in the alphabet), we have the partial 
substitution table of ('t' -> 'a', 'r' -> 'b', 'a' -> 'c', 'v' -> 'd', 'e' -> 'e', 'l' -> 'f', 'h' -> 'g', 'w' -> 'h', 'o' -> 'i', 'd' -> 'j').
Write a function decode_message() that accepts the strings key and message and returns a string representing the decoded message.
"""
def decode_message(key, message):
    sub_table = {
        't' : 'a',
        'h' : 'b',
        'e' : 'c',
        'q' : 'd',
        'u' : 'e',
        'i' : 'f',
        'c' : 'g',
        'k' : 'h',
        'b' : 'i',
        'r' : 'j',
        'o' : 'k',
        'w' : 'l',
        'n' : 'm',
        'f' : 'n',
        'x' : 'o',
        'j' : 'p',
        'm' : 'q',
        'p' : 'r',
        's' : 's',
        'v' : 't',
        'l' : 'u',
        'a' : 'v',
        'z' : 'w',
        'y' : 'x',
        'd' : 'y',
        'g' : 'z'
    }

print("--------Problem 3---------")
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "hntu depcte lxejw lxwntu zwx piqfx"

print(decode_message(key2, message2))