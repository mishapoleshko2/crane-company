from typing import Protocol

from crane_company.domain.models.company import Company
from crane_company.interactor.dto.company import CompanyUpdatingInputDTO


class CompanyRepository(Protocol):
    async def create_company(self, name: str, user_id: int) -> Company: ...

    async def get_company(self, company_id: int) -> Company | None: ...

    async def update_company(
        self, company_id: int, data: CompanyUpdatingInputDTO
    ) -> Company | None: ...

    async def get_user_company(self, user_id: int) -> Company | None: ...
