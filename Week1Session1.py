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

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)