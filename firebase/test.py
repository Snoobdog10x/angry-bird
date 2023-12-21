from firebase_handler import FirebaseHandler

import time


def main():
    instant = FirebaseHandler()
    while True:
        cookie = instant.get_latest_cookie()
        if cookie is None:
            continue
        print(cookie.id)
        time.sleep(2)


main()
