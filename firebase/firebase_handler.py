import json
from datetime import datetime, timezone
import os
import firebase_admin
import discord
from utils import *
from firebase_admin import firestore
from firebase_admin import credentials

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"cookie-netflix-48899-firebase-adminsdk-6bxuo-c48d262735.json"
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()
async_db = firestore.firestore.AsyncClient()


class FirebaseHandler(object):
    def __init__(self):
        self.latest_cookie = None
        self.watched_snapshot = None
        self.listen_snapshot()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FirebaseHandler, cls).__new__(cls)
        return cls.instance

    def _on_snapshot(self, doc_snapshot, changes, read_time):
        for doc in doc_snapshot:
            self.set_latest_cookie(doc)
            return

    def listen_snapshot(self):
        if self.watched_snapshot is not None:
            return

        self.watched_snapshot = db.collection(COOKIE_COLLECTION).where("is_alive", "==", True).limit(1).on_snapshot(
            self._on_snapshot
        )

    def cancel_watch(self):
        if self.watched_snapshot is None:
            return
        self.watched_snapshot.unsubscribe()

    def set_latest_cookie(self, doc):
        self.latest_cookie = doc

    def get_latest_cookie(self):
        return self.latest_cookie

    def get_latest_cookie_json(self):
        cookie = self.get_latest_cookie()
        if cookie is None:
            return "[]"

        return json.dumps(cookie.to_dict()["cookies"], indent=2)

    async def mark_cookie_dead(self, user: discord.User):
        log_message(f"{user.id} {user.display_name} marked cookie dead")
        await async_db.collection(COOKIE_COLLECTION).document(self.latest_cookie.id).update(
            {
                'is_alive': False
            }
        )

    async def mark_cookie_alive(self, user: discord.User):
        log_message(f"{user.id} {user.display_name} marked cookie alive")
        await async_db.collection(COOKIE_COLLECTION).document(self.latest_cookie.id).update(
            {
                'is_alive': True
            }
        )

    async def mark_cookie_picked(self, user: discord.User):
        log_message(f"{user.id} {user.display_name} marked cookie picked")
        await async_db.collection(COOKIE_COLLECTION).document(self.latest_cookie.id).update(
            {
                'picked_days': firestore.ArrayUnion([datetime.now(timezone.utc)])
            }
        )


COOKIE_COLLECTION = "netflix_cookie"
