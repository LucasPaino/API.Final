from typing import List, Optional
from pydantic import BaseModel


class SpritesSchema(BaseModel):
    front_default: Optional[str] = None
    back_default: Optional[str] = None


class PokemonBase(BaseModel):
    name: str
    height: int
    weight: int
    types: List[str] = []
    sprites: SpritesSchema = SpritesSchema()


class PokemonCreate(PokemonBase):
    id: int


class PokemonUpdate(BaseModel):
    name: Optional[str] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    types: Optional[List[str]] = None
    sprites: Optional[SpritesSchema] = None


class PokemonResponse(PokemonBase):
    id: int

    model_config = {"from_attributes": True}


class PaginationMeta(BaseModel):
    total: int
    limit: int
    offset: int
    next: Optional[str] = None
    previous: Optional[str] = None


class PokemonListResponse(BaseModel):
    data: List[PokemonResponse]
    pagination: PaginationMeta