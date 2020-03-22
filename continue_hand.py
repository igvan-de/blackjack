def continue_hand(awnser):
	"""[continue_hand checks if the player wants to continue to play is hand,
		it also checks if input is valid, needs to be yes or no]

	Arguments:
		awnser {[string]} -- [input given by player]

	Returns:
		[boolean] -- [returns False if given input isn't as it required, else returns True
					  or it retruns to itself if input is wrong]
	"""
	if (awnser.lower() == 'yes'):
		return(True)
	elif(awnser.lower() == 'no'):
		return(False)
	else:
		print('Please give valid awnser; yes or no')
		awnser = input()
		return (continue_hand(awnser))

