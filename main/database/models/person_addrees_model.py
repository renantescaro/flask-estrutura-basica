from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


class StateEnum(Enum):

    AMAPA = "AM"
    ACRE = "AC"
    ALAGOAS = "AL"
    

class PersonAddrees(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    street: str
    streetNumber: str
    neighborhood: str
    state: Optional[StateEnum] = None
    city: str
    zipCode: str
    complement: Optional[str] = None
    person_id: Optional[int] = Field(default=None, foreign_key="person.id")

