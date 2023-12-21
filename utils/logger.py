from enum import Enum
from datetime import datetime, timezone
import logging


class LogLevel(Enum):
    WARNING = 0
    ERROR = 1
    INFO = 2


logging.basicConfig(level=logging.INFO)


def _build_message(message: str):
    return f" [{datetime.now()}] {message}"


def log_message(message: str, logLevel: LogLevel = LogLevel.INFO):
    if logLevel == LogLevel.INFO:
        logging.info(_build_message(message))
        return

    if logLevel == LogLevel.WARNING:
        logging.warning(_build_message(message))
        return

    if logLevel == LogLevel.ERROR:
        logging.error(_build_message(message))
        return
