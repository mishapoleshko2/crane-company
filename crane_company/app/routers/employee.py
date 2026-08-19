from typing import Annotated
from fastapi import APIRouter, Body, Depends, Path, Response, status

from crane_company.app.auth import verify_user
from crane_company.app.dependencies import (
    get_employee_repository,
    get_department_repository,
)
from crane_company.interactor.dto.employee import (
    EmployeeCreatingPayload,
    EmployeeCreatingInputDTO,
    EmployeeUseCasesOutputDTO,
    EmployeeDeletingInputDTO,
    EmployeeUpdatingData,
    EmployeeUpdatingInputDTO,
)
from crane_company.interactor.ports.repositories.employee import EmployeeRepository
from crane_company.interactor.ports.repositories.departmeny import DepartmentRepository
from crane_company.interactor.use_cases.employee import (
    EmployeeCreatingUseCase,
    CompanyEmployeesGettingUseCase,
    EmployeeDeletingUseCase,
    EmployeeUpdatingUseCase,
)


router = APIRouter(
    prefix="/{company_id}/employees",
    tags=["employee"],
    dependencies=[Depends(verify_user)],
)


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


@router.get("/", name="getting company employees")
async def get_company_employees(
    company_id: Annotated[int, Path()],
    employee_repository: Annotated[
        EmployeeRepository, Depends(get_employee_repository)
    ],
) -> list[EmployeeUseCasesOutputDTO]:
    use_case = CompanyEmployeesGettingUseCase(employee_repository)
    employees = await use_case.execute(company_id)
    return employees


@router.delete("/{employee_id}", name="deleting employee")
async def delete_employee(
    company_id: Annotated[int, Path()],
    employee_id: Annotated[int, Path()],
    employee_repository: Annotated[
        EmployeeRepository, Depends(get_employee_repository)
    ],
) -> Response:
    use_case = EmployeeDeletingUseCase(employee_repository)
    input_dto = EmployeeDeletingInputDTO(company_id=company_id, employee_id=employee_id)
    await use_case.execute(input_dto)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{employee_id}", name="updating employee")
async def update_employee(
    company_id: Annotated[int, Path()],
    employee_id: Annotated[int, Path()],
    payload: Annotated[EmployeeUpdatingData, Body()],
    employee_repository: Annotated[
        EmployeeRepository, Depends(get_employee_repository)
    ],
    department_repository: Annotated[
        DepartmentRepository, Depends(get_department_repository)
    ],
) -> EmployeeUseCasesOutputDTO:
    input_dto = EmployeeUpdatingInputDTO(
        company_id=company_id,
        employee_id=employee_id,
        data=payload,
    )
    use_case = EmployeeUpdatingUseCase(employee_repository, department_repository)
    employee = await use_case.execute(input_dto)
    return employee
