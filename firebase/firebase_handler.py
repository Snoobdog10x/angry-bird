from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
db = firestore.client()
def get_cookie():
    docs = db.collection("netflix_cookie").where(filter=FieldFilter("is_alive", "==", True)).limit(1).get()
    return docs[0].to_dict()
def mark_cookie_picked():
    pass