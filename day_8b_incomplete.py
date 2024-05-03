with open('advent8datashortb.txt' , 'r') as file:
	lines_split = file.read().split('\n\n')
	directions = lines_split[0]

	element_lines = lines_split[1].split('\n')
	element_dictionary = {}
	nodes = []
	start_nodes = []
	end_nodes = []
	
	for i in range(0, len(element_lines)):	
		single_element_line = element_lines[i].split(' = ')
		split_destination = single_element_line[1].strip(' ()').split(', ')
		start = single_element_line[0]
		nodes.append(start)
		element_dictionary[start] = split_destination		
	
	for node in nodes:
		if node[2] == 'A':
			start_nodes.append(node)
		if node[2] == 'Z':
			end_nodes.append(node)
	
	moves = 0
	
	for k in range(0, len(start_nodes)):

	for items in start_nodes:
		for j in range(0, len(directions)):
			destination_options = element_dictionary[start_position]
			direction = directions[j]
			if j == (len(directions)-1):
				j = 0
			if direction == 'L':
				start_position = destination_options[0]
			if direction == 'R':
				start_position = destination_options[1]
			moves += 1
	print(moves)
	
	#missread question. Need to do the same move on all until they all end up ending in z at the same time




	
	
	





