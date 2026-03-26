import os
os.environ["TESTING"] = "1"

from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

def test_get_pokemon():
    with patch("app.services.pokeapi.fetch_pokemon") as mock:
        mock.return_value = {
            "name": "pikachu",
            "id": 25,
            "height": 4,
            "weight": 60,
            "types": [{"type": {"name": "electric"}}],
            "sprites": {}
        }

        response = client.get("/pokemons/25")
        assert response.status_code == 200
        assert response.json()["name"] == "pikachu"

def test_get_nonexistent_pokemon():
    with patch("app.services.pokeapi.fetch_pokemon") as mock:
        mock.side_effect = Exception("Not found")
        response = client.get("/pokemons/99999")
        assert response.status_code == 404