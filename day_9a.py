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
				
		for k in range((final_line_no-1), -1, -1):
			up_calculated_line = dictionary[k]
			up_calculated_line.append(int(dictionary[k+1][-1])+int(dictionary[k][-1]))
			dictionary[k] = up_calculated_line
						
		total_extrapolated += up_calculated_line[-1]
	print(total_extrapolated)
