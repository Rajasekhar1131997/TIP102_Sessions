"""
Problem 1: New Horizons
Step 1: Copy the following code into your IDE.
Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. 
Store the instance in a variable named apollo.
The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
"""
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) == 0:
            print("Invalid Catchphrase")
        if len(new_catchphrase) < 20 and all(char.isalpha() or char.isspace() for char in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
        else:
            print("Invalid Catchphrase")
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def add_item(self, item_name):
        items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in items:
            self.furniture.append(item_name)

    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory empty")
        else:
            frequency = {}
            for i in self.furniture:
                frequency[i] = frequency.get(i, 0) + 1
            frequency_output = str(frequency).replace('{','').replace('}','')
            print(frequency_output)
    @staticmethod
    def message_received(start_villager, target_villager):
        visited = set()
        current = start_villager
        while current != None:
            if current == target_villager:
                return True
            if current in visited:
                break
            visited.add(current)
            current = current.neighbor
        return False

def of_personality_type(townies, personality_type):
    result = []
    for villager in townies:
        if villager.personality == personality_type:
            result.append(villager.name)
    return result


print("--------Problem 1---------")
apollo = Villager("Apollo","Eagle"," ", "pah")
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

"""
Problem 2: Greet Player
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:
Step 2: Create a second instance of Villager in a variable named bones.
The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". 
For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.
"""
bones = Villager("Bones","Dog"," ","yip yip")

print("--------Problem 2---------")
print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture)

message = bones.greet_player("Rajasekhar Reddy Kolagotla")
print(message)

"""
Problem 3: Update Catchphrase
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.
Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".
Example Usage:
"""
bones.catchphrase = "ruff it up"

print("--------Problem 3---------")
print(bones.greet_player("Samia"))

"""
Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s catchphrase attribute directly. 
Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. 
This has a few different benefits, including allowing us to validate data before updating our class instance.
Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.
If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
Otherwise, it should print out "Invalid catchphrase".
Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.
"""
alice = Villager("Alice", "Koala", " ", "guvnor")

print("--------Problem 4---------")
alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

"""
Problem 5: Add Furniture
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.
Update the Villager class with a new method add_item() that takes in one parameter, item_name.
The method should validate the item_name.
If the item is valid, add item_name to the player’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", 
"kotatsu", or "cacao tree".
"""

print("--------Problem 5---------")
alice = Villager("Alice", "Koala"," ", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

"""
Problem 6: Print Inventory
Update the Villager class with a method print_inventory() that accepts no parameters except for self.
The method should print the name and quantity of each item in a villager’s furniture list.
The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique items 
exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
"""

print("--------Problem 6---------")
alice = Villager("Alice", "Koala"," ", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()

"""
Problem 7: Group by Personality
The Villager class has been updated below to include the new string attribute personality representing the character's personality type.
Outside of the Villager class, write a function of_personality_type(). Given a list of Villager instances townies 
and a string personality_type as parameters, return a list containing the names of all villagers in townies with personality personality_type. 
Return the names in any order.
"""

print("--------Problem 7---------")
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

"""
Problem 8: Telephone
The Villager constructor has been updated to include an additional attribute neighbor. A villager's neighbor is another Villager instance 
and represents their closest neighbor. By default, a Villager's neighbor is set to None.
Given two Villager instances start_villager and target_villager, write a function message_received() that returns True 
if you can pass a message from the start_villager to the target_villager through a series of neighbors and False otherwise.
"""

print("--------Problem 8---------")
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(Villager.message_received(isabelle, kk_slider))
print(Villager.message_received(kk_slider, isabelle))

"""
Problem 9: Nook's Cranny
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. 
The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.
In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. 
If we know where the first element of the list is stored, it’s really easy to find any other element in the list.
In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored 
in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the 
next node in the list.
Using the provided Node class below, create a linked list Tom Nook -> Tommy where the instance tom_nook has value "Tom Nook" 
which points to the instance tommy that has value "Tommy".
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

print("--------Problem 9---------")
tom_nook = Node("Tom Nook")
timmy = Node("Timmy")
tommy = Node("Tommy")
tom_nook.next = timmy
timmy.next = tommy
print(tom_nook.value) #Tom Nook
print(tom_nook.next.value) #Tommy
print(tommy.value) #Tommy
print(tommy.next) #None

"""
Problem 10: Timmy and Tommy
In a linked list, pointers can be redirected to any place in the list.
Using the linked list from Problem 9, create a new Node timmy with value "Timmy" and place it between tom_nook and tommy 
so the new linked list is tom_nook -> timmy -> tommy.
"""

print("--------Problem 10---------")
print(tom_nook.value) #Tom Nook
print(tom_nook.next.value) #Timmy
print(timmy.value) #Timmy
print(timmy.next.value) #Tommy
print(tommy.value) #Tommy
print(tommy.next) #None

"""
Problem 11: Saharah
Using the linked list from Problem 10, remove the tom_nook node and add in a node saharah with value "Saharah" to the end of the list 
so that the resulting list is timmy -> tommy -> saharah.
previously it was tom_nook -> timmy -> tommy
"""
head = tom_nook.next
tom_nook.next = None

saharah = Node("Saharah")
current = head
while current.next:
    current = current.next

current.next = saharah

print("--------Problem 11---------")
print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next)

"""
Problem 12: Print List
Write a function print_list() that takes in the head of a linked list and returns a string linking together the values of the list 
with the separator "->".
Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.
Example Usage:
"""
def print_list(head):
    values = []
    current = head
    while current != None:
        values.append(current.value)
        current = current.next
    return " -> ".join(values)

print("--------Problem 12---------")
isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))