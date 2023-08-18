from typing import Optional
from sqlmodel import Field, SQLModel


class Routes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    method: str

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "method": self.method,
        }
