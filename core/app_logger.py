from abc import ABC

class AppLogger(ABC):
    @staticmethod
    def info(message: str):
        print(f"\033[32m{message}\033[0m")

    @staticmethod
    def error(message: str):
        print(f"\033[31m{message}\033[0m")

    @staticmethod
    def warning(message: str):
        print(f"\033[33m{message}\033[0m")