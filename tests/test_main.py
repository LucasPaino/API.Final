import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_pokemons():
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_pokemon_not_found():
    response = client.get("/pokemons/999999")
    assert response.status_code == 404