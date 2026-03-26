from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pokémon API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/pokemons", response_model=list[schemas.Pokemon])
def read_pokemons(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    try:
        return crud.get_pokemons(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/pokemons/{pokemon_id}", response_model=schemas.Pokemon)
def read_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = crud.get_pokemon(db, pokemon_id=pokemon_id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokémon not found")
    return pokemon