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
		if content.lower().startswith("admin "):
			"""
			Administrator commands
			- CREATE 	Create a new tournament
			- CHECKIN 	Proceed to check-in
			- START 	Start tournament
			"""
		#	if not message.author.has_role("admin"):
		#		return


			content = message.content[10:] #bot admin /
			# Administrator Commands
			if content.lower().startswith("create "):
				"""
				Create a new Challonge tournament

				Args:
					"Tournament Name"
					"Tournament Type"
				"""
				# Dealing with context
				content = message.content[17:] #bot admin create /
				args = content.split(" ") #tournament-name tournament-type
				# Processing args
				t_name = " ".join(args[0].split("-"))
				t_url  = "CL_" + "".join(args[0].split("-"))
				t_type = " ".join(args[1].split("-")).lower()
				# Create tournament
				t_json = challonge.tournaments.create(t_name, t_url, t_type)
				# Saving tournament json file
				t_file = "tournaments/"+t_url+".json" # tournaments/ is in .gitignore
				with open(t_file, "w") as write_file:
					json.dump(t_json, write_file, indent=4, default=str)

			await message.delete()

# Starting the bot
client.run(os.getenv("DISCORD_TOKEN"))
