import random

def first_two_cards():
	"""[this functions creates two random intergers which represent the value of the cards]

	Returns:
		[string] -- [returns a tuple of the given card values]
	"""
	first_card = get_card()
	second_card = get_card()
	return (first_card, second_card)

def extra_card(hand):
	"""[appends and extra int(card) to current list of intergers(hand)]

	Arguments:
		hand {[list]} -- [current list of intergers]

	Returns:
		[list] -- [new list of intergers with new interger appended]
	"""
	extra_card = get_card()
	hand.append(extra_card)
	return (hand)

def random_select():
	"""[generates a random face card]

	Returns:
		[char] -- [returns character of Jack, Queen or King]
	"""
	cards = ["J", "Q", "K"]
	random_card = random.randint(0, 2)
	return (cards[random_card])

def get_card():
	"""[generates a random card and tansform a 11 into a ace]

	Returns:
		[int or char] -- [card value]
	"""
	card = random.randint(1, 11)
	if (card == 10):
		card = random_select()
	if (card == 11):
		card = "A"
	return (card)

def calc_value_cards(cards):
	"""[calculates the values of cards]

	Arguments:
		cards {[list]} -- [cards in hand player or dealer]

	Returns:
		[int] -- [value of cards]
	"""
	total_value = 0
	face_cards = ["J", "Q", "K"]
	for card in cards:
		for face in range(len(face_cards)):
			if (card == face_cards[face]):
				card = 10
		if (card == "A"):
			card = 11
		total_value += card
	return (total_value)
