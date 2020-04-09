from cards import extra_card
from cards import calc_value_cards
from check import hand_value_check
from check import check_21
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
	while (continue_hand(input('Do you wish to continue?\n')) == True):
		player_cards = extra_card(player_cards)
		if (calc_value_cards(player_cards) <= 21 and calc_value_cards(dealer_cards) <= 21):
			print(player_cards, f'your current hand is worth: {calc_value_cards(player_cards)}')
			print(dealer_cards, f'dealer current hand is worth: {calc_value_cards(dealer_cards)}')
		else:
			break
	return (False)
