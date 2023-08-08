from typing import Dict, List
from main.database.models.database import Database, select
from main.database.models.routes_model import Routes


class RoutesRepository:
    @staticmethod
    def get_all():
        statement = select(Routes)
        user_group_access: List[Routes] = Database().get_all(statement)
        return [item.to_json() for item in user_group_access]
