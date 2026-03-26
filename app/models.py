from sqlalchemy import Column, Integer, String
from .database import Base


class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    types = Column(String)
    sprite_front = Column(String)
    sprite_back = Column(String)