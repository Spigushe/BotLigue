# BotLigue
Python Discord Bot using Challonge API to manage tournaments

## Requirements
The bot is based on the following packages and their dependancies
* `Discord.py` ([documentation](https://discordpy.readthedocs.io/en/latest/index.html))
* `pychal` ([documentation](https://github.com/ZEDGR/pychal))
* `dotenv`([documentation](https://pypi.org/project/python-dotenv/))

## Installation
You can download this repository and set a `.env` file at the project root. Note
that `.env` is not uploaded to GitHub as it is ignored via `.gitignore`. The
information required to be put into the file is mentioned later.

Then, you have to run the setup script
```bash
pip install -e .
```

And then you can start the bot using the following command
```bash
bot
```

## Usage
### Setting Tokens
Create a `.env` file at root level. Serve the file with tokens from
[Discord](https://discord.com/developers/) and from
[Challonge](https://challonge.com/fr/settings/developer)
```python
[discord]
DISCORD_TOKEN={your-discord-token-here}

[challonge]
CHALLONGE_NICKNAME={your-challonge-nickname}
CHALLONGE_TOKEN={your-challonge-token}
```

## List of commands
Commands start with `bot ` at the start of the message

### User commands
The first command being developed as of now is `bot register`. More information
can be found [here](https://github.com/Spigushe/BotLigue/blob/main/Registration.md).

### Admin commands
Admin commands are meant to be executed by `Guild.Member` with `Administrator`
permission

#### Admin commands with parameters
The above commands are also implemented using parameters

```bash
bot admin list [-open|-closed]
bot admin create -name Tournament Name -type Tournament Type
bot admin destroy -name Tournament Name
```

Note:
- `Spaces` are allowed in this use of commands

#### Admin commands without parameters
Hereunder is a list of bot commands

```bash
bot admin list
bot admin create Tournament-Name Tournament-Type
bot admin destroy Tournament-Name
```

Note:
- Arguments need to not have any `space` and should be written with a `-`
- `bot admin list` without parameters will display both `-open` and `-closed`
tournaments

## Helping developing the Bot
If you want new feature to be added, please request them in the
[Issues](https://github.com/Spigushe/BotLigue/issues) section.

If you want to share your knowledge and help developing the Bot, you are welcome
to fork this project and send a
[pull request](https://github.com/Spigushe/BotLigue/pulls).
