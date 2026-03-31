import os
import httpx
from dotenv import load_dotenv

load_dotenv()

POKEAPI_URL = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/pokemon")


def get_pokemon_from_api(pokemon_id: int) -> dict:
    url = f"{POKEAPI_URL}/{pokemon_id}"
    response = httpx.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    return {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "sprites": {
            "front_default": data["sprites"].get("front_default"),
            "back_default": data["sprites"].get("back_default"),
        },
    }


def list_pokemons_from_api(limit: int = 20, offset: int = 0) -> dict:
    url = f"{POKEAPI_URL}?limit={limit}&offset={offset}"
    response = httpx.get(url, timeout=10)
    response.raise_for_status()
    return response.json()