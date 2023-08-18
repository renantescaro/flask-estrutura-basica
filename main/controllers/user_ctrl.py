import json
from typing import List
from flask import Blueprint, request, render_template, redirect, url_for
from main.database.models.user_model import User
from main.database.models.database import Database, select
from main.services.access_control_sv import AccessControlSv
from main.database.repository.user_group_repository import (
    UserGroupRepository,
)

bp = Blueprint(
    "user",
    __name__,
    url_prefix="/user",
    template_folder="templates",
)


class UserCtrl:
    @bp.route("/")
    def list():
        statement = select(User)
        users: List[User] = Database().get_all(statement)

        data = [user.to_json() for user in users]

        return render_template(
            "user/list.html",
            data=json.dumps(data),
        )

    @bp.route("/new", methods=["GET", "POST"])
    def new():
        if request.method == "GET":
            return render_template(
                "user/new.html",
                user_groups=UserGroupRepository.get_all(),
            )

        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        id_user_group = int(request.form.get("id_user_group"))

        if username and password:
            hash_password = AccessControlSv().create_hash(password)
            user = User(
                username=username,
                email=email,
                password=hash_password,
                id_user_group=id_user_group,
            )
            Database().save(user)
        return redirect(url_for("user.list"))

    @bp.route("/edit/<id>", methods=["GET", "POST"])
    def edit(id):
        statement = select(User).where(User.id == id)
        user: User = Database().get_one(statement)

        if request.method == "GET":
            return render_template(
                "user/edit.html",
                data=user.to_json(),
                user_groups=UserGroupRepository.get_all(),
            )

        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")

        user.email = email
        if username:
            user.username = username

        if password and user.password != password:
            user.password = AccessControlSv().create_hash(password)

        Database().save(user)
        return redirect(url_for("user.list"))

    @bp.route("/delete/<id>", methods=["POST"])
    def delete(id):
        statement = select(User).where(User.id == id)
        user: User = Database().get_one(statement)

        print("delete: ")
        print(user)

        Database().delete(user)

        return redirect(url_for("user.list"))
