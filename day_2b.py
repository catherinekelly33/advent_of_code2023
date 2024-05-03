# 12 red; 13 green; 14 blue
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

with open('advent2data.txt' , 'r') as file:
	
	total_value = 0
	
	for line in file:
		split_line = line.split(':')
		sets = split_line[1].split(';')
		max_colour = {'green':0, 'red':0, 'blue':0}
				
		for game in sets:
			game_split = game.split(',')
			for balls in game_split:
				ball = balls.strip().split(' ')
				colour = ball[1]
				count = int(ball[0])
				if count > max_colour[colour]:
					max_colour[colour] = count
		total_value += max_colour['green'] * max_colour['red'] * max_colour['blue']
	print(total_value)
					
		
	