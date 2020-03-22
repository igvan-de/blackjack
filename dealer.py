from cards import extra_card

def dealer_rules(dealer_cards):
	"""[checks if dealer_cards value is lower then 17, to append extra card(interger) to list]

	Arguments:
		dealer_cards {[list]} -- [list of intergers(cards) of dealer]

	Returns:
		[list] -- [return new list with append card(interger) or existing list]
	"""
	if(sum(dealer_cards) < 17):
		dealer_cards = extra_card(dealer_cards)
		return(dealer_cards)
	return(dealer_cards)
