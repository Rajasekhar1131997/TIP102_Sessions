"""
Understand : We need to check the list and see if there are any common friends, if we have a match we need to add them to list and return them
Match: Single Linked List
Input: an instance of class
Output: List
Plan:
1. We create an empty list
2. We loop through the list of friends we have
3. if the friend in our list:
4. we append that friend to our list
5. we send that list as output
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

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

new = Node("kk_slider",Node("harriet", Node("saharah", Node("isabelle"))))

print_linked_list(new)

def add_first(head, task):
    temp = Node(task)
    temp.next = head
    return temp
# return Node(task,head)
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))

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

def halve_list(head):
    current = head
    while current:
        half = current.value / 2
        current.value = int(half) if half.is_integer() else half
        current = current.next
    return head

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# 1->2->3->4
def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current=head
    prev=head
    while current.next:
        prev = current
        current = current.next

    prev.next=None
    return head

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_min(head):
    if head is None:
        return None
    if head.next is None:
        return head
    min_value = head.value
    