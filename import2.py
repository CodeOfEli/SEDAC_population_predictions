import collections
import operator 

# Working with FILE: lecz-urban-rural-population-land-area-estimates_continent-90m.csv
# rU = read Universal NewLines

population_dict = collections.defaultdict(int)


with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    #pass
    header = next(inputFile)

    # for line in inputFile:
    # 	line = line.rstrip().split(",")
    # 	line[5] = int(line[5])
    # 	if line[1] == 'Total National Population':
    # 		population_dict[line[0]] += line[5]
    # print population_dict


# population change between 2010 and 2100: 
    africa_growth = []
    asia_growth = []
    oceania_growth = []
    europe_growth = []
    north_am_growth = []
    south_am_growth = []



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


   
    world_dictionary = {} 
   
    # print "Africa's future population will be {}".format(sum(africa_growth))
    # print "Asia's future population will be {}".format(sum(asia_growth))
    

    world_dictionary["europe"] = sum(europe_growth)
    world_dictionary["oceania"] = sum(oceania_growth)
    world_dictionary["asia"] = sum(asia_growth)
    world_dictionary["africa"] = sum(africa_growth)
    world_dictionary['north_america'] = sum(north_am_growth)
    world_dictionary['south_america'] = sum(south_am_growth) 


    print world_dictionary


    world_values = world_dictionary.values()
    sorted_world_values = sorted(world_values)

    print world_values
    print sorted_world_values
    search_key = sorted_world_values.pop()

    print search_key

    for key, value in world_dictionary.items(): 
    	if search_key == value: 
    		print "The continent with the highest projected growth in the next 90 years is {}".format(key)

   	# for key, value in world_dictionary.iteritems():
   	# 	print key, value 
   		# if search_key == value:
   		# 	print key
   		


    # if search_key in world_dictionary.values(): 
    # 	print search_key
    # 	del world_dictionary[search_key]
    	#print del world_dictionary[search_key]

    #{'africa': 1,116,325,992, 'asia': 1,780,634,474}
	# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}



	#print world_dictionary.values()
    
  	# print world 


    		


# CHECK IT
# Africa 573918429 + 327611385

# FUTURE AFRICA = 1,367,949,254 + 649,906,552 


# total 2010 is 573918429
# total 2010 is 327611385

# total FUTURE POP  is 1367949254
# total FUTURE POP  is 649906552





    	#print line[5], line[6]
    	# difference = float(line[6]) - float(line[5])
    	# print "The difference in population is {}".format(difference)

   



# Which continent is estimated to grow the most in the next 90 years?

# Which continent was most densely populated in 2010?
	# (total national population divided by the total land area and remember to convert at least one number to float).



# with open('national_population.csv', 'w') as outputFile: 
# 	outputFile.write('continent,2010_population\n')

# 	for key, value in population_dict.iteritems(): 
# 		outputFile.write(key + ',' + str(value) + '\n')










