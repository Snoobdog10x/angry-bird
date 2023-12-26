import json

import redis
import os

sep = os.sep
f = open(f".{sep}redis_credential.json")
data = json.load(f)
PASSWORD = data["PASSWORD"]
f.close()
redis_instance = redis.Redis(host='192.168.2.19', port=6379, decode_responses=True, password=PASSWORD)
