class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
def palindrome(head):
    if head is None:
        return True
    if head.next is None:
        return True
    current = head
    result = []
    while current:
        result.append(current.value)
        current = current.next
    print(result)
    return ispalindrome(result)
def ispalindrome(list):
    if len(list) < 2:
        return True
    left , right = 0, len(list) - 1
    while left < right:
        if list[left] == list[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

head1 = Node(1,Node(2,Node(3,Node(2, Node(1)))))
head2 = Node(1,Node(2))
head3 = Node(1)
print(palindrome(head1))
print(palindrome(head2))
print(palindrome(head3))