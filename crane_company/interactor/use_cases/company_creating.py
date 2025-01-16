from dataclasses import dataclass

from crane_company.interactor.dto.company import (
    CompanyCreatingInputDTO,
    CompanyCreatingOutputDTO,
)
from crane_company.interactor.ports.repositories.company import CompanyRepository


@dataclass
class CompanyCreatingUseCase:
    company_repository: CompanyRepository

    async def execute(
        self, input_dto: CompanyCreatingInputDTO
    ) -> CompanyCreatingOutputDTO:
        company = await self.company_repository.create_company(
            input_dto.name, input_dto.user_id
        )
        return company
