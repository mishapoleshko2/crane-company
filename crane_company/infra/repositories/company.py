from dataclasses import dataclass

from sqlalchemy.ext.asyncio.session import AsyncSession

from crane_company.domain.models.company import Company
from crane_company.infra.sqlalchemy_db import (
    Company as DBCompany,
    UserCompany as DBUserCompany,
)
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
