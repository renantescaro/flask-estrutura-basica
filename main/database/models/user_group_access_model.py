from typing import Optional
from sqlmodel import Field, SQLModel
from main.database.models.routes_model import Routes
from main.database.models.user_group_model import UserGroup


class UserGroupAccess(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_group: int = Field(foreign_key=UserGroup.id)
    id_route: int = Field(foreign_key=Routes.id)

    def to_json(self):
        return {
            "id": self.id,
            "id_group": self.id_group,
            "id_route": self.id_route,
        }
