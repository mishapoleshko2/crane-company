from typing import Annotated

from fastapi import APIRouter, Depends

from crane_company.app.dependencies import get_company_repository
from crane_company.interactor.dto.company import (
    CompanyCreatingInputDTO,
    CompanyCreatingOutputDTO,
)
from crane_company.interactor.ports.repositories.company import CompanyRepository
from crane_company.interactor.use_cases.company_creating import CompanyCreatingUseCase

router = APIRouter(prefix="/api/company", tags=["company"])


@router.post("/", summary="Company creating")
async def create_company(
    input_dto: CompanyCreatingInputDTO,
    company_repository: Annotated[CompanyRepository, Depends(get_company_repository)],
) -> CompanyCreatingOutputDTO:
    use_case = CompanyCreatingUseCase(company_repository)
    output_dto = await use_case.execute(input_dto)
    return output_dto
