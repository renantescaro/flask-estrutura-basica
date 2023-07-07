from typing import Any
from sqlmodel import SQLModel, Session, create_engine, select
from main.utils.enums.dot_env import DotEnvEnum
from main.utils.settings import Settings
from .person_model import Person
from .person_addrees_model import PersonAddrees

engine = create_engine(
    url=Settings.get(
        DotEnvEnum.DATABASE_URI.value,
    ),
    echo=True,
)
SQLModel.metadata.create_all(engine)


class Database:
    def __init__(self) -> None:
        self._result = Any


    def get_one(self, statement):
        with Session(engine) as session:
            return session.exec(statement).first()
    
    
    def get_all(self, statement):
        with Session(engine) as session:
            return session.exec(statement).all()    


    def save(self, object_model: Any):
        with Session(engine) as session:
            session.add(object_model)
            session.commit()
