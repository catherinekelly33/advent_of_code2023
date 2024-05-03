# 12 red; 13 green; 14 blue

with open('advent2data.txt' , 'r') as file:

	total = 0

	max_balls = {'red':12, 'green':13, 'blue':14}

	for line in file:
		split_line = line.split(':')
		sets = split_line[1].split(';')
		failures = 0
		
		for game in sets:
			game_split = game.split(',')
			for balls in game_split:
				ball = balls.strip().split(' ')
				colour = ball[1]
				count = int(ball[0])
				if max_balls[colour] < count:
					failures += 1
	
		if failures == 0:
			game_number = int((split_line[0].split(' '))[1])
			total += game_number
	
	print(total)
			
			
	

