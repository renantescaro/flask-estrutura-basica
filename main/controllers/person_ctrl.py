from typing import List
from flask import jsonify, Blueprint, abort, request
from main.database.models.person_model import Person
from main.database.models.database import Database, select

bp = Blueprint(
    "person",
    __name__,
    template_folder="templates",
)


class PersonCtrl:
    @bp.route("/person/<name>", methods=["GET"])
    def get_one_person(name):
        statement = select(Person).where(Person.name == name)
        person: Person = Database().run_query(statement).first()
        if person is not None:
            return jsonify(
                {
                    "name": person.name,
                    "gender": person.gender.value if person.gender else "",
                }
            )
        return abort(404)

    @bp.route("/person", methods=["GET"])
    def get_person():
        statement = select(Person)
        persons = Database().run_query(statement).all()

        return jsonify(
            [
                {
                    "name": person.name,
                    "gender": person.gender.value,
                }
                for person in persons
            ]
        )

    @bp.route("/person", methods=["POST"])
    def new_person():
        try:
            print(request.json)
            if data := request.json:
                person = Person(
                    name=data["name"],
                    pronoun=data["pronoun"],
                    weight=data["weight"],
                    gender=data["gender"],
                    birth_date=data["birth_date"],
                )
                Database().run_insert(person)
                return jsonify({})

        except Exception as e:
            print(e)

        return abort(400)
