# Problem 1: Words Containing Character
# Write a function words_with_char() that accepts a list of strings words and a character x. 
# Return a list of indices representing the words that contain the character x. The returned list may be in any order.
def words_with_char(words, x):
    result = []
    for i in range(len(words)):
        if x in words[i]:
            result.append(i)
    return result

words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))

# Problem 2: HulkSmash
# Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:
# answer[i] == "HulkSmash" if i is divisible by 3 and 5.
# answer[i] == "Hulk" if i is divisible by 3.
# answer[i] == "Smash" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
def hulk_smash(n):
    answer = []
    for i in range(1, n+1):
        if (i%3 == 0 and i%5 == 0):
            answer.append("HulkSmash")
        elif (i%3 == 0):
            answer.append("Hulk")
        elif (i%5 == 0):
            answer.append("Smash")
        else:
            answer.append(str(i))
    return answer

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))

# Problem 3: Encode
# The Riddler is planning to leave a coded message to lead Batman into a trap. 
# Write a function shuffle() that takes in a string, the Riddler's message, and encodes it 
# using an integer array indices. The message will be shuffled such that the character at the ith position 
# in message moves to index indices[i] in the shuffled string. You may assume len(message) is equal to the len(indices).
def shuffle(message, indices):
    message_len = len(message)
    indices_len = len(indices)
    encoded = [''] * message_len
    if message_len == indices_len:
        for i in range(message_len):
            encoded[indices[i]] = message[i]
        return ''.join(encoded)

message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))

# Problem 4: Good Samaritan
# Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. 
# He wants to distribute meals in the least number of trips possible.
# Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. 
# There are also m empty boxes which can contain up to capacity[i] meals.
# Given an array meals of length n and capacity of size m, write a function minimum_boxes() that returns 
# the minimum number of boxes needed to redistribute the n packs of meals into boxes.
# Note that meals from the same pack can be distributed into different boxes.
def minimum_boxes(meals, capacity):
    total_meals = sum(meals)
    capacity.sort(reverse = True)
    count = 0
    for i in capacity:
        total_meals = total_meals - i
        count += 1
        if total_meals <= 0:
            return count
    return -1

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))

# Problem 5: Heist
# The legendary outlaw Robin Hood is looking for the target of his next heist. 
# Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts 
# where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.
# If multiple customers have the highest wealth, return the index of any customer.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.
def wealthiest_customer(accounts):
    max_wealth = 0
    result = []
    for i in range(len(accounts)):
        total = sum(accounts[i])
        if total > max_wealth:
            max_wealth = total
            result = [i, max_wealth]
    return result

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
print(wealthiest_customer(accounts))

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
print(wealthiest_customer(accounts))

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
print(wealthiest_customer(accounts))

# Problem 6: Smaller Than
# Write a function smaller_than_current that accepts a list of integers nums and, for each element 
# in the list nums[i], determines the number of other elements in the array that are smaller than it. 
# More formally, for each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer as a list.