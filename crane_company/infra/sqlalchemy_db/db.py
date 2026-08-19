from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from crane_company.settings import settings


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)


class Base(AsyncAttrs, DeclarativeBase):
    metadata = metadata


engine = create_async_engine(str(settings.company_db_uri))
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
