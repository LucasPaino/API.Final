# Pokémon API - Python FastAPI

API RESTful em Python que consome dados da [PokéAPI](https://pokeapi.co/) e disponibiliza informações de Pokémon de forma paginada.

---

## Funcionalidades

- Listar pokémons com paginação (`GET /pokemons`)  
- Buscar pokémon por ID (`GET /pokemons/{id}`)  
- Persistência com banco relacional via SQLAlchemy ORM  
- Estrutura modular, organizada e testável  
- Testes unitários com `pytest`  
- Lint com `flake8`  
- Pipeline CI/CD pronta no GitHub Actions  

---

## Tecnologias

- Python 3.13  
- FastAPI  
- SQLAlchemy ORM  
- SQLite (para desenvolvimento e testes) / PostgreSQL (produção)  
- Pytest / pytest-cov  
- Flake8  
- GitHub Actions (CI/CD)  

---

## Rodando localmente

1. Clone o repositório:

```bash
git clone https://github.com/LucasPaino/API.Final.git
cd API.Final
Crie e ative o ambiente virtual:
# Linux/macOS
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
Instale as dependências:
pip install -r requirements.txt
Rodar a aplicação:
uvicorn app.main:app --reload

Acesse http://127.0.0.1:8000/docs
 para a documentação Swagger UI.

Testes

Executar todos os testes com cobertura:

pytest --cov=app tests/

O relatório de cobertura será gerado na pasta htmlcov/.

Deploy

A API já pode ser deployada em Render ou outro serviço compatível.
Link de produção: https://pokemon-api-tec5.onrender.com/docs

Observações
Todos os endpoints usam banco relacional via SQLAlchemy, garantindo persistência de dados
Código revisado para PEP8/flake8
Testes unitários com mocks e cobertura incluída
Variáveis de ambiente configuráveis via .env (ex: DATABASE_URL)