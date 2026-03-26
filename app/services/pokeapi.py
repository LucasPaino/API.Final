import httpx

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

async def fetch_pokemon(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{id}")
        response.raise_for_status()
        return response.json()