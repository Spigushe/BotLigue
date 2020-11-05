# BotLigue
Python Discord Bot using Challonge API to manage tournaments

## Requirements
The bot is based on the following packages and their dependancies
* `Discord.py`
* `pychal`

## Installation
*to be detailed*

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

### Admin commands
Admin commands are meant to be executed by `Guild.Member` with `Administrator`
role. *This has to be implemented*

Hereunder is a list of bot commands. The brackets are not meant to be typed and
might induce bugs. *This needs to be resolved*

```bash
bot admin create {Tournament Name} {Tournament Type}
```
