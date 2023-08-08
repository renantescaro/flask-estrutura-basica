
from typing import Dict, List
from main.database.models.database import Database, select
from main.database.models.user_group_model import UserGroup


class UserGroupRepository:
    @staticmethod
    def get_all() -> List[Dict]:
        user_groups:List[UserGroup] = Database().get_all(select(UserGroup))
        return [item.to_json() for item in user_groups]
