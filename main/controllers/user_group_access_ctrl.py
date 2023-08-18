import json
from typing import Dict, List
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from main.database.models.user_group_access_model import UserGroupAccess
from main.database.models.database import Database, select
from main.database.repository.routes_repository import RoutesRepository
from main.database.repository.user_group_repository import UserGroupRepository
from main.database.repository.user_group_access_repository import (
    UserGroupAccessRepository,
)

bp = Blueprint(
    "user_group_access",
    __name__,
    url_prefix="/user/group/access",
    template_folder="templates",
)


class UserCtrl:
    @staticmethod
    @bp.route("/data/<id>")
    def get_route(id: int):
        all_routes = RoutesRepository.get_all()
        used_routes = UserGroupAccessRepository.get_by_id_group(id)

        final_data = []
        for route in all_routes:
            use_route = False
            if used_routes:
                for used_route in used_routes:
                    if used_route["id_route"] == route["id"]:
                        use_route = True

            final_data.append(
                {"id": route["id"], "name": route["name"], "use_route": use_route}
            )
        return final_data

    @bp.route("/")
    def list():
        data = UserGroupAccessRepository.get_all()
        return render_template(
            "user_group_access/new_page.html",
            data=json.dumps(data),
            routes=RoutesRepository.get_all(),
            user_groups=UserGroupRepository.get_all(),
        )

    @bp.route("/new", methods=["GET", "POST"])
    def new():
        if request.method == "GET":
            return render_template(
                "user_group_access/new.html",
                user_groups=UserGroupRepository.get_all(),
                routes=RoutesRepository.get_all(),
            )

        user_group_access = UserGroupAccess(
            id_group=int(request.form.get("id_group")),
            id_route=int(request.form.get("id_route")),
        )
        Database().save(user_group_access)
        return redirect(url_for("user_group_access.list"))

    @staticmethod
    @bp.route("/edit/<id>", methods=["GET", "POST"])
    def edit(id):
        user_group_access = UserGroupAccessRepository.get_by_id(int(id))

        if request.method == "GET":
            return render_template(
                "user_group_access/edit.html",
                data=user_group_access.to_json(),
                user_groups=UserGroupRepository.get_all(),
            )

        status = bool(request.json.get("status", False))
        if user_group_access and status is False:
            Database().delete(user_group_access)
            return "ok", 200

        if user_group_access is None and status is True:
            user_group_access = UserGroupAccess(
                id_group=int(request.json.get("idUserGroup")),
                id_route=int(request.json.get("idRoute")),
            )
            Database().save(user_group_access)
            return "ok", 200
        return "ok", 400

    @staticmethod
    @bp.route("/delete/<id>", methods=["POST"])
    def delete(id):
        user = UserGroupAccessRepository.get_by_id(int(id))

        print("delete: ")
        print(user)

        Database().delete(user)

        return redirect(url_for("user_group_access.list"))
