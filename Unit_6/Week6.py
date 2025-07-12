"""
#Problem 1
class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
		
#top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))
bad_romance = SongNode("Bad Romance")
party_rock_anthem = SongNode("Party Rock Anthem", bad_romance)
uptown_funk = SongNode("Uptown Funk", party_rock_anthem)

top_hits_2010s = uptown_funk

print_linked_list(top_hits_2010s)
"""

# problem 2
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

#make an empty hashmap/dictionary
#search the linked list and get artist
#add artist to dictionary
#if condition to add to freq count if artist appears more than once
#return the dictionary 

'''def get_artist_frequency(playlist):
    frequency = {}
    current = playlist
    while current:
        artist = current.artist
        frequency[artist] = frequency.get(artist, 0) + 1
        current = current.next
    return frequency

playlist = SongNode("Saturn", "SZA", SongNode("Who", "Jimin", SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))'''

#debugging problem
#if linked list is empty --
#

def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

#Problem 3
'''playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))'''

#check if linked list is empty
#check if there are the right amount of nodes -- (2 min)

#time complexity: O(n)
#space complexity: O(1)
'''
#problem 4
def on_repeat(playlist_head):
    if not playlist_head:
        return False
    if playlist_head.next is None:
        return False
    slow = playlist_head
    fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
	
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))
'''

#if ll dne
#if its a ll with no cycle

#Problem 5
def loop_length(playlist_head):
	if not playlist_head and not playlist_head.next:
        return 0


song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))