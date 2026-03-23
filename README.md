 Pokémon API com FastAPI
 Descrição

Esta é uma API RESTful desenvolvida com FastAPI que consome dados da PokeAPI
 e os disponibiliza de forma estruturada e paginada.

O projeto foi desenvolvido como atividade final de back-end em Python, aplicando conceitos como:

Construção de APIs com FastAPI
Consumo de APIs externas
Testes automatizados com pytest
Dockerização
CI/CD com GitHub Actions
Deploy em produção

 API em Produção

 https://pokemon-api-tec5.onrender.com

 Documentação (Swagger UI)

 https://pokemon-api-tec5.onrender.com/docs

Use essa interface para testar todos os endpoints diretamente no navegador.

 Funcionalidades
 Listagem paginada de pokémons
 Detalhes de um pokémon específico
 Criação de pokémons (local)
 Atualização de pokémons (local)
 Exclusão de pokémons (local)
 Documentação automática com Swagger

 Endpoints

 Listar Pokémons

 GET /pokemons?limit=20&offset=0

Buscar Pokémon por ID

GET /pokemons/{id}

Criar Pokémon

POST /pokemons

Atualizar Pokémon

PUT /pokemons/{id}

Deletar Pokémon

DELETE /pokemons/{id}


Exemplo de Resposta

GET /pokemons/1

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

Como rodar localmente
1. Clonar o repositório

git clone https://github.com/LucasPaino/API.Final.git
cd API.Final

2. Criar ambiente virtual

python -m venv .venv

3. Ativar ambiente virtual

Windows:
.\.venv\Scripts\Activate

Linux/Mac:
source .venv/bin/activate

4. Instalar dependências

pip install -r requirements.txt

5. Rodar a aplicação

uvicorn app.main:app --reload

6. Acessar no navegador

http://127.0.0.1:8000/docs


 Testes

Para rodar os testes:

pytest --cov=app


Cobertura atual: ~90%+
Testes incluem:
Listagem de pokémons
Busca por ID
Tratamento de erro (não encontrado)
CRUD básico

 Docker

Build da imagem

docker build -t pokemon-api .

Rodar container

docker run -p 8000:8000 pokemon-api

 CI/CD

O projeto utiliza GitHub Actions para:

Instalar dependências
Rodar testes automaticamente
Verificar qualidade do código

O deploy é feito automaticamente no Render a cada push na branch main.

 Tecnologias utilizadas

Python 3.13
FastAPI
Uvicorn
Requests
Pytest
Pytest-cov
Docker
GitHub Actions
Render

 Observações

Os dados são consumidos diretamente da PokeAPI
Operações de criação, atualização e exclusão são simuladas localmente (sem persistência em banco)
A API segue boas práticas REST e organização de projeto
