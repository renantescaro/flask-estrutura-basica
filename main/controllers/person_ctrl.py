from typing import List
from flask import jsonify, Blueprint, abort, request
from main.database.models.person_model import Person
from main.database.models.person_addrees_model import PersonAddrees
from main.database.models.database import Database, select

bp = Blueprint(
    "person",
    __name__,
    template_folder="templates",
)


class PersonCtrl:
    @bp.route("/person/<id>", methods=["GET"])
    def get_one_person(id):
        statement_person = select(Person).where(Person.id == id)
        statement_person_addrees = select(PersonAddrees).where(PersonAddrees.person_id == Person.id)
        person: Person = Database().run_query(statement_person).first()
        person_addrees: PersonAddrees = Database().run_query(statement_person_addrees).first()
        if person is not None and person_addrees is not None:
            return jsonify(
                {
                    "name": person.name,
                    "gender": person.gender.value if person.gender else "",
                    "birth_Date": person.birth_date,
                    "addrees": {
                        "street": person_addrees.street,
                        "streetNumber": person_addrees.streetNumber,
                        "neighborhood": person_addrees.neighborhood,
                        "state": person_addrees.state.value if person_addrees.state else "",
                        "city": person_addrees.city,
                        "zipCode": person_addrees.zipCode,
                        
                    }
                    
                }
            )
        else:
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
    