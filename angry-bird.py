# bot.py
import os
from utils.command_handler import handle_command
from utils.logger import *
import discord

from utils.message_parser import parse_message

TOKEN = 'NzY1NTQ5NjAzODU2MTg3NDEz.G2DYdR.WcW8s-oSrBzn69dAZ5tknc8Sn3pbdcoumPqrmQ'
GUILD_ID = 858409477111152690
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            break


@client.event
async def on_message(message):
    message_content = message.content
    parsed_args = parse_message(message_content)
    log_message(f"{message.author.display_name} send a command {parsed_args}")
    embedVar = handle_command(parsed_args)
    await message.channel.send(embed=embedVar)

if __name__ == "__main__":
    client.run(TOKEN)
