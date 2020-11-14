# Bot Main File
import os

# Importing .env infos
from dotenv import load_dotenv
load_dotenv()

# Discord
import discord
client = discord.Client()
## commands
from .commands import (admin,user)

# Challonge Library
import challonge
challonge.set_credentials(os.getenv("CHALLONGE_NICKNAME"), os.getenv("CHALLONGE_TOKEN"))

# Importing database settings
import json
from .database import database
from .database import structure
connection = database.create_connection("./bot/database/database.sqlite")

@client.event
async def on_ready():
	"""
	Sets activity to playing MtG
	Login success informative log
	"""
	game = discord.Game("Magic: the Gathering")
	await client.change_presence(status=discord.Status.online, activity=game)
	print(f"Logged in as {client.user}")
	# Checking tables existence
	if connection is not None:
		database.create_table(connection, structure.sql_create_tournaments_table)
	else:
		print("Error! cannot create the database connection")

@client.event
async def on_message(message):
	"""
	Main message loop

	Args:
	message (object): a discord.Message
	"""
	# Checking if the bot is sending a message
	if message.author == client.user:
		return

	# Checking if the message is calling the bot
	if message.content.lower().startswith("bot "):
		content = message.content[4:] # ^bot $
		print(f"Received: {content}")

		# Admin Commands
		if content.lower().startswith("admin "):
			await admin.admin_message(message,connection)

		# User Commands
		else:
			user.user_message(message)

# Starting the bot
def main():
	client.run(os.getenv("DISCORD_TOKEN"))
