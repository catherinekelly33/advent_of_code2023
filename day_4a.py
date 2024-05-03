with open('advent4data.txt', 'r') as file:
	
	total_score = 0
	
	for line in file:
		remove_card = line.split(':')
		split_cards = remove_card[1].strip().split('|')
		winning_numbers = split_cards[0].strip().split(' ')
		my_numbers = split_cards[1].strip().split(' ')


		
		wins = 0
		
		for i in range(0, len(winning_numbers)):
			if winning_numbers[i].isnumeric():
				if winning_numbers[i] in my_numbers:
					wins += 1
			if wins > 0:
				score = 2**(wins-1)
			else:
				score = 0

		total_score += score
	
	print(total_score)