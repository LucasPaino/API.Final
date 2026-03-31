from fastapi import FastAPI
from app.routers import pokemon
from app.db.base import Base
from app.db.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pokémon API",
    description="API RESTful que consome dados da PokéAPI com persistência via SQLAlchemy.",
    version="1.0.0",
)

app.include_router(pokemon.router)