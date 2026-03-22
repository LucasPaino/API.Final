# Pokémon API

API simples para listar pokémons e obter detalhes de cada pokémon usando a [PokeAPI](https://pokeapi.co/).

---

## 📦 Tecnologias

- Python 3.13
- FastAPI
- Uvicorn
- Requests
- Pytest (com cobertura)
- Black & Flake8 para formatação e linting
- GitHub para versionamento

---

## 🚀 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/LucasPaino/API.Final.git
cd API.Final

Crie e ative o ambiente virtual:

Windows (PowerShell):

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Windows (CMD):

python -m venv .venv
.\.venv\Scripts\activate

Linux / MacOS:

python3 -m venv .venv
source .venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Rodando a API

uvicorn app.main:app --reload

A API estará disponível em http://127.0.0.1:8000
.

O Swagger UI com a documentação interativa está em http://127.0.0.1:8000/docs
.

🛠️ Endpoints
Listar Pokémons
URL: /pokemons
Método: GET
Query params:
limit (opcional, padrão=20)
offset (opcional, padrão=0)
Exemplo de request:

GET /pokemons?limit=10&offset=0

Resposta:

{
  "data": [
    {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
    {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}
  ],
  "pagination": {
    "total": 1350,
    "limit": 10,
    "offset": 0,
    "next": "https://pokeapi.co/api/v2/pokemon?offset=10&limit=10",
    "previous": null
  }
}

Detalhes de um Pokémon
URL: /pokemons/{pokemon_id}
Método: GET
Exemplo de request:

GET /pokemons/1

Resposta:

{
  "name": "bulbasaur",
  "id": 1,
  "height": 7,
  "weight": 69,
  "types": ["grass", "poison"],
  "sprites": {
    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
    "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png"
  }
}

404 - Pokémon não encontrado:

{"detail": "Pokemon not found"}

Testes

Rodar testes e verificar cobertura:

pytest --cov=app

Todos os testes passam.
Cobertura atual: 94%
Lint e formatação
Black para formatação automática:

black app tests

Flake8 para linting:

flake8 app tests