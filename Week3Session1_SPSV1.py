# You are managing a social media platform and need to ensure that posts are properly formatted. Each 
# post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
# You are given a string representing a post's content, and your task is to determine if the tags in the post are
#  correctly formatted.

# A post is considered valid if:

# Every opening tag has a corresponding closing tag of the same type.
# Tags are closed in the correct order.
#psuedo code:
# 1. Initializing a stack to keep track of the opening brackets
# 2. loop through the string
# 3. if it finds an opening tag, it should that value or tag into the empty stack
# 4. if it finds an closing tag, it should check whether the stack is empty or not and we also need to make sure
# its of the same type
# 5. if it is of same tag, it should then pop from the stack
# 6. if not, the tags are not properly closed and should return false
# 7. once, we loop through all the characters in the string, and also we need make sure that the stack is empty
# then we return true, otherwise false.

def is_valid_post_format(posts):
    dictionary = { ')' : '(',
                  '}':'{',
                  ']' : '['}
    stack = []
    for ch in posts:
        if ch in dictionary.values():
            stack.append(ch)
        elif ch in dictionary.keys():
            if not stack or stack[-1] != dictionary[ch]:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

# Problem 2: Reverse User Comments Queue
# On your platform, comments on posts are displayed in the order they are received. 
# However, for a special feature, you need to reverse the order of comments before displaying them. 
# Given a queue of comments represented as a list of strings, reverse the order using a stack.
# UMPIRE
# Understand
# Input: list of string
# Output: reversed list of strin 
# Constraint: have to use the stack because the problem said so
# edge case: empty string or empty list

# Plan
# intalize stack 
# intalie a list 
# iterate the comments
# push each comment onto stack
# we iterate the stack until its empty
# pop each character
# add character to a new list
# return the list
 
def reverse_comments_queue(comments):
    stack = [] 
    res = [] 
    for word in comments: 
        stack.append(word)
    # till empty
    while(stack):
        res.append(stack.pop())
    return res

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# Problem 3: Check Symmetry in Post Titles
# As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, 
# meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. 
# Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.
# UMPIRE
# Understand
# Input: String
# Output: Boolean Value
# Constraint: Two pointer method
# edge case: Empty String or bunch of spaces
# Plan
# initialize left and right pointers
# 
def is_symmetrical_title(title):
  pass