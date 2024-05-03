with open('advent8data.txt' , 'r') as file:
	lines_split = file.read().split('\n\n')
	directions = lines_split[0]

	element_lines = lines_split[1].split('\n')
	element_dictionary = {}
	
	for i in range(0, len(element_lines)):	
		single_element_line = element_lines[i].split(' = ')
		split_destination = single_element_line[1].strip(' ()').split(', ')
		start = single_element_line[0]
		element_dictionary[start] = split_destination		

	start_position = 'AAA'
	moves = 0

	while start_position != 'ZZZ':
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
		




	
	
	





