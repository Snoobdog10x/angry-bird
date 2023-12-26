import asyncio

import discord


class ButtonView(discord.ui.View):
    def __init__(self, firebase_instance, doc):
        self.doc = doc
        self.firebase_instance = firebase_instance
        super().__init__()

    async def _disable_children(self, interact: discord.Interaction):
        for child in self.children:
            child.disabled = True
        await interact.message.edit(view=self)

    async def _update_after_mark_message(self, interact: discord.Interaction, is_alive: bool):
        user = interact.user
        result = "SỐNG!"
        color = 0x00ff00
        if not is_alive:
            result = "CHẾT!"
            color = 0xff0000
        interact.message.embeds.append(
            discord.Embed(
                title=f"Cảm ơn mày, {user.display_name}",
                description=f"Đã đánh dấu cookie {result}",
                color=color
            )
        )
        await interact.response.edit_message(embeds=interact.message.embeds)

    @discord.ui.button(label="Alive", style=discord.ButtonStyle.green)
    async def alive_button(self, interact: discord.Interaction, button):
        user = interact.user
        await asyncio.gather(
            self._disable_children(interact),
            self.firebase_instance.mark_cookie_alive(user, self.doc),
            self.firebase_instance.mark_cookie_picked(user, self.doc),
            self._update_after_mark_message(interact, True)
        )

    @discord.ui.button(label="Dead", style=discord.ButtonStyle.red)
    async def dead_button(self, interact: discord.Interaction, button):
        user = interact.user
        await asyncio.gather(
            self._disable_children(interact),
            self.firebase_instance.mark_cookie_dead(user, self.doc),
            self.firebase_instance.mark_cookie_picked(user, self.doc),
            self._update_after_mark_message(interact, False)
        )
