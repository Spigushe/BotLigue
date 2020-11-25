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

	# Testing for administrator permission
	if not await check_admin_privilege(message.author):
		await message.channel.send(f"{message.author.id}, you do not have `Administrator` permissions on this server")
		return

	# Commands
	if content.lower().startswith("create "):
		from . import create_tournament
		await create_tournament.create_tournament(message,connection)
		return

	if content.lower().startswith("destroy "):
		from . import destroy_tournament
		await destroy_tournament.destroy_tournament(message,connection)
		return

	if content.lower().startswith("list"):
		from . import list_tournament
		await list_tournament.list_tournament(message,connection)
		return

	return

async def check_admin_privilege(member):
	for role in member.roles:
		if role.permissions.administrator:
			return True

	return False
