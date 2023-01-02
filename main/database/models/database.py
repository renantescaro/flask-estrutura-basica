from typing import Any
from sqlmodel import SQLModel, Session, create_engine, select
from main.utils.config import Config
from .pessoa_model import Pessoa

engine = create_engine(
    url=Config.get('DATABASE_URI'),
    echo=True
)
SQLModel.metadata.create_all(engine)

def run_query(statement) -> Any:
    with Session(engine) as session:
        return session.exec(statement).first()

def run_insert(object_model:Any):
    with Session(engine) as session:
        session.add(object_model)
        session.commit()
