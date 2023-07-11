from flask import Blueprint, request, render_template, redirect, url_for, session
from main.database.models.user_model import User
from main.database.models.database import Database
from main.services.access_control_sv import AccessControlSv

bp = Blueprint(
    "login",
    __name__,
    template_folder="templates",
)


class loginCtrl:
    @bp.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            if username and password and AccessControlSv().login(username, password):
                return redirect(url_for("login.index"))

        if "user" in session:
            return redirect(url_for("login.index"))

        return render_template("login.html")

    @bp.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login.login"))

    @bp.route("/")
    def index():
        return render_template(
            "index.html",
            titulo="Inicial",
        )
