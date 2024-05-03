with open('advent1data.txt' , 'r') as file:

	total_value = 0

	for line in file :
		answer = []
		for char in line:
			if char.isnumeric():answer.append(int(char))
		combined = (answer[0]*10 + answer[-1])	
		total_value += combined
		
	
	print(total_value)







