from typing import Annotated

from fastapi import APIRouter, Depends

from crane_company.app.dependencies import get_company_repository
from crane_company.interactor.dto.company import (
    CompanyCreatingInputDTO,
    CompanyUseCasesOutputDTO,
    CompanyUpdatingInputDTO,
    CompanyGettingInputDTO,
)
from crane_company.interactor.ports.repositories.company import CompanyRepository
from crane_company.interactor.use_cases.company import (
    CompanyCreatingUseCase,
    CompanyUpdatingUseCase,
    CompanyGettingUseCase,
)

router = APIRouter(prefix="/api/company", tags=["company"])


@router.post("/", summary="Creating company")
async def create_company(
    input_dto: CompanyCreatingInputDTO,
    company_repository: Annotated[CompanyRepository, Depends(get_company_repository)],
) -> CompanyUseCasesOutputDTO:
    use_case = CompanyCreatingUseCase(company_repository)
    output_dto = await use_case.execute(input_dto)
    return output_dto


@router.patch("/{company_id}", summary="Updating company")
@router.put("/{company_id}", summary="Updating company")
async def patch_company(
    company_id: int,
    company_repository: Annotated[CompanyRepository, Depends(get_company_repository)],
    input_dto: CompanyUpdatingInputDTO,
) -> CompanyUseCasesOutputDTO:
    use_case = CompanyUpdatingUseCase(company_repository)
    output_dto = await use_case.execute(input_dto, company_id)
    return output_dto


@router.get("/{company_id}", summary="Getting company")
async def get_company(
    company_id: int,
    company_repository: Annotated[CompanyRepository, Depends(get_company_repository)],
) -> CompanyUseCasesOutputDTO:
    use_case = CompanyGettingUseCase(company_repository)
    output_dto = await use_case.execute(CompanyGettingInputDTO(company_id=company_id))
    return output_dto
