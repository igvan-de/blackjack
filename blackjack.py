from saw import saw
from cards import first_two_cards
from check import hand_value_check
from check import check_winner
from dealer import dealer_rules
from play_hand import play_hand

def blackjack():
	"""[main program that runs all combined functions step by step to play blackjack against dealer(computer)]
	"""
	print('DO YOU WANT TO PLAY A GAME?')
	if (saw(input()) == False):
		return
	player_cards = list(first_two_cards())
	dealer_cards = list(first_two_cards())
	print(player_cards, f'your current hand is worth: {sum(player_cards)}')
	print(dealer_cards, f'dealer current hand is worth: {sum(dealer_cards)}')
	if (play_hand(player_cards, dealer_cards) == True):
		while (sum(dealer_cards) < 17 and hand_value_check(player_cards, dealer_cards) == True):
			dealer_cards = dealer_rules(dealer_cards)
			print(dealer_cards, f'dealer current hand is worth: {sum(dealer_cards)}')
		if (hand_value_check(player_cards, dealer_cards) == False):
			return
		print(check_winner(sum(player_cards), sum(dealer_cards)))
blackjack()
