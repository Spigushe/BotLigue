from ...database import database
import challonge
import json
import discord

async def list_tournament (message,connection):
	# Embed message
	embed = discord.Embed(
		title="List of tournaments",
		description="These tournaments are those created using the `admin create -name X -type Y` command",
		color=set_color("#2779C3"),
		type="Rich"
	)
	embed.set_thumbnail(url="https://ligue.spigushe.com/Afficher/CSS/Images/Logo.png")

	if "-open" in message.content or ("-open" and "-closed") not in message.content:
		embed.add_field(name="Open tournaments", value=get_list(connection,1,message.guild.id), inline=False)

	if "-closed" in message.content or ("-open" and "-closed") not in message.content:
		embed.add_field(name="Closed tournaments", value=get_list(connection,0,message.guild.id), inline=False)

	embed.set_footer(
        text=f"List of tournaments of {message.guild}"
    )
	await message.channel.send(embed=embed)

	return

def get_list(connection,status,guild_id):
	sql = "SELECT * FROM tournaments WHERE tournament_status = ? AND guild_id = ?"

	tourneys = database.execute_request(connection, sql, (status,guild_id))

	list = f""
	for tourney in tourneys:
		list = list + "[" + str(tourney[2]) + "](https://challonge.com/" + str(tourney[4]) + ")\n"

	if list == "":
		return "No tournaments in this category"

	return list

def set_color(str):
	if "#" in str:
		str = str.replace("#","")
	return int(str,16)
