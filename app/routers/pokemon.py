from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app import crud, schemas

router = APIRouter()

@router.get("/pokemons/{pokemon_id}", response_model=schemas.PokemonResponse)
def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = crud.get_pokemon(db, pokemon_id)
    return pokemon