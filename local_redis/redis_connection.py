import redis
from firebase import *

sep = os.sep
IP, PASSWORD = credential_instance.get_redis_credential()
redis_instance = redis.Redis(host=IP, port=6379, decode_responses=True, password=PASSWORD)

redis_instance.set("thanh", "hihi")
print(redis_instance.get("thanh"))
