from firebase.init_firebase import *
from firebase_admin import db


def get_active_urls() -> {}:
    client_mapping = {
        "9090": "Cockpit",
        "80": "Casaos"
    }
    data = db.reference("/public_urls").get()
    default_return = {}
    if data is None:
        return default_return
    if "thanhnguyen" in data:
        data.pop("thanhnguyen")

    actually_data = {}
    for hostname, hostname_client_map in data.items():
        for port, urls in hostname_client_map.items():
            if port not in client_mapping:
                continue
            mapped_client = client_mapping[port]
            actually_data[mapped_client] = urls
    return actually_data
