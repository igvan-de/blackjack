def check_value(*hand):
	"""
	[check_values checks if the values of the given hand(cards) are equal to ten,
	if that's the case it will randomly make it to a Jack, Queen or King.
	If card value is equal to 11 it will convert it into an ace]

	Returns:
		[string] -- [returns string with the converted card values in it]
	"""
	result = ''
	values = 'JQK10'
	high_value = None
	for card in hand:
		if (card == 10):
			high_value = random.sample(values, 1)
			for item in high_value:
				if (item == '0' or item == '1'):
					item = '10'
				result += item
		elif(card == 11):
			result += 'A'
		else:
			result += str(card)
		result += ' '
	return result.strip()

def hand_value_check(player_cards, dealer_cards):
	"""[checks if the hand(interger list) of player and dealer are lower the man blackjack value: 21
		if not then it returns if player or dealer is busted or both busted]

	Arguments:
		player_cards {[int]} -- [total value of interger list]
		dealer_cards {[int]} -- [total value of interger list]

	Returns:
		[boolean] -- [True if none of player or dealer busted, else it returns false]
	"""
	if (sum(dealer_cards) > 21 or sum(player_cards) > 21):
		if(sum(dealer_cards) > 21 and sum(player_cards) > 21):
			print('BOTH YOU AND DEALER BUSTED')
			print(player_cards, f'your current hand is worth: {sum(player_cards)}')
			print(dealer_cards, f'your current hand is worth: {sum(dealer_cards)}')
			return (False)
		elif(sum(player_cards) > 21):
			print('YOU BUST')
			print(player_cards, f'your current hand is worth: {sum(player_cards)}')
			print(dealer_cards, f'your current hand is worth: {sum(dealer_cards)}')
			return (False)
		else:
			print('YOU WON!!! DEALER BUSTED')
			print(player_cards, f'your current hand is worth: {sum(player_cards)}')
			print(dealer_cards, f'your current hand is worth: {sum(dealer_cards)}')
			return (False)
		print(player_cards, f'your current hand is worth: {sum(player_cards)}')
		print(dealer_cards, f'your current hand is worth: {sum(dealer_cards)}')
	return (True)

def check_21(hand_player, hand_dealer):
	"""[check if value is equal to 21]

	Arguments:
		value {[boolean]} -- [returns True if value is equal to 21 else it returns False]
	"""
	if (hand_dealer == 21):
		print(f'DEALER WON WITH: {hand_dealer}')
		return(True)
	elif (hand_player == 21):
		print(f'YOU WON WITH: {hand_player}')
		return(True)
	return(False)

def check_winner(hand_player, hand_dealer):
	"""[check_winner checks if player or dealer has the best hand to win this round]

	Arguments:
		hand_player {[int]} -- [total value of the hand]
		hand_dealer {[int]} -- [total value of the hand]

	Returns:
		[boolean] -- [returns True if there is a winner or a draw else returns False]
	"""
	if (check_21(hand_dealer, hand_player) == True):
		return(True)
	elif (hand_dealer > hand_player):
		print(f'DEALER WON WITH: {hand_dealer}')
		return(True)
	elif(hand_dealer == hand_player):
		print(f'you both ended with the same hand: {hand_dealer} {hand_player}')
		return(True)
	print(f'YOU WON WITH: {hand_player}')
	return(False)

