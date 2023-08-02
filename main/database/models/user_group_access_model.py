from typing import Optional
from sqlmodel import Field, SQLModel


class UserGroupAccess(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_group: int
    route: str
    can_create: bool
    can_read: bool
    can_edit: bool
    can_delete: bool

    def to_json(self):
        return {
            "id": self.id,
            "id_group": self.id_group,
            "route": self.route,
            "can_create": self.can_create,
            "can_read": self.can_read,
            "can_edit": self.can_edit,
            "can_delete": self.can_delete,
        }
