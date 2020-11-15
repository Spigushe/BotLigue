from ...database import database
import challonge
import json
import discord

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

	# Commands
	if content.lower().startswith("create "):
		from . import create_tournament
		await create_tournament.create_tournament(message,connection)

	if content.lower().startswith("list"):
		from . import list_tournament
		await list_tournament.list_tournament(message,connection)

	return
