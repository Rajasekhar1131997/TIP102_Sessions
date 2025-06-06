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
        print("he Dark Knight")
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

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)