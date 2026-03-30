from fastapi import status


def test_create_and_read_pokemons(client):
    pokemon_data = {"name": "Pikachu", "type": "Electric"}

    response = client.post("/pokemons/", json=pokemon_data)
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data["name"] == "Pikachu"
    assert data["type"] == "Electric"
    assert "id" in data

    response = client.get("/pokemons/")
    assert response.status_code == status.HTTP_200_OK

    pokemons = response.json()
    assert any(p["name"] == "Pikachu" for p in pokemons)