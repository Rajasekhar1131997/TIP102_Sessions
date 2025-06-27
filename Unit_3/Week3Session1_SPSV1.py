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

print("--------Problem 1---------")
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

print("--------Problem 2---------")
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
def is_symmetrical_title(title):
    title = title.lower()
    title = title.replace(" ","")
    left = 0
    right = len(title) - 1
    while left < right:
        if title[left] != title[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
    
print("--------Problem 3---------")
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

"""
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.
Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Your Task:
Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.
"""
def engagement_boost(engagements):
    squared_engagements = [] # intializing an empty list
    
    for i in range(len(engagements)): # looping through each value from engagements list
        squared_engagement = engagements[i] * engagements[i] #calulating the square of each value
        squared_engagements.append((squared_engagement, i)) # appending the squared value into squared_engagements list
    
    squared_engagements.sort(reverse=True) # with the help of sort() function, sorting the list in descending order
    
    result = [0] * len(engagements) #creating an empty list of 0's the same length of engagements list
    position = len(engagements) - 1 #initializing a pointer at the end of enagagements list
    
    for square, original_index in squared_engagements: #looping through each value and index from squared_engagements list
        result[position] = square #assigning the squared value to the result list
        position -= 1 # moving the position to the left
    
    return result #returning the result list

print("--------Problem 4---------")
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

"""
Problem 4: Engagement Boost (Two-pointer)
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.
Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Your Task:
Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.
"""
def engagement_boost(engagements):
    result = [0] * len(engagements)
    left = 0
    right = len(engagements) - 1
    index = len(engagements) - 1
    
    while left <= right:
        left_square = engagements[left] * engagements[left]
        right_square = engagements[right] * engagements[right]
        
        if left_square < right_square:
            result[index] = right_square
            right -= 1
        else:
            result[index] = left_square
            left += 1
            
        index -= 1
    return result

print("--------Problem 4 (Two Pointer Approach)---------")
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

"""
Problem 5: Content Cleaner
You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, 
you want to remove any pairs of adjacent characters where one is the lowercase version of a letter and the 
other is the uppercase version of the same letter. Keep removing such pairs until the post is clean.
A clean post does not have two adjacent characters post[i] and post[i + 1] where:
post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.
Note that an empty string is also considered clean.
"""
def clean_post(post):
    stack = []
    if not post:
        return ""
    if len(post) == 1:
        return post
    for char in post:
        if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)    

print("--------Problem 5---------")
print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

"""
Problem 6: Post Editor
You want to add a creative twist to your posts by reversing the order of characters in each word within your post while still 
preserving whitespace and the initial word order. Given a string post, use a queue to reverse the order of characters in 
each word within the sentence.
"""
from collections import deque
def edit_post(post):
    result = []
    q = deque()
    for char in post:
        if char != " ":
            q.append(char)
        else:
            while q:
                result.append(q.pop())
            result.append(char)
    while q:
        result.append(q.pop())
    return "".join(result)

print("--------Problem 6---------")
print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog"))

"""
Problem 7: Post Compare
You often draft your posts and edit them before publishing. Given two draft strings draft1 and draft2, 
return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will remain empty.
"""
def post_compare(draft1, draft2):
    return helper(draft1) == helper(draft2)

def helper(draft1):
    stack = []
    for char in draft1:
        if char == "#":
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

print("--------Problem 7---------")
print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b"))