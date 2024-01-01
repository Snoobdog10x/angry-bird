import os
import firebase_admin
from firebase_admin import credentials

if not firebase_admin._apps:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cookie-netflix-48899-firebase-adminsdk-6bxuo-c48d262735.json"
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://cookie-netflix-48899-default-rtdb.firebaseio.com/'})
