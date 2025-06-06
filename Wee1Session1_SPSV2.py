# Problem 1: Batman
# Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".
def batman():
    print("I am vengeance. I am the night. I am Batman!")

batman()

# Problem 2: Mad Libs
# Write a function madlib() that accepts one parameter, a string verb. 
# The function should print the sentence: "I have one power. I never <verb>. - Batman".

def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)

# Problem 3: Trilogy
# Write a function trilogy() that accepts an integer year and prints the title of the 
# Batman trilogy movie released that year as outlined below.
#Year	Movie Title
#2005	"Batman Begins"
#2008	"The Dark Knight"
#2012	"The Dark Knight Rises"
def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")

year = 2008
trilogy(year)

year = 1998
trilogy(year)

# Problem 4: Last
# Implement a function get_last() that accepts a list of items items and 
# returns the last item in the list. If the list is empty, return None.
def get_last(items):
    if not items:
        return None
    length = len(items)
    return items[length-1]

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items))

items = []
print(get_last(items))

items = ["Thor"]
print(get_last(items))

# Problem 5: Concatenate
# Write a function concatenate() that takes in a list of strings words and returns a string 
# concatenated that concatenates all elements in words.
def concatenate(words):
    result = ""
    if not words:
        return ""
    for word in words:
        result = result+word
    return result

words = ["vengeance", "darkness", "batman"]
print(concatenate(words))

words = []
print(concatenate(words))

# Problem 6: Squared
# Write a function squared() that accepts a list of integers numbers as a parameter and 
# squares each item in the list. Return the squared list.
def squared(numbers):
    for i in range(len(numbers)):
        numbers[i] = pow(numbers[i],2)
    return numbers

numbers = [1, 2, 3]
print(squared(numbers))

# Problem 7: NaNaNa Batman!
# Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" 
# where "na" is repeated x times. Do not use the * operator.
def nanana_batman(x):
    result = ""
    if (x == 0):
        return "batman!"
    elif x == 1:
        return "na batman!"
    else:
        for i in range(x):
            result += "na"
        return result + " batman!"

x = 6
print(nanana_batman(x))

x = 0
print(nanana_batman(x))

# Problem 8: Find the Villain
# Write a function find_villain() that accepts a list crowd and a value villain as parameters and 
# returns a list of all indices where the villain is found hiding in the crowd.
def find_villain(crowd, villain):
    result = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            result.append(i)
    return result

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))

# Problem 9: Odd
# Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.
def get_odds(nums):

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)