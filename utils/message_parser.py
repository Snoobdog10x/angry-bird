def parse_message(message: str):
    if message.startswith("/ab"):
        return message.split(" ")
    return [message]
