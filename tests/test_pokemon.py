from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_pokemons():
    response = client.get("/pokemons?limit=5&offset=0")
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert "pagination" in json_data
    assert len(json_data["data"]) <= 5


def test_get_pokemon():
    response = client.get("/pokemons/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "id" in data
    assert "types" in data
    assert "sprites" in data


def test_create_update_delete_pokemon():
    # Criação
    new_pokemon = {
        "name": "testmon",
        "height": 10,
        "weight": 50,
        "types": ["normal"],
        "sprites": {"front_default": "", "back_default": ""},
    }
    response = client.post("/pokemons", json=new_pokemon)
    assert response.status_code == 201
    created = response.json()
    pid = created["id"]
    assert created["name"] == "testmon"

    # Atualização
    updated_pokemon = {
        "name": "testmon-updated",
        "height": 12,
        "weight": 60,
        "types": ["normal"],
        "sprites": {"front_default": "", "back_default": ""},
    }
    response = client.put(f"/pokemons/{pid}", json=updated_pokemon)
    assert response.status_code == 200
    updated = response.json()
    assert updated["name"] == "testmon-updated"

    # Exclusão
    response = client.delete(f"/pokemons/{pid}")
    assert response.status_code == 204

    # Checagem de exclusão
    response = client.get(f"/pokemons/{pid}")
    assert response.status_code == 404