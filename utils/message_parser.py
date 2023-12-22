def parse_message(message: str):
    if message.startswith("/ab"):
        if "gpt" in message:
            ask_data = message.replace("/ab gpt ", "")
            asking_message = ask_data.strip()
            if len(asking_message) == 0:
                return ["/ab", "gpt"]
            return ["/ab", "gpt", asking_message]
        args = message.split(" ")
        return args
    return [message]
