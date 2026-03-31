from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    height: int
    weight: int

    class Config:
        orm_mode = True

class PokemonResponse(PokemonBase):
    id: int