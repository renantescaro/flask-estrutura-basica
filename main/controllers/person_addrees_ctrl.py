from typing import List
from flask import jsonify, Blueprint, abort, request
from main.database.models.person_addrees_model import PersonAddrees
from main.database.models.database import Database, select

bp = Blueprint(
    "person/addrees",
    __name__,
    template_folder="templates",
)

class PersonAddreesCtrl:
    @bp.route("/person/addrees", methods=["POST"])
    def new_person_addrees():
        try:
            print(request.json)
            if data := request.json:
                addrees = PersonAddrees(
                    street=data["street"],
                    streetNumber=data["streetNumber"],
                    neighborhood=data["neighborhood"],
                    state=data["state"],
                    city=data["city"],
                    zipCode=data["zipCode"],
                    complement=data["complement"],
                    person_id=data["person_id"]
                )
                Database().save(addrees)
                return jsonify({})

        except Exception as e:
            print(e)

        return abort(400)