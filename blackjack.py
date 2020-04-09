from saw import saw
from cards import first_two_cards
from cards import calc_value_cards
from check import hand_value_check
from check import check_winner
from check import check_21
from dealer import dealer_rules
from play_hand import play_hand

def print_cards(player, dealer):
		print(player, f'your current hand is worth: {calc_value_cards(player)}')
		print(dealer, f'dealer current hand is worth: {calc_value_cards(dealer)}')

def blackjack():
	"""[main program that runs all combined functions step by step to play blackjack against dealer(computer)]
	"""
	if (saw(input("DO YOU WANT TO PLAY A GAME?\n")) == False):
		return
	player_cards = list(first_two_cards())
	dealer_cards = list(first_two_cards())
	print_cards(player_cards, dealer_cards)
	if (hand_value_check(calc_value_cards(player_cards), calc_value_cards(dealer_cards)) == False):
		return
	while True:
		if (play_hand(player_cards, dealer_cards) == True):
			continue
		else:
			break
	if (calc_value_cards(player_cards) <= 21):
		dealer_cards = dealer_rules(dealer_cards)
	print_cards(player_cards, dealer_cards)
	if (hand_value_check(calc_value_cards(player_cards), calc_value_cards(dealer_cards)) == False):
		return
	check_winner(calc_value_cards(player_cards), calc_value_cards(dealer_cards))

if __name__ == "__main__":
	blackjack()














	# dealer_cards = dealer_rules(dealer_cards) #give problem when dealerhand isn't 17 yet but player wants to stop
	# if (hand_value_check(calc_value_cards(player_cards), calc_value_cards(dealer_cards)) == False):
	# 	return
	# if (check_winner(calc_value_cards(player_cards), calc_value_cards(dealer_cards)) == True):
	# 	return


	# if (play_hand(player_cards, dealer_cards) == True):
	# 	while (calc_value_cards(dealer_cards) < 17 and hand_value_check(player_cards, dealer_cards) == True):
	# 		dealer_cards = dealer_rules(dealer_cards) #give problem when dealerhand isn't 17 yet but player wants to stop
	# 		print(dealer_cards, f'dealer current hand is worth: {calc_value_cards(dealer_cards)}')
	# 	if (hand_value_check(calc_value_cards(player_cards), calc_value_cards(dealer_cards)) == False):
	# 		return
	# 	if (check_winner(calc_value_cards(player_cards), calc_value_cards(dealer_cards)) == True):
	# 		return

