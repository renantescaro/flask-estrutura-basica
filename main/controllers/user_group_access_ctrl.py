import json
from typing import List
from flask import Blueprint, request, render_template, redirect, url_for
from main.database.models.user_group_access_model import UserGroupAccess
from main.database.models.database import Database, select

bp = Blueprint(
    "user_group_access",
    __name__,
    url_prefix="/user/group/access",
    template_folder="templates",
)


class UserCtrl:
    @bp.route("/")
    def list():
        statement = select(UserGroupAccess)
        user_group_access: List[UserGroupAccess] = Database().get_all(statement)

        data = [item.to_json() for item in user_group_access]

        return render_template(
            "user_group_access/list.html",
            data=json.dumps(data),
        )

    @bp.route("/new", methods=["GET", "POST"])
    def new():
        if request.method == "GET":
            return render_template("user_group_access/new.html")

        user_group_access = UserGroupAccess(
            id_group=request.form.get("id_group"),
            route=request.form.get("route"),
            can_create=bool(request.form.get("can_create", False)),
            can_read=bool(request.form.get("can_read", False)),
            can_edit=bool(request.form.get("can_edit", False)),
            can_delete=bool(request.form.get("can_delete", False)),
        )
        Database().save(user_group_access)
        return redirect(url_for("user_group_access.list"))

    @bp.route("/edit/<id>", methods=["GET", "POST"])
    def edit(id):
        statement = select(UserGroupAccess).where(UserGroupAccess.id == id)
        user_group_access: UserGroupAccess = Database().get_one(statement)

        if request.method == "GET":
            return render_template(
                "user_group_access/edit.html",
                data=user_group_access.to_json(),
            )

        user_group_access.id_group = int(request.form.get("id_group"))
        user_group_access.route = request.form.get("route")
        user_group_access.can_create = bool(request.form.get("can_create", False))
        user_group_access.can_read = bool(request.form.get("can_read", False))
        user_group_access.can_edit = bool(request.form.get("can_edit", False))
        user_group_access.can_delete = bool(request.form.get("can_delete", False))

        Database().save(user_group_access)
        return redirect(url_for("user_group_access.list"))

    @bp.route("/delete/<id>", methods=["POST"])
    def delete(id):
        statement = select(UserGroupAccess).where(UserGroupAccess.id == id)
        user: UserGroupAccess = Database().get_one(statement)

        print("delete: ")
        print(user)

        Database().delete(user)

        return redirect(url_for("user_group_access.list"))
