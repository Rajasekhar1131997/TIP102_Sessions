"""
Problem 1: Calculating Village Size
In the kingdom of Codepathia, the queen determines how many resources to distribute to a village based on its class. 
A village's class is equal to the number of digits in its population. Given an integer population, write a function get_village_class() 
that returns the number of digits in population.
Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
"""
def get_village_class_iterative(population):
    count = 0
    while (population > 0):
        population = population // 10
        count += 1
    return count

def get_village_class_recursive(population):
    if population == 0:
        return 0
    return 1 + get_village_class_recursive(population//10)

print("--------Problem 1---------")
print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))
print("Time Complexity for Iterative Approach: O(n)")
print("Space Complexity for Iterative Approach: O(1)")
print("Time Complexity for Recursive Approach: O(n)")
print("Space Complexity for Recursive Approach: O(n)")

"""
Problem 2: Counting the Castle Walls
In a faraway kingdom, a castle is surrounded by multiple defensive walls, where each wall is nested within another. Given a list of 
lists walls where each list [] represents a wall, write a recursive function count_walls() that returns the total number of walls.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def count_walls(walls):
    if not walls:
        return 1
    return 1+count_walls(walls[1])

print("--------Problem 2---------")
walls = ["outer", ["inner", ["keep", []]]]

print(count_walls(walls))
print(count_walls([]))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 3: Reversing a Scroll
A wizard is deciphering an ancient scroll and needs to reverse the letters in a word to reveal a hidden message. 
Write a recursive function to reverse the letters in a given scroll and returns the reversed scroll. 
Assume scroll only contains alphabetic characters.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def reverse_scroll(scroll):
    if not scroll or len(scroll) == 0:
        return scroll
    if len(scroll) == 1:
        return scroll[0]
    return reverse_scroll(scroll[1:]) + scroll[0]

print("--------Problem 3---------")
print(reverse_scroll("cigam"))
print(reverse_scroll("lleps"))
print(reverse_scroll("m"))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 4: Palindromic Name
Queen Ada is superstitious and believes her children will only have good fortune if their name is symmetrical and 
reads the same forward and backward. Write a recursive function that takes in a string comprised of only lowercase 
alphabetic characters name and returns True if the name is palindromic and False otherwise.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def is_palindrome(name):
    if not name or len(name) == 0:
        return True
    if len(name) == 1:
        return True
    if name[0] != name[-1]:
        return False
    return is_palindrome(name[1:-1])

print("--------Problem 4---------")
print(is_palindrome("eve"))
print(is_palindrome("ling"))
print(is_palindrome(""))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 5: Doubling the Power of a Spell
The court magician is practicing a spell that doubles its power with each incantation. Given an integer initial_power 
and a non-negative integer n, write a recursive function that doubles initial_power n times.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity.
"""
def double_power(initial_power, n):
    if not initial_power or initial_power == 0:
        return 0
    if n == 0:
        return initial_power
    else:
        return double_power(initial_power * 2, n-1)

print("--------Problem 5---------")
print(double_power(5, 3))
print(double_power(7, 2))
print(double_power(5, 1))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""

"""