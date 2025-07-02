"""
Problem 1: Player Class
Step 1: Copy the following code into your IDE.
Step 2: Instantiate an instance of the class Player and store it in a variable named player_one.
The Player object should have the character "Yoshi" and the kart "Super Blooper".
"""
class Player():
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
    
    def get_player(self):
        return f"{self.character} driving the {self.kart}"
    
    def set_character(self, name):
        if len(name) == 0:
            print("Invalid character")
        if len(name) > 1:
            names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
            if name in names:
                self.character = name
                print("Character updated")
            else:
                print("Invalid character")
        
    def add_item(self, item_name):
        items_list = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
        if item_name in items_list:
            self.items.append(item_name)

    def print_inventory(self):
        if len(self.items) == 0:
            print("Inventory empty")
        else:
            freq = {}
            for item in self.items:
                freq[item] = freq.get(item, 0) + 1
            print("Inventory: ", freq)
    
def print_results(race_results):
    for position, player in enumerate(race_results, start=1):
        print(f"{position}. {player.character}")

def get_rank(my_player):
    rank = 1
    current_player = my_player
    while current_player != None:
        if current_player.ahead is None:
            return rank
        current_player = current_player.ahead
        rank += 1


print("--------Problem 1---------")
player_one = Player("Yoshi", "Super Blooper")
print(player_one.character)
print(player_one.kart)
print(player_one.items)

"""
Problem 2: Get Player
Step 1: Using the Player class from Problem 1, add the following get_player() method to your existing code:
def get_player(self):
    return f"{self.character} driving the {self.kart}"
Step 2: Create a second instance of Player in a variable named player_two.
The Player object created should have character "Bowser" and kart "Pirahna Prowler".
Step 3: Use the method get_player() below to print out "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler".
Example Usage:
"""
print("--------Problem 2---------")
player_two = Player("Bowser", "Pirahna Prowler")
print(player_two.character)
print(player_two.kart)
print(player_two.items)

message = "Match: "+ player_one.get_player() + " vs " + player_two.get_player()
print(message)

"""
Problem 3: Update Kart
Players might want to update their choice of kart for their next race.
Update player_one so that their kart is "Dolphin Dasher" instead of its current value, "Super Blooper".
Example Usage:
"""
print("--------Problem 3---------")
player_one.kart = "Dolphin Dasher"
print(player_one.get_player())

"""
Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s kart attribute directly. Instead of allowing users to update 
their player directly, it is common to create setter methods that users can call to update class attributes. 
This has a few different benefits, including allowing us to validate data before updating our class instance.
Update your Player class with a method set_character() that takes in one parameter name.
If name is valid, it should update the player’s character attribute to have value name and print "Character updated".
Otherwise, it should print out "Invalid character".
Valid character names are "Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", and "Bowser".
"""
print("--------Problem 4---------")
player_three = Player("Donkey Kong", "Standard Kart")
player_three.set_character("Peach")
print(player_three.character)
player_three.set_character("Baby Peach")
print(player_three.character)

"""
Problem 5: Add Special Item
Players can pick up special items as they race.
Update the Player class with a new method add_item() that takes in one parameter, item_name.
The method should validate the item_name.
If the item is valid, add item_name to the player’s items attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: 
"banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".
"""
print("--------Problem 5---------")
player_one = Player("Yoshi", "Dolphin Dasher")

print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)

"""
Problem 6: Print Inventory
Update the Player class with a method print_inventory() that accepts no parameters except for self.
The method should print the name and quantity of each item in a player’s items list.
If the player has no items, the function should print "Inventory empty".
"""
print("--------Problem 6---------")
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

"""
Problem 7: Race Results
Given a list race_results of Player objects where the first player in the list came first in the race, 
second player in the list came second, etc., write a function print_results() that prints the players in place.
"""
print("--------Problem 7---------")
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]
print_results(race_one)

"""
Problem 8: Get Rank
The Player class has been updated below with a new attribute ahead to represent the player currently directly ahead of them in the race.
Write a function get_rank() that accepts a Player object my_player and returns their current place number in the race.
"""
print("--------Problem 8---------")
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

print(get_rank(luigi))
print(get_rank(peach))
print(get_rank(mario))

"""
Problem 9: Tom and Jerry
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. 
The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.
In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list.
 If we know where the first element of the list is stored, it’s really easy to find any other element in the list.
In a linked list, the individual elements called nodes are not stored in sequential memory locations. 
Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, 
each node stores a reference or pointer to the next node in the list.
Using the provided Node class below, create a linked list cat -> mouse where the instance cat has value "Tom" 
which points to the instance mouse that has value "Jerry".
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def chase_list(head):
    values = []
    current = head
    while current != None:
        values.append(current.value)
        current = current.next
    return " chases ".join(values)

    
print("--------Problem 9---------")
cat = Node("Tom")
mouse = Node("Jerry")
cat.next = mouse
print(cat.value) #Tom
print(cat.next) #memory location of that node will be printed instead of mouse
print(cat.next.value) #Jerry
print(mouse.value) #Jerry
print(mouse.next) #None

"""
Problem 10: Chase List
In a linked list, pointers can be redirected at any place in the list.
Using the linked list from Problem 9, create a new Node dog with value "Spike" and point it to the cat node so that the full list now 
looks like dog -> cat -> mouse.
Example Usage:
"""
print("--------Problem 10---------")
dog = Node("Spike")
dog.next = cat

print(dog.value) #Spike
print(dog.next) #cat
print(dog.next.value) #Tom
print(cat.next) #mouse
print(cat.next.value) #Jerry
print(mouse.next) #None

"""
Problem 11: Update Chase
Using the linked list from Problem 10, remove the dog node and add in a node cheese with value "Gouda" to the end of the list 
so that the resulting list is cat -> mouse -> cheese.
previously it was dog -> cat -> mouse
"""
print("--------Problem 11---------")
head = dog.next
dog.next = None
cheese = Node("Gouda")
current = head
while current.next:
    current = current.next

current.next = cheese

"""
Problem 12: Chase String
Write a function chase_list() that takes in the head of a linked list and returns a string linking together the values of the list 
with the separator "chases".
Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.
Example Usage:
"""
print("--------Problem 12---------")
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))