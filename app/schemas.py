from pydantic import BaseModel


class PokemonBase(BaseModel):
    nome: str
    tipo: str
    nivel: int


class PokemonCreate(PokemonBase):
    pass


class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True
