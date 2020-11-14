def user_message(m):
	"""
	Function dealing with admin commands

	Args:
	m (object): a discord.Message
	"""
	content = m.content[4:] # ^bot $
	print(f"Test User: {content}")
