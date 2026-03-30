from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/pokemons/", response_model=list[schemas.Pokemon])
def read_pokemons(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return crud.get_pokemons(db=db, skip=skip, limit=limit)


@app.post("/pokemons/", response_model=schemas.Pokemon)
def create_pokemons(
    pokemon: schemas.PokemonCreate,
    db: Session = Depends(get_db),
):
    return crud.create_pokemon(db=db, pokemon=pokemon)