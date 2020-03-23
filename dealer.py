import random
from cards import extra_card

def calc_play_card(player_cards, dealer_cards):
	"""[checks if random number given in if statement is equal to 2 to continue with an extra card,
		this to make it more like a gamble also for the player if the dealer is hitting another card
		(want to make a calculation for dealer if it smart to do eventually)]

	Arguments:
		player_cards {[list]} -- [list of cards(integers) of player_cards]
		dealer_cards {[list]} -- [list of cards(integers) of dealer_cards]

	Returns:
		[list] -- [return new list with append card(interger) or existing list of dealer_cards]
	"""
	if (random.randint(0, 5) == 2):
		extra_card = random.randint(1, 11)
		dealer_cards.append(extra_card)
	return(dealer_cards)

def dealer_rules(player_cards, dealer_cards):
	"""[checks if dealer_cards value is lower then 17, to append extra card(interger) to list]

	Arguments:
		dealer_cards {[list]} -- [list of intergers(cards) of dealer]

	Returns:
		[list] -- [return new list with append card(interger) or existing list]
	"""
	if(sum(dealer_cards) < 17):
		dealer_cards = extra_card(dealer_cards)
		return(dealer_cards)
	#function that calculates the changes to win if get a new card
	dealer_cards = calc_play_card(player_cards, dealer_cards)
	return(dealer_cards)
