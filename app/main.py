from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Pokemon API", version="0.1.0")

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

# Schema para criação/atualização de Pokémon local
class Pokemon(BaseModel):
    name: str
    height: int
    weight: int
    types: List[str]
    sprites: Dict[str, str]


# Armazenamento local simples para POST, PUT e DELETE
local_pokemons: Dict[int, Pokemon] = {}
next_id = 10000  # Começa em 10000 para não conflitar com PokeAPI


@app.get("/pokemons")
def list_pokemons(limit: int = 20, offset: int = 0):
    response = requests.get(f"{POKEAPI_URL}?limit={limit}&offset={offset}")
    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Error fetching from PokeAPI"
        )
    data = response.json()
    return {
        "data": data["results"],
        "pagination": {
            "total": data["count"],
            "limit": limit,
            "offset": offset,
            "next": data["next"],
            "previous": data["previous"],
        },
    }


@app.get("/pokemons/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    # Primeiro checa se está no cache local
    if pokemon_id in local_pokemons:
        pokemon = local_pokemons[pokemon_id]
        return {"id": pokemon_id, **pokemon.model_dump()}

    response = requests.get(f"{POKEAPI_URL}{pokemon_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    data = response.json()
    return {
        "name": data["name"],
        "id": data["id"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "sprites": {
            "front_default": data["sprites"]["front_default"],
            "back_default": data["sprites"]["back_default"],
        },
    }


@app.post("/pokemons", status_code=201)
def create_pokemon(pokemon: Pokemon):
    global next_id
    pokemon_dict = pokemon.model_dump()
    local_pokemons[next_id] = pokemon
    result = {"id": next_id, **pokemon_dict}
    next_id += 1
    return result


@app.put("/pokemons/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: Pokemon):
    if pokemon_id not in local_pokemons:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    updated = pokemon.model_dump()
    local_pokemons[pokemon_id] = pokemon
    return {"id": pokemon_id, **updated}


@app.delete("/pokemons/{pokemon_id}", status_code=204)
def delete_pokemon(pokemon_id: int):
    if pokemon_id not in local_pokemons:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    del local_pokemons[pokemon_id]