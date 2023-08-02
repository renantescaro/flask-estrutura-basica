from typing import Optional
from sqlmodel import Field, SQLModel


class UserGroup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_admin: bool

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_admin": self.is_admin,
        }
