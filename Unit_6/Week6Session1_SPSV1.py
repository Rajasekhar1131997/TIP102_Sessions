"""
Problem 1: Building a Playlist
The assignment statement to the top_hits_2010s variable below creates the linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. 
Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.
"""
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
	
print("--------Problem 1---------")
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))
bad_romance = SongNode("Bad Romance")
party_rock_anthem = SongNode("Party Rock Anthem", bad_romance)
uptown_funk = SongNode("Uptown Funk", party_rock_anthem)
top_hits_2010s = uptown_funk
print_linked_list(top_hits_2010s)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 2: Top Artists
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.
"""
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


def get_artist_frequency(playlist):
	if not playlist:
		return {}
	frequency = {}
	current = playlist
	while current:
		artist = current.artist
		frequency[artist] = frequency.get(artist, 0) + 1
		current = current.next
	return frequency

print("--------Problem 2---------")
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 3: Glitching Out
The following code attempts to remove the first node with a given song from a singly linked list with head playlist_head but it 
contains a bug!
Step 1: Copy this code into Replit.
Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and 
fix the bug so that the function correctly removes a node by value from the list.
Step 3: Evaluate the time and space complexity of the fixed solution. Define your variables and provide a rationale for 
why you believe the solution has the stated time and space complexity.
"""
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

print("--------Problem 3---------")
playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 4: On Repeat
A variation of the two-pointer technique introduced in previous units is to have a slow and a fast pointer that increment at different rates.
We would like to check whether our playlist loops or not. Given the head of a linked list playlist_head, return True 
if the playlist has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, 
the node’s next pointer points back to a previous node in the list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
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

print("--------Problem 4---------")
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 5: Looped
Given the head of a linked list playlist_head that may contain a cycle, use the fast and slow pointer method to 
return the length of the cycle. If the list does not contain a cycle, return 0.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def loop_length(playlist_head):
      if not playlist_head:
            return 0
      if playlist_head.next is None:
            return 0
      slow = playlist_head
      fast = playlist_head
      count = 0
      while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
            
            

print("--------Problem 5---------")
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))
print("Time Complexity: ")
print("Space Complexity: ")