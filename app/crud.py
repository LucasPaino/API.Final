from sqlalchemy.orm import Session
from . import models, schemas


def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(
        models.Pokemon.id == pokemon_id
    ).first()


def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(
        nome=pokemon.nome,
        tipo=pokemon.tipo,
        nivel=pokemon.nivel
    )
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon
