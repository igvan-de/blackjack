from cards import extra_card
from check import hand_value_check
from dealer import dealer_rules
from continue_hand import continue_hand


def play_hand(player_cards, dealer_cards):
	"""[summary]

	Arguments:
		player_cards {[list]} -- [list of cards(integers) of player]
		dealer_cards {[list]} -- [list of cards(integers) of dealer]

	Returns:
		[boolean] -- [True if hand is continued with valid card values, else it returns false]
	"""
	print('Do you wish to continue?')
	while (continue_hand(input()) == True):
		player_cards = extra_card(player_cards)
		dealer_cards = dealer_rules(dealer_cards)
		if (sum(player_cards) < 21 and sum(dealer_cards) < 21):
			print(player_cards, f'your current hand is worth: {sum(player_cards)}')
			print(dealer_cards, f'dealer current hand is worth: {sum(dealer_cards)}')
		if (hand_value_check(player_cards, dealer_cards) == False):
			return(False)
		print('Do you wish to continue?')
	return(True)
