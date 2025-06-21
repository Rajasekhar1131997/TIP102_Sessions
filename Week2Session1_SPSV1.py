"""
Breakout room Standard Problem Set Version 1: Problem 1: 
Festival Lineup
Given two lists of strings artists and set_times of length n, 
write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    pass

UNDERSTAND:
1. Input and output
    - input: 2 lists
    - output: match the 2 lists together
2. edge cases
    - 2 empty lists
    - 
3. Run time and space contraints
    - very large list? -> no
4. anything not allowed?
    - no
5. happy case
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

Output: {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}

MATCH: 
    - dictionary

PLAN:
1. use zip to match our two lists

"""
#IMPLEMENT
def lineup(artists, set_times):
    zipped_values = zip(artists, set_times)
    dictionary = dict(zipped_values)
    return dictionary

#test 
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print("----Problem 1--------")
print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


"""
Breakout room Standard Problem Set Version 1: Problem 2: 
Planning App
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, 
users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to 
dictionaries containing the day, time, and stage they are playing on. 
Return the dictionary containing the information about the given artist.
If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    pass

UNDERSTAND:
1. Input and output
    - input: string, dictionary
    - output: dictionary (artists info)
2. edge cases
    - artist not in dictionary -> return artists not found
3. Run time and space contraints
    - ignore
4. anything not allowed?
    - N/A
5. happy case
inputs:
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
output : {'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}

MATCH: 
    - dictionary

PLAN:
1. using get
"""
#IMPLEMENT
def get_artist_info(artist, festival_schedule):
    result = festival_schedule.get(artist, "{'message': 'Artist not found'}")
    return result
#test implementation
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print("----Problem 2--------")
print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))
print(get_artist_info("Lawrence", festival_schedule))  

"""
Breakout room Standard Problem Set Version 1: Problem 3: Ticket Sales
A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.
def total_sales(ticket_sales):
    pass

UNDERSTAND:
1. Input and output
    - input: dictionary
    - output: number of tickets sold
2. edge cases
    - empty dictionary -> 0
3. Run time and space contraints
    - N/A
4. anything not allowed?
    - N/A
5. happy case
    - input: ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
    - output: 4500

MATCH: 
    - dictionary

PLAN:
1. loop over dictionary
2. add each value for the keys

"""
#IMPLEMENT
def total_sales(ticket_sales):
    total = 0
    for i in ticket_sales.values():
        total += i
    return total

print("----Problem 3--------")
#test implementation
ticket_sales = {}
print(total_sales(ticket_sales))

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))

"""
Breakout room Standard Problem Set Version 1: Problem 4: Scheduling Conflict
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. 
Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, 
implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule 
each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs
that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    pass

UNDERSTAND:
1. Input and output
    - input: 2 dictionaries
    - output: dictionary, list of matching values between both inputs
2. edge cases
    - empty dictionaries
3. Run time and space contraints
    - N/A
4. anything not allowed?
    - N/A
5. happy case
    - 
input:
    venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

Output: {"Stromae": "9:00 PM", "HARDY": "7:00 PM"}

MATCH: 
    - dictionary

PLAN:
1. make new dictionary to store conflicts
2. loop through both and compare schedules
3. if they match, add to new dictionary
4. return new dictionary

"""
#IMPLEMENT
def identify_conflicts(venue1_schedule, venue2_schedule):
    matches = {}
    for times in venue1_schedule:
        if times in venue2_schedule and venue1_schedule[times] == venue2_schedule[times]:
            matches[times] = venue1_schedule[times]
    return matches

#test implementation
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print("----Problem 4--------")
print(identify_conflicts(venue1_schedule, venue2_schedule))

"""
Breakout room Standard Problem Set Version 1: Problem 5: Best Set
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps 
attendees id numbers to the artist they voted for, return the artist that had the most number of votes. 
If there is a tie, return any artist with the top number of votes.
"""
def best_set(votes):
    max_votes = {}
    for artist in votes.values():
        max_votes[artist] = max_votes.get(artist, 0) + 1
    top_artist = max(max_votes, key=max_votes.get)
    return top_artist

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print("----Problem 5--------")
print(best_set(votes1))
print(best_set(votes2))

"""
Problem 6: Performances with Maximum Audience
You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.
Return the combined audience size of all performances in audiences with the maximum audience size.
The audience size of a performance is the number of people who attended that performance.
"""
def max_audience_performances(audiences):
    if not audiences:
        return 0
    M = max(audiences)
    total = 0
    for size in audiences:
        if size == M:
            total += size
    return total

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print("----Problem 6--------")
print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

"""
Problem 7: Performances with Maximum Audience II
If you used a dictionary as part of your solution to max_audience_performances() in the previous problem, 
try reimplementing the function without using a dictionary. If you implemented max_audience_performances() 
without using a dictionary, try solving the problem with a dictionary.
Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?
"""
def max_audience_performances(audiences):
    dictionary = {}
    for size in audiences:
        dictionary[size] = dictionary.get(size, 0) + size
    M = max(dictionary.keys())
    return dictionary[M]


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print("----Problem 7--------")
print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

"""
Problem 8: Popular Song Pairs
Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, 
return the number of popular song pairs.
A pair (i, j) is called popular if the songs have the same popularity score and i < j.
Hint: number of pairs = (n x n-1)/2
"""
def num_popular_pairs(popularity_scores):
    frequency = {}
    for score in popularity_scores:
        frequency[score] = frequency.get(score, 0) + 1
    total_pairs = 0
    for value in frequency.values():
        if value> 1:
            total_pairs += (value * (value-1)//2)
    return total_pairs

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print("-----Problem 8-------")
print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))

"""
Problem 9: Stage Arrangement Difference Between Two Performances
You are given two strings s and t representing the stage arrangements of performers in two different performances 
at a music festival, such that every performer occurs at most once in s and t, and t is a permutation of s.
The stage arrangement difference between s and t is defined as the sum of the absolute difference between 
the index of the occurrence of each performer in s and the index of the occurrence of the same performer in t.
Return the stage arrangement difference between s and t.
A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].
Hint: Absolute value function
"""
# problem yet to solve
def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """



s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print("-----Problem 9-------")
print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))

"""
Problem 10: VIP Passes and Guests
You're given strings vip_passes representing the types of guests that have VIP passes, and guests representing 
the guests you have at the music festival. Each character in guests is a type of guest you have. 
You want to know how many of the guests you have are also VIP pass holders.
Letters are case sensitive, so "a" is considered a different type of guest from "A".
Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.
1. Create an empty set called vip_set.
2. For each character in vip_passes, add it to vip_set.
3. Initialize a counter variable to 0.
4. For each character in guests:
   * If the character is in vip_set, increment the count by 1.
5. Return the count.
"""
def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    for i in vip_passes:
        vip_set.add(i)
    count = 0
    for char in guests:
        if char in vip_set:
            count += 1
    return count

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print("-----Problem 10-------")
print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

"""
Problem 11: Performer Schedule Pattern
Given a string pattern and a string schedule, return True if schedule follows the same pattern. Return False otherwise.
Here, "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in schedule.
You are provided with a partially implemented and buggy version of the solution. Identify and fix the bugs in the code. 
Then, perform a thorough code review and suggest improvements.
"""
def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False
    
    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                    return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
                genre_to_char[genre] = char
    return True
pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print("-----Problem 11-------")
print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))