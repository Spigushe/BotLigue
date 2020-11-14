from ..database import database
import challonge
import json

async def admin_message(message,connection):
	"""
	Function dealing with admin commands

	Args:
	message (object): a discord.Message
	connection : a sqite3 database
	"""
	content = message.content[10:] # ^bot admin $

	# Check if database connection is active
	if connection is None:
		await message.channel.send(f"Error! Connection to database impossible")
		return

	"""
	This needs to be documented and implemented
	# Testing for "admin" role
	if not check_admin_privilege(message.author):
		await message.author.reply(f"You don't seem to have enough privileges")
		return
	"""

	# Testing for command
	if content.lower().startswith("create "):
		await create_tournament(message,connection)

	return

