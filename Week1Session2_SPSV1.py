# Problem 1: Reverse Sentence
# Write a function reverse_sentence() that takes in a string sentence and returns the sentence 
# with the order of the words reversed. The sentence will contain only alphabetic characters and 
# spaces to separate the words. If there is only one word in the sentence, the function should return the original string.
def reverse_sentence(sentence):
    words = sentence.split(' ')
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))

# Problem 2: Goldilocks Number
# In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. 
# She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. 
# Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns 
# any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
# Return the selected integer.
def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    minimum = min(nums)
    maximum = max(nums)
    for i in nums:
        if i != minimum and i != maximum:
            return i
    return -1
    
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))

# Problem 3: Delete Minimum
# Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, 
# write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. 
# Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
def delete_minimum_elements(hunny_jar_sizes):
    new_list = []
    while(len(hunny_jar_sizes) > 0):
        min_val = min(hunny_jar_sizes)
        new_list.append(min_val)
        hunny_jar_sizes.remove(min_val)
    return new_list

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

# Problem 4: Sum of Digits
# Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.
def sum_of_digits(num):
    sum = 0
    while(num>0):
        rem = num % 10
        sum += rem
        num = num // 10
    return sum

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))

# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations 
# containing a list of operations, return the final value of tigger after performing all the operations.
def final_value_after_operations(operations):
    tigger = 1
    for i in operations:
        if i in ["bouncy", "flouncy"]:
            tigger += 1
        elif i in ["trouncy", "pouncy"]:
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# Problem 6: Acronym
# Given an array of strings words and a string s, implement a function is_acronym() that 
# returns True if s is an acronym of words and returns False otherwise.
# The string s is considered an acronym of words if it can be formed by concatenating the 
# first character of each string in words in order. For example, "pb" can be formed from ["pooh"", "bear"], 
# but it can't be formed from ["bear", "pooh"].
def is_acronym(words, s):
    acronym = ""
    for word in words:
        if word:
            acronym = acronym + word[0]
    return acronym == s

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

# Problem 7: Good Things Come in Threes
# Write a function make_divisible_by_3() that accepts an integer array nums. 
# In one operation, you can add or subtract 1 from any element of nums. 
# Return the minimum number of operations to make all elements of nums divisible by 3.
def make_divisible_by_3(nums):
    ops = 0
    for num in nums:
        if num % 3 != 0:
            ops += 1
    return ops

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))

# Problem 8: Exclusive Elements
# Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list that 
# contains the elements which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.
def exclusive_elemts(lst1, lst2):
    first_intersection = [x for x in lst1 if x not in lst2]
    second_intersection = [x for x in lst2 if x not in lst1]
    return first_intersection + second_intersection

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))

# Problem 9: Merge Strings Alternately
# Write a function merge_alternately() that accepts two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
def merge_alternately(word1, word2):
    new_list = []
    length = max(len(word1), len(word2))
    for i in range(length):
        if i < len(word1):
            new_list.append(word1[i])
        if i < len(word2):
            new_list.append(word2[i])
    return ''.join(new_list)

word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))

# Problem 10: Eeyore's House
# Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks 
# whose lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays 
# pile1 and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. 
# The function should return the number of good pairs.
# A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1
def good_pairs(pile1, pile2, k):
    p1 = len(pile1)
    p2 = len(pile2)
    count = 0
    for i in range(p1):
        for j in range(p2):
            if (pile1[i] % (pile2[j] * k) == 0):
                count +=1
    return count

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))