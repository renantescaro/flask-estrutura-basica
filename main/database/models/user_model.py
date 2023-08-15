from typing import Optional
from sqlmodel import Field, SQLModel
from main.database.models.user_group_model import UserGroup


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    email: Optional[str] = ""
    id_user_group: int = Field(foreign_key=UserGroup.id)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "id_user_group": self.id_user_group,
        }
