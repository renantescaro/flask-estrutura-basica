import json
import uuid
from typing import List
from flask import Blueprint, request, render_template, redirect, url_for
from main.database.models.api_keys_model import ApiKeys
from main.database.models.database import Database, select

bp = Blueprint(
    "api_keys",
    __name__,
    url_prefix="/apikeys",
    template_folder="templates",
)


class ApiKeysCtrl:
    @bp.route("/")
    def list():
        statement = select(ApiKeys)
        api_keys: List[ApiKeys] = Database().get_all(statement)
        data = [item.to_json() for item in api_keys]

        return render_template(
            "api_keys/list.html",
            data=json.dumps(data),
        )

    @bp.route("/new", methods=["GET", "POST"])
    def new():
        if request.method == "GET":
            key = str(uuid.uuid4())
            return render_template(
                "api_keys/new.html",
                key=key,
            )

        name = request.form.get("name")
        key = request.form.get("key")
        active = bool(request.form.get("active", False))

        print("key: ", key)

        if name and key:
            print("entrou")
            api_keys = ApiKeys(
                name=name,
                key=key,
                active=active,
            )
            Database().save(api_keys)
        return redirect(url_for("api_keys.list"))

    @bp.route("/edit/<id>", methods=["GET", "POST"])
    def edit(id):
        statement = select(ApiKeys).where(ApiKeys.id == id)
        api_key: ApiKeys = Database().get_one(statement)

        if request.method == "GET":
            return render_template(
                "api_keys/edit.html",
                data=api_key.to_json(),
            )

        api_key.name = request.form.get("name", api_key.name)
        api_key.active = bool(request.form.get("active", False))

        Database().save(api_key)
        return redirect(url_for("api_keys.list"))

    @bp.route("/delete/<id>", methods=["POST"])
    def delete(id):
        statement = select(ApiKeys).where(ApiKeys.id == id)
        user: ApiKeys = Database().get_one(statement)

        print("delete: ")
        print(user)

        Database().delete(user)

        return redirect(url_for("api_keys.list"))
