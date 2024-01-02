import init_firebase
from firebase import get_active_urls
from firebase.credential_loader import CredentialLoader


def main():
    test = get_active_urls()
    print(test)


main()
