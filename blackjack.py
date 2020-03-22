 # this program is based on the gamble game blackjack

import random

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

def first_two_cards():
	"""[this functions creates two random intergers which represent the value of the cards]

	Returns:
		[string] -- [returns a tuple of the given card values]
	"""
	first_card = random.randint(1, 11)
	second_card = random.randint(1, 11)
	return (first_card, second_card)

def continue_hand(awnser):
	"""[continue_hand checks if the player wants to continue to play is hand]

	Arguments:
		awnser {[string]} -- [the awnser given by player, should be yes or no]

	Returns:
		[boolean] -- [returns True if player wants to continue game, else returns False]
	"""
	return (awnser.lower() == 'yes')

def extra_card(hand):
	"""[appends and extra int(card) to current list of intergers(hand)]

	Arguments:
		hand {[list]} -- [current list of intergers]

	Returns:
		[list] -- [new list of intergers with new interger appended]
	"""
	extra_card = random.randint(1, 11)
	hand.append(extra_card)
	return (hand)

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

def check_winner(hand_player, hand_dealer):
	"""[check_winner checks if player or dealer has the best hand to win this round]

	Arguments:
		hand_player {[int]} -- [total value of the hand]
		hand_dealer {[int]} -- [total value of the hand]

	Returns:
		[string] -- [string of who won and their value]
	"""
	if (hand_dealer > hand_player):
		return (f'DEALER WON WITH: {hand_dealer}')
	return (f'YOU WON WITH: {hand_player}')

def blackjack():
	player_cards = list(first_two_cards())
	dealer_cards = list(first_two_cards())
	print(player_cards)
	print(dealer_cards)
	print('Do you wish to continue?')
	while (continue_hand(input()) == True):
		player_cards = extra_card(player_cards)
		dealer_cards = extra_card(dealer_cards)
		if (sum(player_cards) < 21 and sum(dealer_cards) < 21):
			print(player_cards, f'your current hand is worth: {sum(player_cards)}')
			print(dealer_cards, f'your current hand is worth: {sum(dealer_cards)}')
		if (hand_value_check(player_cards, dealer_cards) == False):
			return
	print(check_winner(sum(player_cards), sum(dealer_cards)))
blackjack()
