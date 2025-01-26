from typing import Annotated
from fastapi import APIRouter, Body, Depends, Path

from crane_company.app.dependencies import (
    get_employee_repository,
    get_department_repository,
)
from crane_company.interactor.dto.employee import (
    EmployeeCreatingPayload,
    EmployeeCreatingInputDTO,
    EmployeeUseCasesOutputDTO,
)
from crane_company.interactor.ports.repositories.employee import EmployeeRepository
from crane_company.interactor.ports.repositories.departmeny import DepartmentRepository
from crane_company.interactor.use_cases.employee import EmployeeCreatingUseCase
from typing import Annotated


router = APIRouter(prefix="/{company_id}/employees", tags=["employee"])


@router.post("/", name="employee creating")
async def create_employee(
    company_id: Annotated[int, Path()],
    payload: Annotated[EmployeeCreatingPayload, Body()],
    employee_repository: Annotated[
        EmployeeRepository, Depends(get_employee_repository)
    ],
    department_repository: Annotated[
        DepartmentRepository, Depends(get_department_repository)
    ],
) -> EmployeeUseCasesOutputDTO:
    use_case = EmployeeCreatingUseCase(employee_repository, department_repository)
    input_dto = EmployeeCreatingInputDTO(company_id=company_id, **payload.model_dump())
    employee = await use_case.execute(input_dto)
    return employee
