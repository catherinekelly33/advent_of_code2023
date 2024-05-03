#note to aid coding a new line was added in the raw data after seeds to seperate the title and numbers

with open('advent5data.txt', 'r') as file:
	lines_split = file.read().split('\n\n')
	
	map_dictionary = {}
	seeds = []
	soils = []
	fertilizers = []
	waters = []
	lights = []
	temperatures = []
	humidities = []
	locations = []
	
	
	for item in lines_split:
		map = item.split('\n')
		map_list = []
		for i in range(1, len(map)):
			map_split = map[i].split(' ')
			map_list.append(map_split)
					
		map_dictionary[map[0]] = map_list
	
	
	#to get seed numbers
	for j in range(0, len(map_dictionary['seeds:'][0])):
		seeds.append(int(map_dictionary['seeds:'][0][j]))
		
	def mapping_function(item_number, map_type, list_type):		
		for item in item_number:
			found = 0
			for k in range(0,len(map_dictionary[map_type])):
				destination_start = int(map_dictionary[map_type][k][0])
				source_start = int(map_dictionary[map_type][k][1])
				length = int(map_dictionary[map_type][k][2])
				if item in range(source_start, (source_start+length)):
					list_type.append((item - source_start) +  destination_start)
					found += 1
			if found == 0:
				list_type.append(item)
		return list_type

	
	print('seeds =' , seeds)
	print('soil =', mapping_function(seeds, 'seed-to-soil map:', soils))
	print('fertilizer =', mapping_function(soils, 'soil-to-fertilizer map:', fertilizers))
	print('water =', mapping_function(fertilizers, 'fertilizer-to-water map:', waters))
	print('light =', mapping_function(waters, 'water-to-light map:', lights))
	print('temperature =', mapping_function(lights, 'light-to-temperature map:', temperatures))
	print('humidity =', mapping_function(temperatures, 'temperature-to-humidity map:', humidities))
	location = mapping_function(humidities, 'humidity-to-location map:', locations)
	print('location =', location)
	

	lowest_location = location[0]
	for l in range(1, len(location)):
		if location[l] < lowest_location:
			lowest_location = location[l]
	print('lowest_location =', lowest_location)
	
	
	
	