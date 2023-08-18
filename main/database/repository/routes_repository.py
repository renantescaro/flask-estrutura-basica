from typing import Dict, List
from main.database.models.database import Database, select
from main.database.models.routes_model import Routes


class RoutesRepository:
    @staticmethod
    def get_all():
        statement = select(Routes)
        routes: List[Routes] = Database().get_all(statement)
        return [item.to_dict() for item in routes]

    @staticmethod
    def get_by_id(id: int):
        statement = select(Routes).where(Routes.id == id)
        route: Routes = Database().get_one(statement)
        return route.to_dict()
