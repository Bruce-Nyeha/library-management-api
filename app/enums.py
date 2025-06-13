import enum

class RoleEnum(str, enum.Enum):
    ADMIN = "admin"
    STAFF = "Staff"
    USER = "user"
    