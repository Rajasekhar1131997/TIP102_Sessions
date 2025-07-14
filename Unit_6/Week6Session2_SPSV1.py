"""
Problem 1: Wild Goose Chase
You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy - you suspect 
the clue might be a red herring meant to send you around in circles. Write a function is_circular() that accepts the 
head of a singly linked list clues and returns True if the tail of the linked list points at the head of the linked list. 
Otherwise, return False.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    if not clues:
        return False
    current = clues
    while current.next:
        if current.next == clues:
            return True
        current = current.next
    return False


print("--------Problem 1---------")
clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 2: Breaking the Cycle
All the clues that lead us in circles are false evidence we need to purge! Given the head of a linked list evidence, 
clean up the evidence list by identifying any false clues. Write a function collect_false_evidence() that returns 
an array containing all values that are part of any cycle in evidence. Return the values in any order.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def collect_false_evidence(evidence):
    result = []
    if not evidence:
        return result
    slow = evidence
    fast = evidence
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return result
    slow = evidence
    while slow != fast:
        slow = slow.next
        fast = fast.next

    cycle_start = slow
    current = cycle_start
    while True:
        result.append(current.value)
        current = current.next
        if current == cycle_start:
            break
    return result

print("--------Problem 2---------")
clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))
print("Time Complexity: O(n)")
print("Space Complexity: O(k), where k is the length of the cycle, to store the nodes in the cycle to the list")

"""
Problem 3: Prioritizing Suspects
You've identified a list of suspect, but time is limited and you won't be able to question all of them today. 
Write a function partition() to help prioritize the order in which you question suspects. Given the head of a linked list of integers 
suspect_ratings, where each integer represents the suspiciousness of the a given suspect and a value threshold, 
partition the linked list such that all nodes with values greater than threshold come before nodes with values less than or equal to threshold.
Return the head of the partitioned list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
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

def partition(suspect_ratings, threshold):
    if not suspect_ratings:
        return None
    greater_head = Node(0)
    less_or_equal_head = Node(0)
    greater = greater_head
    less_or_equal = less_or_equal_head
    current = suspect_ratings
    while current:
        if current.value > threshold:
            greater.next = current
            greater = greater.next
        else:
            less_or_equal.next = current
            less_or_equal = less_or_equal.next
        current = current.next
    greater.next = less_or_equal_head.next
    less_or_equal.next = None
    if greater_head.next:
        return greater_head.next
    else:
        return less_or_equal_head.next

print("--------Problem 3---------")
suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print_linked_list(partition(suspect_ratings, 3))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 4: Puzzling it Out
A new witness has emerged and provided a new account of events the night of the crime. Given the heads of two sorted linked lists, 
known_timeline and witness_timeline, each representing a numbered sequence of events, merge the two timelines into one sorted sequence 
of events. The resulting linked list should be made by splicing together the nodes of the first two timelines. 
Return the head of the merged timeline.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def merge_timelines(known_timeline, witness_timeline):
    temp_head = Node(0)
    current = temp_head

    p1 = known_timeline
    p2 = witness_timeline
    while p1 and p2:
        if p1.value <= p2.value:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    if p1:
        current.next = p1
    if p2:
        current.next = p2
    return temp_head.next

print("--------Problem 4---------")
known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))
print("Time Complexity: O(M+N)")
print("Space Complexity: O(1)")

"""
Problem 5: A New Perspective
You're having a tough time making a break in the case, and it's time to shake things up to gain a new perspective. 
Given the head of a linked list of numbered pieces of evidence evidence, and a non-negative integer k, rotate the list 
to the right by k places. Return the head of the rotated list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def rotate_right(head, k):


print("--------Problem 5---------")
evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))
print("Time Complexity: ")
print("Space Complexity: ")