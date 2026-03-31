from sqlalchemy.orm import Session
from app.db.models import Pokemon

def get_pokemon(db: Session, pokemon_id: int):
    return db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()