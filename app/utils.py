import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from . import models
from .database import engine, SessionLocal

async def fetch_and_store_pokemons():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://pokeapi.co/api/v2/pokemon?limit=1000') as resp:
            data = await resp.json()
            pokemons = data['results']
            
            async with SessionLocal() as db_session:
                for pokemon in pokemons:
                    async with session.get(pokemon['url']) as pokemon_resp:
                        pokemon_data = await pokemon_resp.json()
                        new_pokemon = models.Pokemon(
                            id=pokemon_data['id'],
                            name=pokemon_data['name'],
                            image=pokemon_data['sprites']['front_default'],
                            type=pokemon_data['types'][0]['type']['name']
                        )
                        db_session.add(new_pokemon)
                await db_session.commit()
