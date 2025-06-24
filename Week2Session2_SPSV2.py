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
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    mapping = {}
    p = 0
    for char in key:
        if char != " " and char not in mapping:
            mapping[char] = alphabets[p]
            p += 1
            if p == 26:
                break
    new_message = []
    for char in message:
        if char == " ":
            new_message.append(" ")
        else:
            new_message.append(mapping[char])
    return ''.join(new_message)
        
        

print("--------Problem 3---------")
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "hntu depcte lxejw lxwntu zwx piqfx"

print(decode_message(key2, message2))

"""
Problem 4: Longest Harmonious Travel Sequence
In a list of travel packages, we define a harmonious travel sequence as a sequence where the difference between 
the maximum and minimum travel ratings is exactly 1.
Given an integer array rating, return the length of the longest harmonious travel sequence among all its possible subsequences.
A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing 
the order of the remaining elements.
You are provided with a partially implemented solution that contains bugs. 
Your task is to identify and fix the bugs to ensure the solution works correctly.
"""
def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        frequency[rating] = frequency.get(rating, 0) + 1
    
    max_length = 0

    # Find the longest harmonious sequence
    for rating, count in frequency.items():
        if rating + 1 in frequency:
            length = count + frequency[rating+1]
            max_length = max(max_length, length)

    return max_length


durations1 = [1, 3, 2, 2, 5, 2, 3, 7]
durations2 = [1, 2, 3, 4]
durations3 = [1, 1, 1, 1]

print("--------Problem 4---------")
print(find_longest_harmonious_travel_sequence(durations1))
print(find_longest_harmonious_travel_sequence(durations2)) 
print(find_longest_harmonious_travel_sequence(durations3)) 

"""
Problem 5: Check if All Destinations in a Route are Covered
You are given a 2D integer array trips and two integers start_dest and end_dest. Each trips[i] = [starti, endi] 
represents an inclusive travel interval between starti and endi.
Return True if each destination in the inclusive route [start_dest, end_dest] is covered by at least one trip in trips. Return False otherwise.
A destination x is covered by a trip trips[i] = [starti, endi] if starti <= x <= endi.
"""
# need to clear out this problem
def is_route_covered(trips, start_dest, end_dest):
    for x in range(start_dest, end_dest+1):
        covered = False
        for a, b in trips:
            if a <= x <= b:
                covered = True
                break
        if not covered:
            return False
    return True

trips1 = [[1, 2], [3, 4], [5, 6]]
start_dest1, end_dest1 = 2, 5

trips2 = [[1, 10], [10, 20]]
start_dest2, end_dest2 = 21, 21

trips3 = [[1, 2], [3, 5]]
start_dest3, end_dest3 = 2, 5

print("--------Problem 5---------")
print(is_route_covered(trips1, start_dest1, end_dest1))
print(is_route_covered(trips2, start_dest2, end_dest2))
print(is_route_covered(trips3, start_dest3, end_dest3))

"""
Problem 6: Most Popular Even Destination
Given a list of integers destinations, where each integer represents the popularity score of a destination, 
return the most popular even destination.
If there is a tie, return the smallest one. If there is no such destination, return -1.
"""
def most_popular_even_destination(destinations):
    freq = {}
    for i in destinations:
        if i % 2 == 0:
            freq[i] = freq.get(i, 0) + 1
    
    if not freq:
        return -1
    best_dest = max(freq, key=lambda x: (freq[x],-x))
    return best_dest

destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

print("--------Problem 6---------")
print(most_popular_even_destination(destinations1))
print(most_popular_even_destination(destinations2))
print(most_popular_even_destination(destinations3))

"""
Problem 7: Check if Itinerary is Valid
You are given an itinerary itinerary representing a list of trips between cities, where each city is represented by an integer. 
We consider an itinerary valid if it is a permutation of an itinerary template base[n].
The template base[n] is defined as [1, 2, ..., n - 1, n, n] 
(in other words, it is an itinerary of length n + 1 that visits cities 1 to n - 1 exactly once, plus visits city n twice). 
For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
Return True if the given itinerary is valid, otherwise return False.
A permutation is an arrangement of a set of elements. For example [3, 2, 1] and [2, 3, 1] are both possible permutations 
of the set of numbers 1, 2, and 3.
"""
def is_valid_itinerary(itinerary):
    if not itinerary:
        return False
    counts = {} 
    for city in itinerary:
        counts[city] = counts.get(city, 0) + 1
    base = max(counts.keys())
    if len(itinerary) != base + 1:
        return False
    if set(counts.keys()) != set(range(1,base+1)):
        return False
    if counts.get(base,0)!=2:
        return False
    for i in range(1,base):
        if counts.get(i,0)!=1:
            return False
    return True

itinerary1 = [2, 1, 3]
itinerary2 = [1, 3, 3, 2]
itinerary3 = [1, 1]

print("--------Problem 7---------")
print(is_valid_itinerary(itinerary1))
print(is_valid_itinerary(itinerary2))
print(is_valid_itinerary(itinerary3))

"""
Problem 8: Finding Common Tourist Attractions with Least Travel Time
Given two lists of tourist attractions, tourist_list1 and tourist_list2, find the common attractions with the least total travel time.
A common attraction is one that appears in both tourist_list1 and tourist_list2.
A common attraction with the least total travel time is a common attraction such that if it appeared at 
tourist_list1[i] and tourist_list2[j] then i + j should be the minimum value among all the other common attractions.
Return all the common attractions with the least total travel time. Return the answer in any order.
"""
def find_attractions(tourist_list1, tourist_list2):
    tl1 = {}
    for i, attraction in enumerate(tourist_list1):
        tl1[attraction] = i
    best = float('inf')
    result = []
    for j, attraction in enumerate(tourist_list2):
        if attraction in tl1:
            total = tl1[attraction] + j
            if total < best:
                best = total
                result = [attraction]
            elif total == best:
                result.append(attraction)
    return result


print("--------Problem 7---------")
tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Colosseum","Trevi Fountain","Pantheon","Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Disneyland","Eiffel Tower","Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach","mountain","forest"]
tourist_list2 = ["mountain","beach","forest"]

print(find_attractions(tourist_list1, tourist_list2))