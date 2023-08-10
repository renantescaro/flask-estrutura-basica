from flask import Flask
from werkzeug.routing.rules import Rule
from main.database.models.database import Database, select
from main.database.models.routes_model import Routes


class AccessRouteSv:
    def register_routes(self, app: Flask) -> None:
        stm = select(Routes)
        routes_data = Database().get_all(stm)

        if not routes_data:
            for rule in app.url_map.iter_rules():
                self._register_route(rule)

    def _register_route(self, rule: Rule):
        if not rule.methods:
            return

        for method in rule.methods:
            if method in ["HEAD", "OPTIONS"]:
                continue

            route = Routes(name=str(rule), method=method)
            Database().save(route)
