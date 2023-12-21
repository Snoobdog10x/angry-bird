import asyncio

import discord


class ButtonView(discord.ui.View):
    def __init__(self, firebase_instance):
        self.firebase_instance = firebase_instance
        super().__init__()

    @discord.ui.button(label="Alive", style=discord.ButtonStyle.green)
    async def alive_button(self, interact: discord.Interaction, button):
        user = interact.user
        await asyncio.gather(
            self.firebase_instance.mark_cookie_alive(user),
            self.firebase_instance.mark_cookie_picked(user),
            interact.response.send_message("Cảm ơn m đã báo là nó còn sống")
        )

    @discord.ui.button(label="Dead", style=discord.ButtonStyle.red)
    async def dead_button(self, interact: discord.Interaction, button):
        user = interact.user
        await asyncio.gather(
            self.firebase_instance.mark_cookie_dead(user),
            self.firebase_instance.mark_cookie_picked(user),
            interact.response.send_message("Cảm ơn m đã báo là nó chết rồi")
        )
