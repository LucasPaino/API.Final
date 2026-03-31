from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app import crud, schemas
from app.services.pokeapi import get_pokemon_from_api, list_pokemons_from_api

router = APIRouter(prefix="/pokemons", tags=["Pokémons"])


@router.get("", response_model=schemas.PokemonListResponse)
def list_pokemons(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    pokemons, total_local = crud.get_pokemons(db, skip=offset, limit=limit)

    if not pokemons:
        api_data = list_pokemons_from_api(limit=limit, offset=offset)
        total = api_data.get("count", 0)
        for entry in api_data.get("results", []):
            pokemon_id = int(entry["url"].rstrip("/").split("/")[-1])
            if not crud.get_pokemon(db, pokemon_id):
                try:
                    details = get_pokemon_from_api(pokemon_id)
                    crud.create_pokemon(db, schemas.PokemonCreate(**details))
                except Exception:
                    pass
        pokemons, total_local = crud.get_pokemons(db, skip=offset, limit=limit)
    else:
        try:
            api_data = list_pokemons_from_api(limit=1, offset=0)
            total = api_data.get("count", total_local)
        except Exception:
            total = total_local

    next_url = f"/pokemons?limit={limit}&offset={offset + limit}" if offset + limit < total else None
    prev_url = f"/pokemons?limit={limit}&offset={offset - limit}" if offset > 0 else None

    return schemas.PokemonListResponse(
        data=pokemons,
        pagination=schemas.PaginationMeta(
            total=total,
            limit=limit,
            offset=offset,
            next=next_url,
            previous=prev_url,
        ),
    )


@router.get("/{pokemon_id}", response_model=schemas.PokemonResponse)
def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = crud.get_pokemon(db, pokemon_id)
    if not pokemon:
        try:
            data = get_pokemon_from_api(pokemon_id)
            pokemon = crud.create_pokemon(db, schemas.PokemonCreate(**data))
        except Exception:
            raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return pokemon


@router.post("", response_model=schemas.PokemonResponse, status_code=201)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    existing = crud.get_pokemon(db, pokemon.id)
    if existing:
        raise HTTPException(status_code=400, detail="Pokémon com este ID já existe")
    return crud.create_pokemon(db, pokemon)


@router.put("/{pokemon_id}", response_model=schemas.PokemonResponse)
def update_pokemon(
    pokemon_id: int, data: schemas.PokemonUpdate, db: Session = Depends(get_db)
):
    pokemon = crud.update_pokemon(db, pokemon_id, data)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return pokemon


@router.delete("/{pokemon_id}", status_code=204)
def delete_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = crud.delete_pokemon(db, pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")