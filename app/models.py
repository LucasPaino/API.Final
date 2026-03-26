from sqlalchemy import Column, Integer, String
from .database import Base


class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String, index=True)
    nivel = Column(Integer)
