from ...database import database
import challonge
import json
import discord

async def user_message(message,connection):
	"""
	Function dealing with user commands

	Args:
	message (object): a discord.Message
	connection : a sqite3 database
	"""
	content = message.content[4:] # ^bot $

	# Check if database connection is active
	if connection is None:
		await message.channel.send(f"Error! Connection to database impossible")
		return

	# Commands
	if content.lower().startswith("register"):
		from . import register
		if "-help" in content:
			await register.show_help(message)
			return
			
		await register.initiate_registration(message,connection)
		return

	return
