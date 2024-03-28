import sqlalchemy
from sqlalchemy import ext
from sqlalchemy import orm

def initialize_database(database_url: str):
    engine = ext.asyncio.create_async_engine(database_url)
    session = orm.sessionmaker(
        bind=engine,
        class_=ext.asyncio.AsyncSession,
        expire_on_commit=False,
    )
    
    return engine, session