from fastapi import FastAPI
from app.routers import pokemon

app = FastAPI()
app.include_router(pokemon.router)