with open('advent6data.txt' , 'r') as file:

	time_line = file.readline().strip().split(':')
	distance_line = file.readline().strip().split(':')



	time = int(time_line[1].replace(' ', ''))
	distance = int(distance_line[1].replace(' ', ''))
	print(time)
	print(distance)
	
	
	for k in range(1, time):
		distance_travelled = (time - k) * k
		if distance_travelled > distance:
			start = k
			break
	
	for l in range(time, 1, -1):
		distance_travelled = (time - l) * l
		if distance_travelled > distance:
			end = l
			break	

	print(start)
	print(end)

	total_wins = end - start + 1
	
	print(total_wins)






