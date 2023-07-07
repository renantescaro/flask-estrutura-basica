from datetime import date
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


class GenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    pronoun: str
    weight: Optional[float] = None
    gender: Optional[GenderEnum] = None
    birth_date: Optional[date]
   