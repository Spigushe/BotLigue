from ...database import database
import challonge
import json
import discord

async def show_help(message):
	# Embed message
	embed = discord.Embed(
		title="Registration Process Helper",
		description="Here is a list of options you can use for the `bot register` command",
		color=set_color("#2779C3"),
		type="Rich",
		url="https://github.com/Spigushe/BotLigue/blob/main/Registration.md"
	)
	embed.set_thumbnail(url="https://ligue.spigushe.com/Afficher/CSS/Images/Logo.png")
	embed.set_footer(text=f"List of options for `bot register` command")

	# List of mandatory options
	embed.add_field( name="Mandatory options",value="Hereunder is the list of mandatory options to register",inline=False )
	embed.add_field( name="-decklist",value="Register the deck you are using, please use a link you will not update during the season",inline=True )
	embed.add_field( name="-hash",value="Announce the hash of your deck, please use a hash you will not update during the season",inline=True )

	# List of facultative options
	embed.add_field( name="Facultative options",value="Hereunder is the list of facultative options to register",inline=False)
	embed.add_field( name="-nickname",value="Set your nickname to one different from the one you are using here",inline=True )
	embed.add_field( name="-cz", value="Help us with naming your command zone here", inline=True )
	embed.add_field( name="-archetype",value="Help us determining the archetype of your deck",inline=True )

	await message.channel.send(embed=embed)



	return

def set_color(str):
	if "#" in str:
		str = str.replace("#","")
	return int(str,16)
