import json
import uuid
from typing import List
from flask import Blueprint, request, render_template, redirect, url_for


bp = Blueprint(
    "ping_api",
    __name__,
    url_prefix="/api/ping",
)


class PingApi:
    @bp.route("/")
    def ping():
        return "pong", 200
