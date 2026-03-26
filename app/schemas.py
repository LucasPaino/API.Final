from pydantic import BaseModel, ConfigDict

class PokemonBase(BaseModel):
    name: str
    height: int
    weight: int

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int
    model_config = ConfigDict(from_attributes=True)