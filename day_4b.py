with open('advent4data.txt', 'r') as file:
	
	total_cards = 0
	card_dictionary = {1:1}
	j = 1
		
	for line in file:
		remove_card = line.split(':')
		split_cards = remove_card[1].strip().split('|')
		winning_numbers = split_cards[0].strip().split(' ')
		my_numbers = split_cards[1].strip().split(' ')

		matches = 0
		
		for i in range(0, len(winning_numbers)):
			if winning_numbers[i].isnumeric():
				if winning_numbers[i] in my_numbers:
					matches += 1

		if (j) in card_dictionary:
			pass
		else:
			card_dictionary[j] = 1 
		
		if matches > 0:
			for k in range(1, (matches+1)):
				if (j+k) in card_dictionary:
					pass
				else:
					card_dictionary[j+k] = 1 
				card_dictionary[j+k] += card_dictionary[j]
		
		j += 1
	
	for cards in card_dictionary.values():
		total_cards += cards

	print(total_cards)
	

