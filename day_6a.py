with open('advent6data.txt' , 'r') as file:

	time_line = file.readline().strip().split(':')
	distance_line = file.readline().strip().split(':')
	time = time_line[1].strip().split('   ')
	distance = distance_line[1].strip().split('  ')
	print(time)
	print(distance)
	
	win_list = []		
	for k in range(0, len(time)):
		race_time = int(time[k])
		race_distance = int(distance[k])
		wins = 0
		for l in range(1, race_time):
			distance_travelled = (race_time - l) * l
			if distance_travelled > race_distance:
				wins += 1
		win_list.append(wins)
	print(win_list)

	total_wins = 1
	for item in win_list:
		total_wins = total_wins * item
	print(total_wins)






