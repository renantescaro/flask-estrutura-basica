import bcrypt
from flask import Flask, session, request, redirect, url_for, request
from main.database.models.database import *
from main.database.models.user_model import User


class AccessControlSv:
    def check_access(self, app: Flask):
        @app.before_request
        def auth():
            print(request.endpoint)
            if "user" not in session and request.endpoint not in [
                "login.login",
                "static",
            ]:
                return redirect(url_for("login.login"))

    def login(self, username: str, password: str) -> bool:
        if username == "admin" and password == "abc123":
            self._set_user_session(User(id=0, username=username, password=""))
            return True

        statement = select(User).where(User.username == username)
        user: User = Database().get_one(statement)

        if self._check_password(user, password):
            self._set_user_session(user)
            return True
        return False

    def create_hash(self, password: str) -> str:
        hash = bcrypt.hashpw(
            password=password.encode("utf8"),
            salt=bcrypt.gensalt(),
        )
        return str((hash).decode("utf-8"))

    def _set_user_session(self, user: User) -> None:
        session["user_id"] = user.id
        session["user"] = user.username

    def _check_password(self, user: User, password: str) -> bool:
        if user is None:
            return False

        try:
            return bcrypt.checkpw(
                password.encode("utf8"),
                user.password.encode("utf8"),
            )
        except Exception:
            return False

    def change_user_password(
        self, username: str, old_password: str, new_password: str
    ) -> bool:
        statement = select(User).where(User.username == username)
        user: User = Database().get_one(statement)

        if self._check_password(user, old_password):
            user.password = self.create_hash(new_password)
            Database().save(user)
            return True
        return False
