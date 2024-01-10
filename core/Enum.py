from enum import Enum, unique


@unique
class Role(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class StatusCode(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    INTERNAL_SERVER_ERROR = 500


class Message(Enum):
    CREATE_SUCCESS = "Create successfully!!!"
    UPDATE_SUCCESS = "Updated successfully!!!"
    DELETED_SUCCESS = "Deleted successfully!!!"
    INTERNAL_SERVER_ERROR = "Internal Server Error!!!"
    DATA_NOT_NULL = "Data can't null!!!"

    # Account

    USERNAME_EXIST = "Username exist!!!"
    PASSWORD_WEAK = "Password so weak!!!"
    PASSWORD_NOT_MATCH = "Password did not match!!!"
    NOT_FOUND_ACCOUNT = "Not Found Account!!!"
