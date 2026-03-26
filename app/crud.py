from sqlalchemy.orm import Session
from . import models, schemas


def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()


def get_pokemons(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(
        name=pokemon.name,
        height=pokemon.height,
        weight=pokemon.weight,
        types=",".join(pokemon.types),
        sprite_front=pokemon.sprites.front_default,
        sprite_back=pokemon.sprites.back_default,
    )
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon