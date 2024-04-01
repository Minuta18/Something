import sqlalchemy
from sqlalchemy import ext
from sqlalchemy import orm

async def init_connection(database_url: str):
    engine = ext.asyncio.create_async_engine(database_url)
    session = orm.sessionmaker(
        bind=engine,
        class_=ext.asyncio.AsyncSession,
        expire_on_commit=False,
    )
    
    return engine, session

async def destroy_connection(engine: ext.asyncio.AsyncEngine):
    engine.dispose()

async def init_models(engine: ext.asyncio.AsyncEngine, base: ext.declarative):
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)



