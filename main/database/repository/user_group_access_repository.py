from typing import Dict, List
from main.database.models.database import Database, select
from main.database.models.user_group_access_model import UserGroupAccess

class UserGroupAccessRepository:
    @staticmethod
    def get_by_id(id:int) -> UserGroupAccess:
        statement = select(UserGroupAccess).where(UserGroupAccess.id == id)
        user: UserGroupAccess = Database().get_one(statement)
        return user

    @staticmethod
    def get_all() -> List[Dict]:
        statement = select(UserGroupAccess)
        user_group_access: List[UserGroupAccess] = Database().get_all(statement)
        return [item.to_json() for item in user_group_access]
