from cards import calc_value_cards

def hand_value_check(player_cards, dealer_cards):
	"""[checks if the hand(interger list) of player and dealer are lower the man blackjack value: 21
		if not then it returns if player or dealer is busted or both busted]

	Arguments:
		player_cards {[int]} -- [total value of interger list]
		dealer_cards {[int]} -- [total value of interger list]

	Returns:
		[boolean] -- [True if none of player or dealer busted, else it returns false]
	"""
	if (check_21(player_cards, dealer_cards) == True):
		return (False)
	if (dealer_cards > 21 or player_cards > 21):
		if(dealer_cards > 21 and player_cards > 21):
			print('BOTH YOU AND DEALER BUSTED')
			print(player_cards, f'your current hand is worth: {player_cards}')
			print(dealer_cards, f'your current hand is worth: {dealer_cards}')
			return (False)
		elif(player_cards > 21):
			print('YOU BUST')
			print(player_cards, f'your current hand is worth: {player_cards}')
			print(dealer_cards, f'your current hand is worth: {dealer_cards}')
			return (False)
		else:
			print('YOU WON!!! DEALER BUSTED')
			print(player_cards, f'your current hand is worth: {player_cards}')
			print(dealer_cards, f'your current hand is worth: {dealer_cards}')
			return (False)
		print(player_cards, f'your current hand is worth: {player_cards}')
		print(dealer_cards, f'your current hand is worth: {dealer_cards}')
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

