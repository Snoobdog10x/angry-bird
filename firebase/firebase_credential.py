import firebase_admin
from firebase_admin import credentials
import os
cred = credentials.Certificate(f".{os.sep}cookie-netflix-48899-firebase-adminsdk-6bxuo-c48d262735.json")
firebase_admin.initialize_app(cred)