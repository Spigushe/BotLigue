from ...database import database
import challonge
import json
import discord

async def destroy_tournament(message, connection):
	"""
	Destroy a Challonge tournament

	Args:
		"Tournament Name"
	"""
	content = message.content[18:] # ^bot admin destroy $

	# Extracting tournament name
	if "-name" in content:
		t_name = content.split("-name")[1][1:]
	else:
		t_name = " ".join(content.split(" ")[0].split("-"))

	# Check if tournament exists in database
	if not t_exists(connection, t_name, message.guild.id):
		await message.channel.send(f"The tournament named `{t_name}` does not exist in the database")
		return

	# Destroy tournament in Challonge
	success = await execChallongeDestroyTournament(connection, t_name, message.guild.id)
	if not success:
		await message.channel.send(f"There have been a issue while deleting tournament `{t_name}`")
		return

	await message.channel.send(f"<@{message.author.id}>, tournament `{t_name}` is deleted ")

	return

def t_exists(connection, name, g_id):
	sql = "SELECT * FROM tournaments WHERE t_name = ? AND g_id = ? AND t_status = 1"
	query = database.execute_request(connection, sql, (name,g_id))

	if query == []:
		return False

	return True

async def execChallongeDestroyTournament(connection, name, g_id):
	sql = "SELECT t_url FROM tournaments WHERE t_name = ? AND g_id = ? AND t_status = 1"
	query = database.execute_request(connection, sql, (name,g_id))

	if query == []:
		return False

	for url in query:
		if url != "":
			challonge.tournaments.destroy(url)
			await setTournamentClosed(connection, name, g_id)

	return True

async def setTournamentClosed(connection, name, g_id):
	sql = "UPDATE tournaments SET t_status = 0 WHERE t_name = ? AND g_id = ?"
	query = database.execute_request(connection, sql, (name,g_id))

	return
