def saw(awnser):
	"""[a small joke function]

	Arguments:
		awnser {[string]} -- [given input by player]

	Returns:
		[boolean] -- [True if yes, False if no and returns itself with new given awnser if input was wrong]
	"""
	if (awnser.lower() == 'yes'):
		print('Let the game begin')
		return(True)
	elif(awnser.lower() == 'no'):
		return(False)
	else:
		print('Please give valid awnser; yes or no')
		awnser = input()
		return (saw(awnser))
