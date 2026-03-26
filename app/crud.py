from sqlalchemy.orm import Session
from app import models, schemas

def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def get_pokemons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

def delete_pokemon(db: Session, pokemon_id: int):
    pokemon = get_pokemon(db, pokemon_id)
    if pokemon:
        db.delete(pokemon)
        db.commit()
    return pokemon