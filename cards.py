
import random

def first_two_cards():
	"""[this functions creates two random intergers which represent the value of the cards]

	Returns:
		[string] -- [returns a tuple of the given card values]
	"""
	first_card = random.randint(1, 11)
	second_card = random.randint(1, 11)
	return (first_card, second_card)

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
