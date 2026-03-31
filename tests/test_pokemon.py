def test_get_pokemon(client, mocker):
    mocker.patch(
        "app.services.pokeapi.get_pokemon_from_api",
        return_value={"id": 25, "name": "pikachu", "height": 4, "weight": 60}
    )
    response = client.get("/pokemons/25")
    assert response.status_code == 200
    assert response.json()["name"] == "pikachu"