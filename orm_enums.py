from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Status(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    PENDING = "pending"
    COMPLETED = "completed"
