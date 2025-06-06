# Problem 1: Hundred Acre Wood
# Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

# Problem 2: Greeting
# Write a function greeting() that accepts a single parameter, a string name, 
# and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
def greetings(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greetings("Michael")
greetings("Winnie the Pooh")

# Problem 3: Catchphrase
# Write a function print_catchphrase() that accepts a string character as a parameter 
# and prints the catchphrase of the given character as outlined in the table below.
#Character	Catchphrase
#"Pooh"	"Oh bother!"
#"Tigger"	"TTFN: Ta-ta for now!"
#"Eeyore"	"Thanks for noticing me."
#"Christopher Robin"	"Silly old bear."
# If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

# Problem 4: Return Item
# Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x 
# and returns the element at index x in items. If x is not a valid index of items, return None.
def get_item(items, x):
    if x < len(items) and x >=0:
        return items[x]
    else:
        return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))

# Problem 5: Total Honey
# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts 
# a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the 
# built-in function sum().
def sum_honey(hunny_jars):
    total = 0
    for i in range(len(hunny_jars)):
        total = total + hunny_jars[i]
    return total

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))

# Problem 6: Double Trouble
# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of 
# integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.
def doubled(hunny_jars):
    for i in range(len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
    return hunny_jars


hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

hunny_jars = [2, 4, 6, 8, 10]
print(doubled(hunny_jars))

# Problem 7: Poohsticks
# Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks 
# in a stream and race them. They time how long it takes each player's stick to float under 
# Poohsticks Bridge to score each round.

# Write a function count_less_than() to help Pooh and his friends determine how many players 
# should move on to the next round of Poohsticks. count_less_than() should accept a list of 
# integers race_times and an integer threshold and return the number of race times less than threshold.
def count_less_than(race_times, threshold):
    count = 0
    for i in race_times:
        if i < threshold:
            count += 1
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

# Problem 8: Pooh's To Do's
# Write a function print_todo_list() that accepts a list of strings named tasks. 
# The function should then number and print each task on a new line using the format:
# Pooh's To Dos:
# 1. Task 1
# 2. Task 2
def print_todo_list(task):
    count = 1
    print("Pooh's To Dos:")
    for i in range(len(task)):
        print(f"{count}.{task[i]}")
        count +=1

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)