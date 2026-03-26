from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine, Base
from app.services.pokeapi import fetch_pokemon

app = FastAPI(title="Pokémon API")

# Cria tabelas
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/pokemons")
async def list_pokemons(limit: int = 10, offset: int = 0):
    data = []
    for i in range(offset + 1, offset + limit + 1):
        try:
            pokemon = await fetch_pokemon(i)
            data.append({
                "name": pokemon["name"],
                "id": pokemon["id"],
                "height": pokemon["height"],
                "weight": pokemon["weight"],
                "types": [t["type"]["name"] for t in pokemon["types"]],
                "sprites": pokemon["sprites"]
            })
        except:
            continue

    return {
        "data": data,
        "pagination": {
            "limit": limit,
            "offset": offset,
            "next": f"/pokemons?limit={limit}&offset={offset + limit}",
            "previous": None if offset == 0 else f"/pokemons?limit={limit}&offset={offset - limit}"
        }
    }

@app.get("/pokemons/{pokemon_id}")
async def get_pokemon_detail(pokemon_id: int):
    try:
        pokemon = await fetch_pokemon(pokemon_id)
        return {
            "name": pokemon["name"],
            "id": pokemon["id"],
            "height": pokemon["height"],
            "weight": pokemon["weight"],
            "types": [t["type"]["name"] for t in pokemon["types"]],
            "sprites": pokemon["sprites"]
        }
    except:
        raise HTTPException(status_code=404, detail="Pokemon not found")

@app.post("/pokemons", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    return crud.create_pokemon(db, pokemon)

@app.delete("/pokemons/{pokemon_id}")
def delete_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = crud.delete_pokemon(db, pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return {"ok": True}