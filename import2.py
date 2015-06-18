import collections
import operator 

# Import the SEDAC population CSV file: 
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

# Set up lists for each continent: 
    africa_growth = []
    asia_growth = []
    oceania_growth = []
    europe_growth = []
    north_am_growth = []
    south_am_growth = []

# Each contient has a projected URBAN and RURAL growth over the next 90 years (2100 - 2010)
# I want a COMBINED (URBAN + RURAL) growth rate for each continent. 

# Put each continent's urban + rural growth into it's OWN list: 
    for line in inputFile: 
    	line = line.rstrip().split(",")
        if line[1] == 'Total National Population': 

            if line[0] == 'Africa':
                africa_growth.append(int(line[6]) - int(line[5]))

            if line[0] == 'Asia':
                asia_growth.append(int(line[6]) - int(line[5]))

            if line[0] == 'Oceania':
                oceania_growth.append(int(line[6]) - int(line[5]))

            if line[0] == 'Europe':
                europe_growth.append(int(line[6]) - int(line[5]))

            if line[0] == 'North America':
                north_am_growth.append(int(line[6]) - int(line[5]))

            if line[0] == 'South America':
                south_am_growth.append(int(line[6]) - int(line[5]))


   
# Put all the lists into a dictionary
    world_dictionary = {} 
    
    world_dictionary["europe"] = sum(europe_growth)
    world_dictionary["oceania"] = sum(oceania_growth)
    world_dictionary["asia"] = sum(asia_growth)
    world_dictionary["africa"] = sum(africa_growth)
    world_dictionary['north_america'] = sum(north_am_growth)
    world_dictionary['south_america'] = sum(south_am_growth) 


# Pull out just the values of the dictionary and sort them: 
    world_values = world_dictionary.values()
    sorted_world_values = sorted(world_values)

# Pull out the largest value and use it to search the World Dictionary: 
    search_key = sorted_world_values.pop()

# Find and print the name of the country that matches the largest value (population growth): 
    for key, value in world_dictionary.items(): 
    	if search_key == value: 
    		print "The continent with the highest projected growth in the next 90 years is {}".format(key)

# Print out my answer to an external file: 
with open('national_population.csv', 'w') as outputFile: 
    #outputFile.write('continent\n\n')
    for key, value in world_dictionary.items(): 
        if search_key == value: 
            outputFile.write("The continent with the highest projected growth in the next 90 years is {}".format(key))  



	








   










