from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_

from . import models

async def get_pokemons(session: AsyncSession, name: str = None, type: str = None):
    query = select(models.Pokemon)
    if name:
        query = query.filter(models.Pokemon.name.ilike(f"%{name}%"))
    if type:
        query = query.filter(models.Pokemon.type.ilike(f"%{type}%"))
    result = await session.execute(query)
    return result.scalars().all()
