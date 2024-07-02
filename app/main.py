from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from . import models, schemas, crud
from .database import engine, get_session
from .utils import fetch_and_store_pokemons

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    await fetch_and_store_pokemons()

@app.get("/api/v1/pokemons", response_model=List[schemas.Pokemon])
async def get_pokemons(name: str = None, type: str = None, session: AsyncSession = Depends(get_session)):
    pokemons = await crud.get_pokemons(session, name, type)
    return pokemons
