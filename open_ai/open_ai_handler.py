import discord
import g4f
from local_redis import *
from shared import *

g4f.debug.logging = True
g4f.debug.check_version = False


class MessageAsking(metaclass=Singleton):
    def __init__(self):
        pass

    def insert_message(self, message_data: {}, user: discord.User):
        user_id = str(user.id)
        redis_instance.rpush(user_id, json.dumps(message_data))
        redis_instance.ltrim(user_id, -4, -1)

    def get_messages(self, user: discord.User):
        user_id = str(user.id)
        return [json.loads(data_json) for data_json in redis_instance.lrange(user_id, 0, 4)]


message_asked_instance = MessageAsking()


async def ask_gpt(message: str, user: discord.User):
    message_asked_instance.insert_message({"role": "user", "content": message}, user)
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4,
        messages=message_asked_instance.get_messages(user),
    )
    message_asked_instance.insert_message({"role": "assistant", "content": response}, user)
    return response
