import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def get_pokemons(limit=20, offset=0):
    response = requests.get(f"{BASE_URL}?limit={limit}&offset={offset}")
    response.raise_for_status()
    return response.json()


def get_pokemon_by_id(pokemon_id: int):
    response = requests.get(f"{BASE_URL}/{pokemon_id}")
    if response.status_code != 200:
        return None
    return response.json()
