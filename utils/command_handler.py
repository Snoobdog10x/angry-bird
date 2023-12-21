import io

import discord

from firebase.firebase_handler import FirebaseHandler
from utils.view import ButtonView

help_data = [
    ("Angry Bird Command:", "", False),
    ("/ab help", "Show all AB command", False),
    ("/ab cookie", "Request a new cookie [In Progress]", False),
    ("/ab music <music name>", "Playing a music [Pending, cause of big blocker]", False),
]
firebase_instance = FirebaseHandler()


def _build_embed(field=[], title: str = "", description: str = "", color=0x00ff00):
    embedVar = discord.Embed(title=title, description=description, color=color)
    for value in field:
        key, value, inline = value
        embedVar.add_field(name=key, value=value, inline=inline)
    return embedVar


async def help_command(message: discord.Message):
    embed = _build_embed(
        help_data,
        title="Toàn bộ command của tao",
        description="Lười dịch quá đọc tiếng anh đi"
    )
    await message.channel.send(embed=embed)


async def error_command(command_args: [], message: discord.Message):
    embed = _build_embed(
        help_data,
        color=0xff0000,
        title="Sai rồi",
        description=f"Tao không tìm thấy command {' '.join(command_args)}, xài mấy cái sau đây đi!",
    )
    await message.channel.send(embed=embed)


async def cookie_command(message: discord.Message):
    cookie_json = firebase_instance.get_latest_cookie_json()
    f = io.StringIO(cookie_json)
    embed = _build_embed(
        title="Cho mày cookie nè",
        description="Nhớ cảm ơn tao nha"
    )

    await message.channel.send(embed=embed, file=discord.File(f, filename="cookie.json"),
                               view=ButtonView(firebase_instance=firebase_instance))