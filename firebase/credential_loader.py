from shared import Singleton
from firebase_admin import db
from firebase.init_firebase import *


class CredentialLoader(metaclass=Singleton):
    ref_credential = db.reference("/credentials")

    def __init__(self):
        self.redis_credential = {}
        self.discord_credential = {}

    def _init_credential_listener(self):
        data = self.ref_credential.get()
        self.redis_credential = data["redis"]
        self.discord_credential = data["discord"]

    def get_redis_credential(self):
        self._init_credential_listener()
        return self.redis_credential["IP"], self.redis_credential["PASSWORD"]

    def get_discord_credential(self):
        self._init_credential_listener()
        return self.discord_credential["TOKEN"], self.discord_credential["GUILD_ID"]


credential_instance = CredentialLoader()
