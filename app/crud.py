from sqlalchemy.orm import Session
from app.db.models import Pokemon
from app import schemas


def get_pokemon(db: Session, pokemon_id: int):
    return db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()


def get_pokemons(db: Session, skip: int = 0, limit: int = 20):
    total = db.query(Pokemon).count()
    pokemons = db.query(Pokemon).offset(skip).limit(limit).all()
    return pokemons, total


def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = Pokemon(
        id=pokemon.id,
        name=pokemon.name,
        height=pokemon.height,
        weight=pokemon.weight,
        types=pokemon.types,
        sprites=pokemon.sprites.model_dump(),
    )
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon


def update_pokemon(db: Session, pokemon_id: int, data: schemas.PokemonUpdate):
    db_pokemon = get_pokemon(db, pokemon_id)
    if not db_pokemon:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_pokemon, key, value)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon


def delete_pokemon(db: Session, pokemon_id: int):
    db_pokemon = get_pokemon(db, pokemon_id)
    if not db_pokemon:
        return None
    db.delete(db_pokemon)
    db.commit()
    return db_pokemon