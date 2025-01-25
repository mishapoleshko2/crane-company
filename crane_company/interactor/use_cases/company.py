from dataclasses import dataclass

from crane_company.interactor.dto.company import (
    CompanyCreatingInputDTO,
    CompanyGettingInputDTO,
    CompanyUseCasesOutputDTO,
    CompanyUpdatingInputDTO,
)
from crane_company.interactor.exceptions import CompanyNotFound
from crane_company.interactor.ports.repositories.company import CompanyRepository


@dataclass
class CompanyCreatingUseCase:
    company_repository: CompanyRepository

    async def execute(
        self, input_dto: CompanyCreatingInputDTO
    ) -> CompanyUseCasesOutputDTO:
        company = await self.company_repository.create_company(
            input_dto.name, input_dto.user_id
        )
        return company


@dataclass
class CompanyUpdatingUseCase:
    company_repository: CompanyRepository

    async def execute(
        self, input_dto: CompanyUpdatingInputDTO, company_id: int
    ) -> CompanyUseCasesOutputDTO:
        company = await self.company_repository.update_company(company_id, input_dto)
        if not company:
            raise CompanyNotFound
        return company


@dataclass
class CompanyGettingUseCase:
    company_repository: CompanyRepository

    async def execute(
        self, input_dto: CompanyGettingInputDTO
    ) -> CompanyUseCasesOutputDTO:
        company = await self.company_repository.get_company(input_dto.company_id)
        if not company:
            raise CompanyNotFound
        return company
