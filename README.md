# Pokémon API 🎮

API RESTful em Python que consome dados da [PokéAPI](https://pokeapi.co/) e disponibiliza informações de Pokémon com persistência em banco de dados relacional via SQLAlchemy.

---

## Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy ORM
- SQLite (desenvolvimento/testes) / PostgreSQL (produção)
- Pytest / pytest-cov / pytest-mock
- Flake8
- Docker / Docker Compose
- GitHub Actions (CI/CD)
- Render (deploy)

---

## Funcionalidades

- Listar pokémons com paginação (`GET /pokemons`)
- Buscar pokémon por ID (`GET /pokemons/{id}`)
- Criar pokémon (`POST /pokemons`)
- Atualizar pokémon (`PUT /pokemons/{id}`)
- Deletar pokémon (`DELETE /pokemons/{id}`)
- Persistência com banco relacional via SQLAlchemy ORM
- Consumo direto da PokéAPI com cache local no banco
- Testes unitários com mocks
- CI/CD com GitHub Actions e deploy automático no Render

---

## Como rodar localmente

### 1. Clone o repositório
```bash
git clone https://github.com/LucasPaino/API.Final.git
cd API.Final
```

### 2. Crie e ative o ambiente virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:
```
DATABASE_URL=sqlite:///./pokemon.db
POKEAPI_URL=https://pokeapi.co/api/v2/pokemon
```

### 5. Rode a aplicação
```bash
uvicorn app.main:app --reload
```

Acesse a documentação em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Como rodar com Docker
```bash
docker-compose up --build
```

A API ficará disponível em [http://localhost:8000/docs](http://localhost:8000/docs)

> O Docker Compose sobe dois containers: um para a API e outro para o banco PostgreSQL.

---

## Como executar os testes
```bash
pytest
```

Para gerar relatório de cobertura:
```bash
pytest --cov=app tests/
```

---

## CI/CD

O projeto utiliza **GitHub Actions** para integração e entrega contínua:

- A cada `push` na branch `main` o pipeline roda automaticamente
- **CI:** instala dependências, executa lint com flake8 e roda os testes com pytest
- **CD:** após o CI passar, o deploy é feito automaticamente no Render via Deploy Hook

---

## Endpoints

### `GET /pokemons`
Lista pokémons com paginação.

**Parâmetros:**
- `limit` (padrão: 20)
- `offset` (padrão: 0)

**Resposta:**
```json
{
  "data": [
    {
      "id": 25,
      "name": "pikachu",
      "height": 4,
      "weight": 60,
      "types": ["electric"],
      "sprites": {
        "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png"
      }
    }
  ],
  "pagination": {
    "total": 1281,
    "limit": 20,
    "offset": 0,
    "next": "/pokemons?limit=20&offset=20",
    "previous": null
  }
}
```

### `GET /pokemons/{id}`
Retorna detalhes de um pokémon específico.

### `POST /pokemons`
Cria um novo pokémon no banco de dados.

### `PUT /pokemons/{id}`
Atualiza dados de um pokémon existente.

### `DELETE /pokemons/{id}`
Remove um pokémon do banco de dados.

---

## Link de produção

[https://pokemon-api-tec5.onrender.com/docs](https://pokemon-api-tec5.onrender.com/docs)