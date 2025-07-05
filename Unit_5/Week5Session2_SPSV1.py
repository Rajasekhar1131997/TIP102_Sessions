"""
Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.
Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, and returns a list 
with the name of all friends the current villager and new_contact have in common.
"""
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        result = []
        for friend in self.friends:
            if friend in new_contact.friends:
                result.append(friend.name)
        return result

print("--------Problem 1---------")
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))

"""
Problem 2: Linked Up
A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. 
The key difference is how the elements are stored in memory.
In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, 
we can easily access any other element in the list.
In a linked list, individual elements, called nodes, are not stored in sequential memory locations. 
Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.
Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.
A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list 
has also been provided for testing purposes.
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
    
def add_first(head, task):
    return Node(task, head)

def halve_list(head):
    current = head
    while current:
        half = current.value / 2
        current.value = int(half) if half.is_integer() else half
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next != None:
        current = current.next

    current.next = None
    return head

def find_min(head):
    if head is None:
        return None
    if head.next is None:
        return None
    min_value = head.value
    current = head.next
    while current:
        if current.value < min_value:
            min_value = current.value
        current = current.next
    return min_value

def delete_item(head, item):
    if head is None:
        return None
    if head.next is None:
        return None
    if head.value == item:
        return head.next
    prev = head
    current = head.next
    while current:
        if current.value == item:
            prev.next = current.next
            return head
        prev = current
        current = current.next
    return head

def tail_to_head(head):
    if head is None:
        return head
    if head.next is None:
        return head
    prev = None
    current = head
    while current.next:
        prev = current
        current = current.next
    prev.next = None
    current.next = head
    return current

print("--------Problem 2---------")
kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")
# Add code here to link the above nodes
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
print_linked_list(kk_slider)

"""
Problem 3: Daily Tasks
Imagine a linked list used as a daily task list where each node represents a task. Write a function add_task() that takes 
in the head of a linked list and adds a new node to the front of the task list.
The function should insert a new Node object with the value task as the new head of the linked list and return the new node.
Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.
"""
print("--------Problem 3---------")
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))

"""
Problem 4: Halve List
Write a function halve_list() that accepts the head of a linked list whose values are integers and divides each value by two. 
Return the head of the modified list.
"""
print("--------Problem 4---------")
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))

"""
Problem 5: Remove Last
Write a function delete_tail() that accepts the head of a linked list and removes the last node in the list. Return the head of the modified list.
Note: The "tail" of a list is the last element in the linked list. It is equivalent to lst[-1] in a normal list.
"""
print("--------Problem 5---------")
butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))

"""
Problem 6: Find Minimum in Linked List
Write a function find_min() that takes in the head of a linked list and returns the minimum value in the linked list. 
You can assume the linked list will contain only numeric values.
"""
print("--------Problem 6---------")
head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))

"""
Problem 7: Remove From Inventory
Imagine a linked list used to store a player's inventory. Write a function delete_item() that takes in the head of a linked list 
and a value item as parameters.
The function should remove the first node it finds in the linked list with the value item and return the head of the modified list. 
If no node can be found with the value item, return the list unchanged.
"""
print("--------Problem 7---------")
slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))

"""
Problem 8: Move Tail to Front of Linked List
Write a function tail_to_head() that takes in the head of a linked list as a parameter and moves the tail of the linked list to the front.
"""
print("--------Problem 8---------")
daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad") 
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

# Linked List: Daisy -> Mario -> Toad -> Peach
print_linked_list(tail_to_head(daisy))

"""
Problem 9: Create Double Links
One of the drawbacks of a linked list is that it's difficult to go backwards because each Node only knows about the Node in front of it. 
(E.g., A -> B -> C)
A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that 
points to the Node before it. (E.g., A <-> B <-> C)
Update the Node constructor below so that the code creates a doubly linked list with head <-> tail.
"""
