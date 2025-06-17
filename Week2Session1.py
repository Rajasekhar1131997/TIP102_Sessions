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
    return dict(zip(artists, set_times))

#test 
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


"""
Breakout room Standard Problem Set Version 1: Problem 2: 
Planning App
You are designing an app for your festival to help attendees 
have the best experience possible! As part of the application, 
users will be able to easily search their favorite artist and 
find out the day, time, and stage the artist is playing at. 
Write a function get_artist_info() that accepts a string artist 
and a dictionary festival_schedule mapping artist's names to 
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
    return festival_schedule.get((artist),  {"message": "Artist not found"})
#test implementation
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

"""
Breakout room Standard Problem Set Version 1: Problem 3: 
Ticket Sales
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


#test implementation
ticket_sales = {}
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
print(total_sales(ticket_sales))

"""
Breakout room Standard Problem Set Version 1: Problem 4: 
Scheduling Conflict
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that are the same in each schedule.

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

print(identify_conflicts(venue1_schedule, venue2_schedule))

"""
Breakout room Standard Problem Set Version 1: Problem 5: 
Best Set
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    pass

UNDERSTAND:
1. Input and output
    - input: dictionary
    - output: most frequent value
2. edge cases
    - 
3. Run time and space contraints
    - 
4. anything not allowed?
    -
5. happy case
    -

MATCH: 
    - 

PLAN:
1. 

"""
#IMPLEMENT


#test implementation