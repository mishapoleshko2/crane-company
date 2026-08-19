from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio.session import AsyncSession

from crane_company.infra.sqlalchemy_db.db import async_session


async def get_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e


get_context_session = asynccontextmanager(get_session)
