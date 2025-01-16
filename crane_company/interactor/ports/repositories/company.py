from typing import Protocol

from crane_company.domain.models.company import Company


class CompanyRepository(Protocol):
    async def create_company(self, name: str, user_id: int) -> Company: ...
