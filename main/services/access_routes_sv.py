from flask import Flask
from main.database.models.database import Database, select
from main.database.models.routes_model import Routes

class AccessRouteSv:
    def register_routes(self, app:Flask) -> None:
        stm = select(Routes)
        routes_data = Database().get_all(stm)

        if not routes_data:
            for rule in app.url_map.iter_rules():
                for method in rule.methods:
                    if str(method) not in ['HEAD', 'OPTIONS']:
                        route = Routes(name=str(rule), method=method)
                        Database().save(route)
