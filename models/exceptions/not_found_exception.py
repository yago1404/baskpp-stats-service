from models.exceptions.app_exception import AppException


class AppNotFound(AppException):
    def __init__(self, message: str):
        super().__init__(message, 404)