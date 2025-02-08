from dataclasses import dataclass

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select

from crane_company.domain.models.company import Company
from crane_company.infra.sqlalchemy_db import (
    Company as DBCompany,
    UserCompany as DBUserCompany,
)
from crane_company.interactor.dto.company import CompanyUpdatingInputDTO
from crane_company.interactor.exceptions import UserHasCompanyException
from crane_company.interactor.ports.repositories.company import CompanyRepository


@dataclass
class PGCompanyRepository(CompanyRepository):
    session: AsyncSession

    async def create_company(self, name: str, user_id: int) -> Company:
        db_company = DBCompany(name=name)
        db_user_company = DBUserCompany(user_id=user_id, company=db_company)
        self.session.add(db_company)
        self.session.add(db_user_company)
        try:
            await self.session.commit()
        except Exception as e:
            if 'unique constraint "uq_user_company_user_id"' in str(e):
                raise UserHasCompanyException from None
            raise e
        company = db_company.to_entity()
        return company

    async def update_company(
        self, company_id: int, data: CompanyUpdatingInputDTO
    ) -> Company | None:
        db_company = await self._get_db_company(company_id)
        if not db_company:
            return None

        db_company.name = data.name
        await self.session.commit()
        return db_company.to_entity()

    async def get_company(self, company_id: int) -> Company | None:
        db_company = await self._get_db_company(company_id)
        return db_company.to_entity() if db_company else None

    async def _get_db_company(self, company_id: int) -> DBCompany | None:
        query = select(DBCompany).where(DBCompany.id == company_id)
        result = await self.session.execute(query)
        db_company = result.scalar_one_or_none()
        return db_company

    async def get_user_company(self, user_id: int) -> Company | None:
        return await super().get_user_company(user_id)
