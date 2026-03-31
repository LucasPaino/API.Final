import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.dependencies import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

SQLALCHEMY_TEST_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

MOCK_POKEMON = {
    "id": 25,
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "types": ["electric"],
    "sprites": {
        "front_default": "https://raw.githubusercontent.com/front.png",
        "back_default": "https://raw.githubusercontent.com/back.png",
    },
}


@pytest.fixture(autouse=True)
def setup_tables():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_create_pokemon(client):
    response = client.post("/pokemons", json=MOCK_POKEMON)
    assert response.status_code == 201
    assert response.json()["name"] == "pikachu"


def test_create_pokemon_duplicate(client):
    client.post("/pokemons", json=MOCK_POKEMON)
    response = client.post("/pokemons", json=MOCK_POKEMON)
    assert response.status_code == 400


def test_get_pokemon_from_db(client):
    client.post("/pokemons", json=MOCK_POKEMON)
    response = client.get("/pokemons/25")
    assert response.status_code == 200
    assert response.json()["name"] == "pikachu"


def test_get_pokemon_from_pokeapi(client, mocker):
    mocker.patch(
        "app.routers.pokemon.get_pokemon_from_api",
        return_value=MOCK_POKEMON,
    )
    response = client.get("/pokemons/25")
    assert response.status_code == 200
    assert response.json()["name"] == "pikachu"


def test_get_pokemon_not_found(client, mocker):
    mocker.patch(
        "app.routers.pokemon.get_pokemon_from_api",
        side_effect=Exception("Not found"),
    )
    response = client.get("/pokemons/99999")
    assert response.status_code == 404


def test_list_pokemons_empty_fetches_api(client, mocker):
    mocker.patch(
        "app.routers.pokemon.list_pokemons_from_api",
        return_value={
            "count": 1,
            "results": [{"name": "pikachu", "url": "https://pokeapi.co/api/v2/pokemon/25/"}],
        },
    )
    mocker.patch(
        "app.routers.pokemon.get_pokemon_from_api",
        return_value=MOCK_POKEMON,
    )
    response = client.get("/pokemons?limit=20&offset=0")
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert "pagination" in body


def test_list_pokemons_pagination_meta(client, mocker):
    mocker.patch(
        "app.routers.pokemon.list_pokemons_from_api",
        return_value={
            "count": 100,
            "results": [{"name": "pikachu", "url": "https://pokeapi.co/api/v2/pokemon/25/"}],
        },
    )
    mocker.patch(
        "app.routers.pokemon.get_pokemon_from_api",
        return_value=MOCK_POKEMON,
    )
    response = client.get("/pokemons?limit=20&offset=0")
    pagination = response.json()["pagination"]
    assert pagination["total"] == 100
    assert pagination["next"] == "/pokemons?limit=20&offset=20"
    assert pagination["previous"] is None


def test_list_pokemons_previous_link(client, mocker):
    client.post("/pokemons", json=MOCK_POKEMON)
    mocker.patch(
        "app.routers.pokemon.list_pokemons_from_api",
        return_value={"count": 100},
    )
    response = client.get("/pokemons?limit=20&offset=20")
    pagination = response.json()["pagination"]
    assert pagination["previous"] == "/pokemons?limit=20&offset=0"


def test_update_pokemon(client):
    client.post("/pokemons", json=MOCK_POKEMON)
    response = client.put("/pokemons/25", json={"weight": 99})
    assert response.status_code == 200
    assert response.json()["weight"] == 99


def test_update_pokemon_not_found(client):
    response = client.put("/pokemons/99999", json={"weight": 99})
    assert response.status_code == 404


def test_delete_pokemon(client):
    client.post("/pokemons", json=MOCK_POKEMON)
    response = client.delete("/pokemons/25")
    assert response.status_code == 204


def test_delete_pokemon_not_found(client):
    response = client.delete("/pokemons/99999")
    assert response.status_code == 404