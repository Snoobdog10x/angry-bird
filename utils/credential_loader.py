import json
import os


def load_credential():
    sep = os.sep
    f = open(f".{sep}discord_credential.json")
    data = json.load(f)
    TOKEN = data["TOKEN"]
    GUILD_ID = data["GUILD_ID"]
    f.close()
    return TOKEN, GUILD_ID
