# Bot Main File
import os
import json

# Importing .env infos
from dotenv import load_dotenv
load_dotenv()

# Discord
import discord
client = discord.Client()

# Challonge Library
import challonge
challonge.set_credentials(os.getenv("CHALLONGE_NICKNAME"), os.getenv("CHALLONGE_TOKEN"))

@client.event
async def on_ready():
	"""
	Login success informative log
	"""
	print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
	"""
	Main message loop

	Args:
	message (object): a discord.Message
	"""
	if message.author == client.user:
		return

	if message.content.lower().startswith("bot "):
		content = message.content[4:]
		print(f"Received: {content}")

			await message.delete()

# Starting the bot
client.run(os.getenv("DISCORD_TOKEN"))
