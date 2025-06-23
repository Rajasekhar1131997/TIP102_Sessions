"""
Problem 1: Most Endangered Species
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns 
the species with the highest conservation priority based on its population.
The function should take in a list of dictionaries named species_list as a parameter. 
Each dictionary represents data associated with a species, including its name, habitat, and wild population. 
The function should return the name of the species with the lowest population.
If there are multiple species with the lowest population, return the species with the lowest index.
"""
def most_endangered(species_list):
    if not species_list:
        return None
    
    minimum_population = species_list[0]["population"]
    result_name = species_list[0]["name"]

    for species in species_list[1:]:
        if species.get("population") < minimum_population:
            minimum_population = species.get("population")
            result_name = species.get("name")
    return result_name

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print("--------Problem 1---------")
print(most_endangered(species_list))

"""
Problem 2: Identifying Endangered Species
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. 
Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, 
represented by the string observed_species. 
Each character in observed_species denotes a species observed in the region.
Your task is to determine how many instances of the observed species are also considered endangered.
Note: Species are case-sensitive, so "a" is considered a different species from "A".
Write a function to count the number of endangered species observed.
"""
def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    count = 0
    for species in observed_species:
        if species in endangered_set:
            count +=1
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print("--------Problem 2---------")
print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))

"""
Problem 3: Navigating the Research Station
In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. 
Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), 
you start your journey at the first observation point (index 0). To make observations in a specific order represented 
by a string observations, you need to move from one point to another.
The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.
Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.
"""
def navigate_research_station(station_layout, observations):
    if not station_layout:
        return 0
    position = {station_layout[i]: i for i in range(26)}
    total_time = 0
    current = 0
    for char in observations:
        target = position[char]
        total_time += abs(target-current)
        current = target
    return total_time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print("--------Problem 3---------")
print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

"""
Problem 4: Prioritizing Endangered Species Observations
In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. 
The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.
Write a function prioritize_observations() that sorts the elements of observed_species such that the 
relative ordering of items in observed_species matches that of priority_species. Species that do not appear in priority_species 
should be placed at the end of observed_species in ascending order.
"""
def prioritize_observations(observed_species, priority_species):
    new_list = []
    for species in priority_species:
        new_list.extend([s for s in observed_species if s==species])

    remaining_species = sorted([s for s in observed_species if s not in priority_species])
    return new_list + remaining_species
  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print("--------Problem 4---------")
print(prioritize_observations(observed_species2, priority_species2))

"""
Problem 5: Calculating Conservation Statistics
You are given a 0-indexed integer array species_populations of even length, where each element represents 
the population of a particular species in a wildlife reserve.
As long as species_populations is not empty, you must repetitively:
Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.
For example, the average of 200 and 300 is (200+300)/2=250.
Return the number of distinct averages calculated using the above process.
Note that when there is a tie for a minimum or maximum population, any can be removed.
"""
"""
def distinct_averages(species_populations):
    averages = set()
    while(species_populations):
        minimum = min(species_populations)
        maximum = max(species_populations)
        avg = (minimum+maximum)/2
        averages.add(avg)
        species_populations.remove(minimum)
        species_populations.remove(maximum)
    return len(averages)
"""
# Two pointer approach
def distinct_averages(species_populations):
    species_populations.sort()
    left = 0
    right = len(species_populations) - 1
    averages = set()
    while left < right:
        avg = ((species_populations[left] + species_populations[right]) / 2)
        averages.add(avg)
        left += 1
        right -= 1
    return len(averages)

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print("--------Problem 5---------")
print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

"""
Problem 6: Wildlife Reintroduction
As a conservationist, your research center has been raising multiple endangered species and is now ready to reintroduce 
them into their native habitats. You are given two 0-indexed strings raised_species and target_species. 
The string raised_species represents the list of species available to release into the wild at your center, 
where each character represents a different species. 
The string target_speciesrepresents a specific sequence of species you want to form and release together.
You can take some species from raised_species and rearrange them to form new sequences.
Return the maximum number of copies of target_species that can be formed by taking species from raised_species and rearranging them.
"""
def max_species_copies(raised_species, target_species):
    raised = {}
    for char in raised_species:
        raised[char] = raised.get(char, 0) + 1
    target = {}
    for char in target_species:
        target[char] = target.get(char, 0) + 1
    
    count = []
    for char, value in target.items():
        available = raised.get(char, 0)
        copies_of_char = available // value
        count.append(copies_of_char)
    return min(count)
  
print("--------Problem 6---------")
raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2

"""
Problem 7: Count Unique Species
You are given a string ecosystem_data that consists of digits and lowercase English letters. 
The digits represent the observed counts of various species in a protected ecosystem.
You will replace every non-digit character with a space. For example, "f123de34g8hi34" will become " 123 34 8 34". 
Notice that you are left with some species counts that are separated by at least one space: "123", "34", "8", and "34".
Return the number of unique species counts after performing the replacement operations on ecosystem_data.
Two species counts are considered different if their decimal representations without any leading zeros are different.
"""
def count_unique_species(ecosystem_data):
    new_string = []
    for char in ecosystem_data:
        if char.isdigit():
            new_string.append(char)
        else:
            new_string.append(" ")
    new_string = ''.join(new_string)
    tokens = new_string.split()
    unique = set()
    for token in tokens:
        normalized = token.lstrip('0')
        if not normalized:
            normalized = 0
        unique.add(normalized)
    return len(unique)

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print("--------Problem 7---------")
print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))

"""
Problem 8: Equivalent Species Pairs
In an effort to understand species diversity in different habitats, researchers are analyzing species pairs observed in various regions. 
Each pair is represented by a list [a, b] where a and b represent two species observed together.
A species pair [a, b] is considered equivalent to another pair [c, d] if and only if either (a == c and b == d) or (a == d and b == c). 
This means that the order of species in a pair does not matter.
Your task is to determine the number of equivalent species pairs in the list of observed species pairs.
For a species pair that appears n times, the number of equivalent pairs that can be formed is given by the formula the formula : c * (c - 1) // 2
"""
from collections import Counter
def num_equiv_species_pairs(species_pairs):
    normalized = []
    for a, b in species_pairs:
        if a <= b:
            normalized.append((a,b))
        else:
            normalized.append((b,a))
    frequency = Counter(normalized)
    total = 0
    for freq in frequency.values():
        if freq > 1:
            total += (freq * (freq-1)) // 2
    return total
    

species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print("--------Problem 8---------")
print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))