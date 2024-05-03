with open('advent7data.txt', 'r') as file:
	points = {}
	letters = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	five = []
	four = []
	full_house = []
	three = []
	two_pair = []
	one_pair = []
	high_card = []
	total_score = 0

	for line in file:
		data_list = line.split(' ')
		cards = data_list[0]
		#print(cards)
		cards_sorted = cards.replace('A', 'F').replace('K', 'E').replace('Q', 'D').replace('J', '1').replace('T', 'B')
		points[cards_sorted] = data_list[1]
		#print(cards_sorted)
	#print(points)		
		
	for hand in points.keys():
		#print(hand)
		matches = {}
		for i in range(0, len(hand)):
			if hand[i] != '1' or hand == '11111':
				matches[hand[i]] = hand.count(hand[i])
		#print(matches)
		count = list(matches.values())
		count.sort(reverse=True)
		#print(count)
		J = hand.count('1')
		#print(J)
		if count[0] == 5 or ((count[0] + J) == 5):
			five.append(hand)
		elif count[0] == 4 or ((count[0] + J) == 4):
			four.append(hand)
		elif (count[0] == 3 or ((count[0] + J == 3))) and (count[1] == 2):
			full_house.append(hand)
		elif (count[0] == 3 or ((count[0] + J == 3))) and count[1] == 1:
			three.append(hand)
		elif (count[0] == 2 or ((count[0] + J == 2))) and (count[1] == 2):
			two_pair.append(hand)
		elif (count[0] == 2 or ((count[0] + J == 2))) and count[1] == 1:
			one_pair.append(hand)
		elif count[0] == 1:
			high_card.append(hand)
	
	#print(five, four, full_house, three, two_pair, one_pair, high_card)
	all_hands = [high_card, one_pair, two_pair, three, full_house, four, five]
	
	for group in all_hands:
		group.sort()
	#	print(group)
	k = 1
	order = {}
	for group in all_hands:
		for set in group:
			order[set] = k
			score = int(points[set]) * k
			#print(score)
			k += 1
			total_score += score
	#print(order)
	print(total_score)

	
				