# Pokémon API

API RESTful de Pokémon construída com **FastAPI**, **SQLAlchemy**, **Docker** e testes com **pytest**.  
Consome dados da [PokeAPI](https://pokeapi.co/) e oferece endpoints paginados com persistência local via PostgreSQL.

---

## 🛠 Funcionalidades

- Listar pokémons paginados (`/pokemons`)
- Detalhes de um pokémon (`/pokemons/{id}`)
- Criação de pokémons no banco local
- Exclusão de pokémons
- Persistência com PostgreSQL via SQLAlchemy
- Testes unitários com mocks da PokeAPI
- Docker + docker-compose
- CI/CD configurado para deploy automático (GitHub Actions)
- Documentação automática via Swagger (`/docs`)

---

## 🚀 Tecnologias

- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose
- Pytest + pytest-mock
- Httpx
- Python-dotenv
- Alembic (migrações futuras)
- GitHub Actions (CI/CD)

---

## ⚙️ Como rodar localmente

1. Clone o repositório:

```bash
git clone <seu-repo-url>
cd API.Final

Crie e ative o ambiente virtual:

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Configure variáveis de ambiente:

Crie um arquivo .env na raiz:

DATABASE_URL=postgresql://postgres:postgres@db:5432/pokemon

Para testes unitários, crie .env.test:

DATABASE_URL=sqlite:///./test.db

Execute a API localmente:

uvicorn app.main:app --reload

Swagger UI disponível em: http://127.0.0.1:8000/docs

🐳 Rodando com Docker

Certifique-se de ter Docker e Docker Compose instalados

Execute:

docker-compose up --build

A aplicação estará disponível em: http://localhost:8000/docs

O banco PostgreSQL será criado automaticamente via Docker Compose

🧪 Testes

Para rodar os testes unitários:

pytest

Cobrem:

Sucesso dos endpoints
Erros (404, dados inexistentes)

Paginação

Testes usam mocks para isolar chamadas à PokeAPI

🌐 Deploy

A API pode ser publicada em serviços como Render
 ou Railway.

Link de produção (exemplo):

https://pokemon-api-tec5.onrender.com/docs

🔍 Exemplos de uso

Listar Pokémons (paginação)

GET /pokemons?limit=20&offset=0

Resposta:

{
  "data": [
    {
      "name": "pikachu",
      "id": 25,
      "height": 4,
      "weight": 60,
      "types": ["electric"],
      "sprites": {}
    }
  ],
  "pagination": {
    "total": null,
    "limit": 20,
    "offset": 0,
    "next": "/pokemons?limit=20&offset=20",
    "previous": null
  }
}
Detalhes de um Pokémon

GET /pokemons/25

{
  "name": "pikachu",
  "id": 25,
  "height": 4,
  "weight": 60,
  "types": ["electric"],
  "sprites": {}
}
📂 Estrutura do projeto
API.Final/
├─ app/
│  ├─ main.py
│  ├─ models.py
│  ├─ crud.py
│  ├─ database.py
│  ├─ schemas.py
│  └─ services/pokeapi.py
├─ tests/
│  └─ test_main.py
├─ .env
├─ .env.test
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ README.md

🔧 Boas práticas

Variáveis de ambiente para configuração de banco
Testes isolados e com mocks
Docker Compose para desenvolvimento e produção
Documentação automática com Swagger
CI/CD via GitHub Actions