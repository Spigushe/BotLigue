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
role. **This has to be implemented**

Hereunder is a list of bot commands.

```bash
bot admin create {Tournament-Name} {Tournament-Type}
```

Note :
- Arguments need to not have any ` ` and should be written with a `-`.
*This may evolve at some point*
- The brackets are not meant to be typed and might induce bugs.
**This needs to be resolved**

## Helping developing the Bot
If you want new feature to be added, please request them in the
[Issues](https://github.com/Spigushe/BotLigue/issues) section.

If you want to share your knowledge and help developing the Bot, you are welcome
to fork this project and send PR.
