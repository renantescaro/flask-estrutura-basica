from typing import Optional
from sqlmodel import Field, SQLModel


class ApiKeys(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    key: str
    active: bool

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "key": self.key,
            "active": self.active,
        }
