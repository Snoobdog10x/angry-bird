from utils import *
from utils.credential_loader import *
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
        await error_command(parsed_args, message)


if __name__ == "__main__":
    TOKEN, GUILD_ID = load_credential()

    client.run(TOKEN)
