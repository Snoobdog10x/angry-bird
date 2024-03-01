import traceback
from firebase import *
from utils import *
from utils.command_handler import *
import discord
from utils.message_parser import parse_message

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            break


@client.event
async def on_message(message: discord.Message):
    if message.channel.id == 1212999388692090931:
        return

    if message.content.startswith("/ab"):
        message_content = message.content
        parsed_args = parse_message(message_content)
        log_message(f"{message.author.display_name} send a command {parsed_args}")

        if "cookie" in parsed_args:
            await cookie_command(message)
            return
        if "help" in parsed_args:
            await help_command(message)
            return
        if "gpt" in parsed_args:
            await ask_command(parsed_args, message)
            return
        if "client" in parsed_args:
            await client_command(message)
            return
        await error_command(parsed_args, message)


if __name__ == "__main__":
    try:
        TOKEN, GUILD_ID = credential_instance.get_discord_credential()
        client.run(TOKEN)
    except Exception:
        log_message(traceback.format_exc(), LogLevel.ERROR)
