#..........
#467..114..
#...*......
#..35..633.
#..........

with open('advent3data_shortist.txt', 'r') as file:
	line = file.readlines()

	total = 0
	
	for i in range(0, len(line)):
		for j in range(0,10):		
			if line[i][j].isnumeric():
				number = ' '
				
				print(line[i][j])