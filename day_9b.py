with open('advent9data.txt', 'r') as file:
	total_extrapolated = 0
	for line in file:
		initial_line = line.split(' ')
		dictionary = {0:initial_line}
		for i in range(0, len(initial_line)):
			test_line = dictionary[i]
			calculated_line = []
			line_number = i
			for j in range(0, (len(test_line))-1):
				calculated_line.append(int(test_line[j+1])-int(test_line[j]))
			dictionary[i+1] = calculated_line
			if all([x== 0 for x in calculated_line]):
				final_line_no = i+1
				break
		#print(final_line_no)
		#print(dictionary)
		
		for k in range((final_line_no-1), -1, -1):
			starting_line = dictionary[k]
			appended_line = []
			appended_line.append(int(dictionary[k][0])-int(dictionary[k+1][0]))
			for item in starting_line:
				appended_line.append(item)
			dictionary[k] = appended_line
		#print(appended_line)		
		total_extrapolated += appended_line[0]
	print(total_extrapolated)
