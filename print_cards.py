from cards import calc_value_cards

def print_cards(player, dealer):
	"""[print the cards in hand and the total value of hand]

	Arguments:
		player {[list]} -- [list containing card values]
		dealer {[list]} -- [list containing card values]
	"""
	print(player, f'your current hand is worth: {player}')
	print(dealer, f'dealer current hand is worth: {dealer}')
