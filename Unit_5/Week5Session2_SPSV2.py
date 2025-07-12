"""
Problem 1: Calculate Tournament Placement
In the Player class below, each player has a race_outcomes attribute which holds a list of integers describing 
what place they came in for each race in a tournament.
Write a method get_tournament_place() that takes in one parameter, opponents, a list of other player objects also participating in the tournament, 
and returns the place in the overall tournament.
Rank in the tournament is determined by the lowest average race outcome. (1st place is better than 2nd!)
Each opponent in opponents is guaranteed to have participated in the same number of races as the current player.
"""
class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        if not opponents:
            return None
        total = sum(self.race_outcomes)
        count = len(self.race_outcomes)
        avg = total/count

        rank = 1
        for opponent in opponents:
            opponent_avg = sum(opponent.race_outcomes) / len(opponent.race_outcomes)
            if opponent_avg < avg:
                rank += 1
        return rank

print("--------Problem 1---------")
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(player1.get_tournament_place(opponents))

"""
Problem 2: Update Linked List Sequence
A linked list is a data structure that allows us to store pieces of data sequentially, similar to a normal list or array. 
The key difference between a linked list and a normal list is how each element is stored in a computer’s memory.
In a normal list, individual elements are stored in adjacent memory locations according to their order in the list. 
If we know where the first element is stored, it's easy to access any other element in the list.
In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Each node may be stored in an 
unrelated memory location. To connect nodes into a sequential list, each node stores a reference or pointer to the next node in the list.
Using the provided Node class and the linked list below, update the current linked list shy_guy -> diddy_kong -> dry_bones to 
shy_guy -> link -> diddy_kong -> toad -> dry_bones.
A function print_linked_list() that accepts the head, or first element, of a linked list and prints the values of the list has also 
been provided for testing purposes.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

print("--------Problem 2---------")
shy_guy = Node("Shy Guy")
link = Node("Link")
diddy_kong = Node("Diddy Kong")
toad = Node("Toad")
dry_bones = Node("Dry Bones")
shy_guy.next = link
link.next = diddy_kong
diddy_kong.next = toad
toad.next = dry_bones

print("Current List:")
print_linked_list(shy_guy)

"""
Problem 3: Insert Node as Second Element
Write a function add_second() that takes in the head of a linked list and a value val as parameters. It should insert val as the second node 
in the linked list and return the head of the linked list. (You can assume head is not None.)
Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.
"""
def add_second(head, val):
    new_node = Node(val,head.next)
    head.next = new_node
    return head

print("--------Problem 3---------")
original_list_head = Node("banana")
second = Node("blue shell")
third = Node("bullet bill")
original_list_head.next = second
second.next = third

# Linked list: "banana" -> "blue shell" -> "bullet bill"
new_list = add_second(original_list_head, "red shell")
print_linked_list(new_list)

"""
Problem 4: Increment Linked List Node Values
Write a function increment_ll() that takes in the head of a linked list of integer values and returns the same list, 
but with each node's value incremented by 1. Return the head of the list.
"""
def increment_ll(head):
    if not head:
        return None
    current = head
    while current:
        current.value += 1
        current = current.next
    return head

print("--------Problem 4---------")
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(increment_ll(node_one))

"""
Problem 5: Copy Linked List
Write a function copy_ll() that takes in the head of a linked list and creates a complete copy of that linked list.
The function should return the head of a new linked list which is identical to the given list in terms of its structure and contents, 
but does not use any of the node objects from the original list.
"""
def copy_ll(head):
    if not head:
        return None
    new_head = Node(head.value)
    new_current = new_head
    old_current = head.next
    while old_current:
        new_node = Node(old_current.value)
        new_current.next = new_node
        new_current = new_current.next
        old_current = old_current.next
    return new_head

print("--------Problem 5---------")
mario = Node("Mario")
daisy = Node("Daisy")
luigi = Node("Luigi")
mario.next = daisy
daisy.next = luigi

# Linked List: Mario -> Daisy -> Luigi
copy = copy_ll(mario)

# Change original list -- should not affect the copy
mario.value = "Original Mario"

print_linked_list(mario)
print_linked_list(copy)

"""
Problem 6: Making the Cut
Imagine that a linked list is used to track the order players finished in a race. Write a function top_n_finishers() 
that takes in the head of a linked list and a non-negative integer n as parameters.
The function should return a list of the values of the first n nodes.
If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
"""
def top_n_finishers(head, n):
    if not head:
        return None
    result = []
    count = 0
    current = head
    while current and count < n:
        result.append(current.value)
        current = current.next
        count += 1
    return result

print("--------Problem 6---------")
head = Node("Daisy", Node("Mario", Node("Toad", Node("Yoshi"))))

# Linked List: Daisy -> Mario -> Toad -> Yoshi
print(top_n_finishers(head, 3))

# Linked List: Daisy -> Mario -> Toad -> Yoshi
print(top_n_finishers(head, 5))

# Linked List: Daisy -> Mario -> Toad -> Yoshi
print(top_n_finishers(head, 1))

"""
Problem 7: Remove Racer
Write a function remove_racer() that takes in the head of a linked list and a value racer as parameters.
The function should remove the first node with the value racer from the linked list and return the head of the modified list. 
If racer is not in the list, return the head of the original list.
"""
def remove_racer(head, racer):
    if not head:
        return None
    if head.value == racer:
        return head.next
    current = head
    while current.next and current.next.value != racer:
        current = current.next
    if current.next:
        current.next = current.next.next
    return head

print("--------Problem 7---------")
head = Node("Daisy", Node("Mario", Node("Toad", Node("Mario"))))

# Linked List: Daisy -> Mario -> Toad -> Mario
print_linked_list(remove_racer(head, "Mario"))

# Linked List: Daisy -> Mario -> Toad
print_linked_list(remove_racer(head, "Yoshi"))

"""
Problem 8: Array to Linked List
Write a function arr_to_ll() that accepts an array of Player instances arr and converts arr into a linked list. 
The function should return the head of the linked list. If arr is empty, return None.
A function print_linked_list() which accepts the head, or first element, of a linked list and prints the character attribute of 
each Player in the linked list has also been provided for testing purposes.
"""
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list1(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for player in arr[1:]:
        current.next = Node(player)
        current = current.next
    return head

print("--------Problem 8---------")
mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list1(arr_to_ll([mario, luigi, peach]))
print_linked_list1(arr_to_ll([peach]))

"""
Problem 9: Convert Singly Linked List to Doubly Linked List
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. 
(E.g., A -> B -> C)
A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute 
that points to the Node before it. (E.g., A <-> B <-> C)
Update the code below to convert the singly linked list to a doubly linked list.
Two functions, print_linked_list() and print_linked_list_backwards(), have been provided for testing purposes. 
print_linked_list() accepts the head of a linked list and prints the values of each node in the list, 
starting at the head and iterating in a forward direction. print_linked_list_backwards() accepts the tail of a linked list 
and prints the values of each node in the list, starting at the tail and iterating in a backward direction.
"""
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

koopa_troopa = Node("Koopa Troopa")
toadette = Node("Toadette")
waluigi = Node("Waluigi")
koopa_troopa.next = toadette
toadette.next = waluigi

# Add code to convert to doubly linked list here --> manual way of converting nodes to doubly linked list
# waluigi.prev = toadette
# toadette.prev = koopa_troopa

# method to convert singly linked list to doubly linked list
def single_to_double(head):
    prev_node = None
    current = head
    while current:
        current.prev = prev_node
        prev_node = current
        current = current.next
    return prev_node

def print_linked_list_backwards(tail):
    current = tail
    while current:
        print(current.value, end=" -> " if current.prev else "\n")
        current = current.prev

print("--------Problem 9---------")
tail = single_to_double(koopa_troopa)
print_linked_list(koopa_troopa)
print_linked_list_backwards(tail)

"""
Problem 10: Find Length of Doubly Linked List from Any Node
Write a function get_length() that takes in a node at an unknown position within a doubly linked list. 
The function should return the length of the entire list.
"""
def get_length(node):
    if node is None:
        return 0
    start = node
    while start.prev:
        start = start.prev
    length = 0
    current = start
    while current:
        length += 1
        current = current.next
    return length

print("--------Problem 10---------")
yoshi_falls = Node("Yoshi Falls")
moo_moo_farm = Node("Moo Moo Farm")
rainbow_road = Node("Rainbow Road")
dk_mountain = Node("DK Mountain")
yoshi_falls.next = moo_moo_farm
moo_moo_farm.next = rainbow_road
rainbow_road.next = dk_mountain
dk_mountain.prev = rainbow_road
rainbow_road.prev = moo_moo_farm
moo_moo_farm.prev = yoshi_falls

# List: Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain
print(get_length(rainbow_road))