from dataclasses import dataclass

from crane_company.interactor.dto.employee import (
    EmployeeCreatingInputDTO,
    EmployeeUpdatingInputDTO,
    EmployeeUseCasesOutputDTO,
    EmployeeDeletingInputDTO,
)
from crane_company.interactor.exceptions import (
    CompanyHasNotDepartmenError,
    EmployeeNotFound,
)
from crane_company.interactor.ports.repositories.departmeny import DepartmentRepository
from crane_company.interactor.ports.repositories.employee import EmployeeRepository


@dataclass(frozen=True)
class EmployeeCreatingUseCase:
    employee_repository: EmployeeRepository
    department_repository: DepartmentRepository

    async def execute(
        self, input_dto: EmployeeCreatingInputDTO
    ) -> EmployeeUseCasesOutputDTO:
        department_id = input_dto.department_id
        if (
            department_id
            and not await self.department_repository.get_company_department(
                input_dto.company_id, department_id
            )
        ):
            raise CompanyHasNotDepartmenError

        employee = await self.employee_repository.create_employee(input_dto)
        return employee


@dataclass(frozen=True)
class CompanyEmployeesGettingUseCase:
    employee_repository: EmployeeRepository

    async def execute(self, company_id: int) -> list[EmployeeUseCasesOutputDTO]:
        employees = await self.employee_repository.get_company_employees(company_id)
        return employees


@dataclass(frozen=True)
class EmployeeDeletingUseCase:
    employee_repository: EmployeeRepository

    async def execute(self, input_dto: EmployeeDeletingInputDTO) -> None:
        employee = await self.employee_repository.get_employee(input_dto.employee_id)
        if not employee or employee.company_id != input_dto.company_id:
            raise EmployeeNotFound

        await self.employee_repository.delepte_employee(input_dto.employee_id)


@dataclass(frozen=True)
class EmployeeUpdatingUseCase:
    employee_repository: EmployeeRepository
    department_repository: DepartmentRepository

    async def execute(
        self, input_dto: EmployeeUpdatingInputDTO
    ) -> EmployeeUseCasesOutputDTO:
        updating_data = input_dto.data
        if (
            updating_data.department_id
            and not await self.department_repository.get_company_department(
                input_dto.company_id, updating_data.department_id
            )
        ):
            raise CompanyHasNotDepartmenError

        employee = await self.employee_repository.get_employee(input_dto.employee_id)
        if not employee or employee.company_id != input_dto.company_id:
            raise EmployeeNotFound
        await self.employee_repository.update_employee(employee, updating_data)
        return employee
