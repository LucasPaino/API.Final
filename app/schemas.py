from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class Sprites(BaseModel):
    front_default: Optional[str] = None
    back_default: Optional[str] = None


class PokemonBase(BaseModel):
    name: str
    height: int
    weight: int
    types: List[str]
    sprites: Sprites


class PokemonCreate(PokemonBase):
    model_config = ConfigDict(extra="forbid")


class Pokemon(PokemonBase):
    id: int

    model_config = ConfigDict(from_attributes=True)