with open('advent1data.txt' , 'r') as file:

	total_value = 0

	for line in file :
		line = (line.replace('zero' , 'z0ero'))
		line = (line.replace('one' , 'o1ne'))
		line = (line.replace('two' , 't2wo'))
		line = (line.replace('three' , 't3hree'))
		line = (line.replace('four' , 'f4our'))
		line = (line.replace('five' , 'f5ive'))
		line = (line.replace('six' , 's6ix'))
		line = (line.replace('seven' , 's7even'))
		line = (line.replace('eight' , 'e8ight'))
		line = (line.replace('nine' , 'n9ine'))
		answer = []
		for i in line:
			if i.isnumeric(): answer.append(int(i))
		combined = (answer[0]*10 + answer[-1])	
		total_value += combined
			
print(total_value)





