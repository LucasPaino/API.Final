from fastapi import APIRouter, HTTPException
from app.services.pokeapi import get_pokemons, get_pokemon_by_id

router = APIRouter()


@router.get("/pokemons")
def list_pokemons(limit: int = 20, offset: int = 0):
    data = get_pokemons(limit, offset)

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


@router.get("/pokemons/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    pokemon = get_pokemon_by_id(pokemon_id)

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    return {
        "name": pokemon["name"],
        "id": pokemon["id"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "types": [t["type"]["name"] for t in pokemon["types"]],
        "sprites": {
            "front_default": pokemon["sprites"]["front_default"],
            "back_default": pokemon["sprites"]["back_default"],
        },
    }
