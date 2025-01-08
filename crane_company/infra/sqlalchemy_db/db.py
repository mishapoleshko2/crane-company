from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from crane_company.settings import settings


class Base(AsyncAttrs, DeclarativeBase): ...


engine = create_async_engine(str(settings.db_uri))
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
