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

print(most_endangered(species_list))


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

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))



def navigate_research_station(station_layout, observations):
    if not station_layout:
        return 0
    mapping = {letter: idx for idx, letter in enumerate(station_layout)}
    total_time = 0
    index = 0
    for i in observations:
        j = mapping[i]
        total_time += abs(j-index)
        index = j
    return total_time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

def prioritize_observations(observed_species, priority_species):
    new_list = []
    for species in priority_species:
        new_list.extend([s for s in observed_species if s==species])

    remaining_species = sorted([s for s in observed_species if s not in priority_species])
    return new_list + remaining_species
  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species2, priority_species2))


def distinct_averages(species_populations):



species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 