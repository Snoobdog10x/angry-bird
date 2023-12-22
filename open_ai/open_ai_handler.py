import discord
import g4f

g4f.debug.logging = True
g4f.debug.check_version = False


class MessageAsking(object):
    def __init__(self):
        self.asked_conversation = {}
        pass

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MessageAsking, cls).__new__(cls)
        return cls.instance

    def insert_message(self, message_data: {}, user: discord.User):
        user_id = str(user.id)
        if user_id not in self.asked_conversation:
            self.asked_conversation[user_id] = [message_data]
            return
        self.asked_conversation[user_id].append(message_data)

    def get_messages(self, user: discord.User):
        user_id = str(user.id)
        return self.asked_conversation[user_id]

    def clear_conversation(self, user: discord.User):
        user_id = str(user.id)
        self.asked_conversation[user_id].clear()


message_asked_instance = MessageAsking()


async def ask_gpt(message: str, user: discord.User):
    message_asked_instance.insert_message({"role": "user", "content": message}, user)
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4,
        messages=message_asked_instance.get_messages(user),
        provider=g4f.Provider.Bing,
    )
    return response
