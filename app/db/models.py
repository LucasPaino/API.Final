from sqlalchemy import Column, Integer, String, JSON
from app.db.base import Base


class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    height = Column(Integer)
    weight = Column(Integer)
    types = Column(JSON, default=[])
    sprites = Column(JSON, default={})