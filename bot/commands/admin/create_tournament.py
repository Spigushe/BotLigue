from ...database import database
import challonge
import json
import discord

async def create_tournament(message,connection):
	"""
	Create a new Challonge tournament

	Args:
		"Tournament Name"
		"Tournament Type"
	"""
	content = message.content[17:] # ^bot admin create $

	# Building tournament dict
	tournament = {
		'guild': message.guild.id,
		'creator': message.author.id,
		'status': 1 # 1 for open / 0 for closed
	}
	await setNameType(message,tournament)
	await setURL(message,tournament)

	# Creating tournament using Challonge API
	await execChallongeCreateTournament(tournament)

	# Tournament into database
	database.create_tournament(connection, tournament)

	# Confirming tournament creation
	author = "<@" + str(tournament['creator']) + ">"
	await message.channel.send(f"{author}, tournament `{tournament['name']}` is created ")

	return


async def setNameType(message,tournament):
	content = message.content[17:] # ^bot admin create $

	t_name = ""
	t_type = ""
	# Other implementations can be done
	if "-name" and "-type" in content:
		#-name tournament name -type tournament type
		t_name = content.split("-name")[1][1:]
		if "-type" in t_name:
			t_name = t_name.split("-type")[0][:-1]

		t_type = content.split("-type")[1][1:]
		if "-name" in t_type:
			t_type = t_type.split("-name")[0][:-1]

	elif "-name" and "-type" not in content:
		#tournament-name tournament-type
		args = content.split(" ")
		t_name = " ".join(args[0].split("-"))
		t_type = " ".join(args[1].split("-"))
	else:
		await message.channel.send("Error! Non-supported query")

	tournament['name'] = t_name
	tournament['type'] = t_type.lower()
	return

async def setURL(message,tournament):
	t_url = ""

	words = (message.guild.name).split(" ")
	for word in words:
		t_url += word.lower()[:1]

	tournament['url'] = t_url + "_" + "".join(tournament['name'].lower().split(" "))
	return

async def execChallongeCreateTournament(tournament):
	chal_json = challonge.tournaments.create(tournament['name'], tournament['url'], tournament['type'])
	file = "bot/tournaments/" + tournament['url'] + ".json" # */tournaments/ is in .gitignore
	with open(file, "w") as write_file:
		json.dump(chal_json, write_file, indent=4, default=str)
	tournament['id'] = chal_json['id']
	return
