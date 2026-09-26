import datetime


def timestamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def debug(msg: str):
    print(f"[DEBUG {timestamp()}] {msg}")


def info(msg: str):
    print(f"[INFO  {timestamp()}] {msg}")


def warn(msg: str):
    print(f"[WARN  {timestamp()}] {msg}")


def error(msg: str):
    print(f"[ERROR {timestamp()}] {msg}")
