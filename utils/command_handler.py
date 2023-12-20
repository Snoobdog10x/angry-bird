import discord

help_data = [
    ("Angry Bird Command:", "", False),
    ("/ab help", "Show all AB command", False),
    ("/ab cookie", "Request a new cookie [In Progress]", False),
    ("/ab music <music name>", "Playing a music [Pending, cause of big blocker]", False),
]


def _build_embed(field=[], title: str = "", description: str = "", color=0x00ff00):
    embedVar = discord.Embed(title=title, description=description, color=color)
    for value in field:
        key, value, inline = value
        embedVar.add_field(name=key, value=value, inline=inline)
    return embedVar


def _help_command():
    return _build_embed(
        help_data,
        title="Toàn bộ command của tao",
        description="Lười dịch quá đọc tiếng anh đi"
    )


def _error_command(command_args: []):
    return _build_embed(
        help_data,
        color=0xff0000,
        title="Sai rồi",
        description=f"Tao không tìm thấy command {' '.join(command_args)}, xài mấy cái sau đây đi!",
    )


def _cookie_command():
    return _build_embed(
        title="Cho mày cookie nè",
        description="Nhớ cảm ơn tao nha"
    )


def handle_command(command_args: []):
    if "cookie" in command_args:
        return _cookie_command()
    if "help" in command_args:
        return _help_command()
    return _error_command(command_args)
