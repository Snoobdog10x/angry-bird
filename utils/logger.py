from enum import Enum
class LogLevel(Enum):
    WARNING = 0
    ERROR = 1
    INFO = 2

def log_message(message:str, logLevel: LogLevel = LogLevel.INFO):
    print(f"[{logLevel.name}]: {message}")