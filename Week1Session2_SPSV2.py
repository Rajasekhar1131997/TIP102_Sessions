# Problem 1: String Array Equivalency
# Given two string arrays word1 and word2, return True if the two arrays represent the same string, and False otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
def are_equivalent(word1, word2):
    string1 = ''.join(word1)
    string2 = ''.join(word2)

    return string1 == string2

word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2))

# Problem 2: Count Even Strings
# Implement a function count_evens() that accepts a list of strings lst as a parameter. 
# The function should return the number of strings with an even length in the list.
def count_evens(lst):
    count = 0
    for word in lst:
        if len(word) % 2 == 0:
            count += 1
    return count

lst = ["na", "nana", "nanana", "batman", "!"]
print(count_evens(lst))

lst = ["the", "joker", "robin"]
print(count_evens(lst))

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
print(count_evens(lst))

# Problem 3: Secret Identity
# Write a function remove_name() to keep Batman's secret identity hidden. 
# The function accepts a list of names people and a string secret_identity and should return the 
# list with any instances of secret_identity removed. The list must be modified in place; you may 
# not create any new lists as part of your solution. Relative order of the remaining elements must be maintained.
def remove_name(people, secret_identity):
    i = 0
    while i < len(people):
        if secret_identity == people[i]:
            del people[i]
        else:
            i+=1
    return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))

# Problem 4: Count Digits
# Given a non-negative integer n, write a function count_digits() that returns the number of digits in n. You may not cast n to a string.
def count_digits(n):
    count = 0
    if n == 0:
        return 1
    while(n>0):
        n = n//10
        count +=1
    return count

n = 964
print(count_digits(n))

n = 0
print(count_digits(n))

# Problem 5: Move Zeroes
# Write a function move_zeroes that accepts an integer array nums and returns a new list with all 0s moved 
# to the end of list. The relative order of the non-zero elements in the original list should be maintained.
def move_zeroes(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] != 0:
            new_list.append(lst[i])
    zeros = len(lst) - len(new_list)
    new_list.extend([0] * zeros)
    return new_list
    

lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))

# Problem 6: Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases and more than once.
def reverse_vowels(s):
    vowels = list("aeiouAEIOU")
    s = list(s)
    left = 0 
    right = len(s) - 1
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))

# Problem 7: Vantage Point
# Batman is going on a scouting trip, surveying an area where he thinks Harley Quinn might commit her next crime spree. 
# The area has many hills with different heights and Batman wants to find the tallest one to get the best vantage point. 
# His scout trip consists of n + 1 points at different altitudes. Batman starts his trip at point 0 with altitude 0.
# Write a function highest_altitude() that accepts an integer array gain of length n where gain[i] is the 
# net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
def highest_altitude(gain):
    altitudes = [0]
    for i in range(len(gain)):
        new_altitude = altitudes[-1] + gain[i]
        altitudes.append(new_altitude)
    return max(altitudes)

gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))

gain = [-4, -3, -2, -1, 4, 3, 2]
print(highest_altitude(gain))

# Problem 8: Left and Right Sum Differences
# Given a 0-indexed integer array nums, write a function left_right_difference that returns a 0-indexed integer array answer where:
# len(answer) == len(nums)
# answer[i] = left_sum[i] - right_sum[i]
# Where:
# left_sum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, left_sum[i] = 0
# right_sum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, right_sum[i] = 0
def left_right_difference(nums):
    n = len(nums)
    answer = [0] * n
    left_sum = [0] * n
    right_sum = [0] * n
    for i in range(1,n):
        left_sum[i] = left_sum[i-1] + nums[i-1]
    for i in range(n-2,-1,-1):
        right_sum[i] = right_sum[i+1] + nums[i+1]
    for i in range(n):
        answer[i] = left_sum[i] - right_sum[i]
    return answer

nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))

# Problem 9: Common Cause
# Write a function common_elements() that takes in two lists lst1 and lst2 and returns a list of the elements that are common to both lists.
def common_elements(lst1, lst2):
    list1 = [x for x in lst1 if x in lst2]
    return list1


lst1 = ["super strength", "super speed", "x-ray vision"] 
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

lst1 = ["super strength", "super speed", "x-ray vision"] 
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))

"""
Problem 10: Exposing Superman
Metropolis has a population n, with each citizen assigned an integer id from 1 to n. 
There's a rumor that Superman is an ordinary citizen among this group.
If Superman is an ordinary citizen, then:
Superman trusts nobody.
Everybody (except for Superman) trusts Superman.
There is exactly one citizen that satisfies properties 1 and 2.
Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] representing that 
the person labeled ai trusts the person labeled bi. 
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.
"""
def expose_superman(trust, n):
    score = [0] * (n + 1)
    print(score)
    for a, b in trust:
        score[a] -= 1
        score[b] += 1

    for i in range(1, n + 1):
        if score[i] == n - 1:
            return i

    return -1

n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))