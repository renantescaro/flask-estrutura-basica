from datetime import date
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


class GeneroEnum(Enum):
    MASCULINO='masculino'
    FEMININO='feminino'
    OUTRO='outro'

class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    pronome: str
    peso: Optional[float] = None
    genero: Optional[GeneroEnum] = None
    data_nascimento: Optional[date]
