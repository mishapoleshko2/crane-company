from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crane_company.infra.repositories.company import PGCompanyRepository
from crane_company.infra.sqlalchemy_db.utils import get_session


async def get_company_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> PGCompanyRepository:
    repo = PGCompanyRepository(session)
    return repo
