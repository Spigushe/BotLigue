from ...database import database
import challonge
import json
import discord

async def show_help(message):
	# Embed message
	embed = discord.Embed(
		title="Registration Process Helper",
		description="Here is a list of options you can use for the `bot register` command",
		color=int("#2779C3".replace("#",""),16),
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


async def initiate_registration(message, connection):
	"""
	The user wants to join a tournament
	"""
	content = message.content[13:] # ^bot register $

	# First check is call to helper
	if "-help" in content:
		await show_help(message)
		return

	# Second check is use of mandatory options
	if "-decklist" in content or "-hash" in content: # 1-step process
		if "-decklist" not in content or "-hash" not in content:
			await message.channel.send("Missing some mandatory option, you can use `bot register -help` for further assistance")
			return

		# Processing options
		registration = {
			"disc_id": message.author.id,
			"disc_nm": message.author.name+"#"+message.author.discriminator,
			"disc_gi": message.author.guild.id,
			"disc_gn": message.author.guild.name,
			"deck": content.split("-decklist")[1][1:],
			"hash": content.split("-hash")[1][1:],
			"nick": content.split("-nickname")[1][1:] if "-nickname" in content else message.author.name,
			"zone": content.split("-cz")[1][1:] if "-cz" in content else "",
			"arch": content.split("-archetype")[1][1:] if "-archetype" in content else "",
		}

		for key in registration:
			for opt in ["-decklist","-hash","-nickname","-cz","-archetype"]:
				if opt in str(registration[key]):
					registration[key] = registration[key].split(opt)[0][:-1]

		#if "-decklist" in r_hash:
		#	r_hash = r_hash.split("-decklist")[0][:-1]

		await message.channel.send(f"Information: {registration}")
		return

	else: # 2-step process
		await message.channel.send("Registration: 2-step process")
		return

	return
