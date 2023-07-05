from typing import Any
from sqlmodel import SQLModel, Session, create_engine, select
from main.utils.enums.dot_env import DotEnvEnum
from main.utils.settings import Settings
from .person_model import Person

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

    def first(self) -> Any:
        return self._result.first()

    def all(self) -> Any:
        return self._result.all()

    def run_query(self, statement):
        self._result = Session(engine).exec(statement)
        return self

    def run_insert(self, object_model: Any):
        with Session(engine) as session:
            session.add(object_model)
            session.commit()
