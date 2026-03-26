from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_pokemons():
    response = client.get("/pokemons/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_pokemon():
    response = client.post(
        "/pokemons/",
        json={"nome": "Pikachu", "tipo": "Eletrico", "nivel": 10},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Pikachu"
    assert data["tipo"] == "Eletrico"
    assert data["nivel"] == 10
