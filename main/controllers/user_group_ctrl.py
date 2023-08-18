import json
from typing import List
from flask import Blueprint, request, render_template, redirect, url_for
from main.database.models.user_group_model import UserGroup
from main.database.models.database import Database, select

bp = Blueprint(
    "user_group",
    __name__,
    url_prefix="/user/group",
    template_folder="templates",
)


class UserCtrl:
    @bp.route("/")
    def list():
        statement = select(UserGroup)
        users: List[UserGroup] = Database().get_all(statement)

        data = [user.to_json() for user in users]

        return render_template(
            "user_group/list.html",
            data=json.dumps(data),
        )

    @bp.route("/new", methods=["GET", "POST"])
    def new():
        if request.method == "GET":
            return render_template("user_group/new.html")

        name = request.form.get("name")
        is_admin = bool(request.form.get("isAdmin", False))

        # TODO: apenas usuário adm pode criar grupo adm

        user_group = UserGroup(
            name=name,
            is_admin=is_admin,
        )
        Database().save(user_group)
        return redirect(url_for("user_group.list"))

    @bp.route("/edit/<id>", methods=["GET", "POST"])
    def edit(id):
        statement = select(UserGroup).where(UserGroup.id == id)
        user: UserGroup = Database().get_one(statement)

        if request.method == "GET":
            return render_template(
                "user_group/edit.html",
                data=user.to_json(),
            )

        user.name = request.form.get("name")
        user.is_admin = bool(request.form.get("is_admin", False))

        Database().save(user)
        return redirect(url_for("user_group.list"))

    @bp.route("/delete/<id>", methods=["POST"])
    def delete(id):
        statement = select(UserGroup).where(UserGroup.id == id)
        user: UserGroup = Database().get_one(statement)

        print("delete: ")
        print(user)

        Database().delete(user)

        return redirect(url_for("user_group.list"))
