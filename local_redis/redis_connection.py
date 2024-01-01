import json

import redis
import os

sep = os.sep
f = open(f"..{sep}redis_credential.json")
data = json.load(f)
PASSWORD = data["PASSWORD"]
IP = data["IP"]
f.close()
redis_instance = redis.Redis(host=IP, port=6379, decode_responses=True, password=PASSWORD)
