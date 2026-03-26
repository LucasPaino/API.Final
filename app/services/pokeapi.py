import httpx

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(nome: str):
    response = httpx.get(f"{BASE_URL}{nome.lower()}")
    if response.status_code != 200:
        return None
    return response.json()
