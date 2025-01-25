from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from crane_company.app.dependencies import get_department_repository
from crane_company.interactor.dto.department import (
    DeparnmentCreatingInputDTO,
    APIDeparnmentCreatingInputDTO,
    DepartmentDeletingInputDTO,
    DepartmentUpdatingInputDTO,
    DepartmentUseCasesOutputDTO,
)
from crane_company.interactor.ports.repositories.departmeny import DepartmentRepository
from crane_company.interactor.use_cases.department import (
    CompanyDepartmentsGettingUseCase,
    DepartmentCreatingUseCase,
    DepartmentDeletingUseCase,
    DepartmentUpdatingUseCase,
)


router = APIRouter(
    prefix="/api/companies/{company_id}/departments", tags=["department"]
)


@router.post("/")
async def create_department(
    company_id: int,
    data: APIDeparnmentCreatingInputDTO,
    department_repository: Annotated[
        DepartmentRepository, Depends(get_department_repository)
    ],
) -> DepartmentUseCasesOutputDTO:
    use_case = DepartmentCreatingUseCase(department_repository)
    input_dto = DeparnmentCreatingInputDTO(company_id=company_id, name=data.name)
    output_dto = await use_case.execute(input_dto)
    return output_dto


@router.get("/")
async def get_departments(
    company_id: int,
    department_repository: Annotated[
        DepartmentRepository, Depends(get_department_repository)
    ],
) -> list[DepartmentUseCasesOutputDTO]:
    use_case = CompanyDepartmentsGettingUseCase(department_repository)
    departments = await use_case.execute(company_id)
    return departments


@router.patch("/{department_id}")
async def update_department(
    company_id: int,
    department_id: int,
    department_repository: Annotated[
        DepartmentRepository,
        Depends(get_department_repository),
    ],
    data: DepartmentUpdatingInputDTO,
) -> DepartmentUseCasesOutputDTO:
    use_case = DepartmentUpdatingUseCase(department_repository)
    department = await use_case.execute(company_id, department_id, data)
    return department


@router.delete("/{department_id}")
async def delete_department(
    company_id: int,
    department_id: int,
    department_repository: Annotated[
        DepartmentRepository, Depends(get_department_repository)
    ],
) -> Response:
    use_case = DepartmentDeletingUseCase(department_repository)
    await use_case.execute(
        DepartmentDeletingInputDTO(company_id=company_id, department_id=department_id)
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
