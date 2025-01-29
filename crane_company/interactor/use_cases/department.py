from dataclasses import dataclass

from crane_company.interactor.exceptions import DepartmentNotFound, EmployeeNotFound
from crane_company.interactor.ports.repositories.departmeny import DepartmentRepository
from crane_company.interactor.dto.department import (
    DepartmentUseCasesOutputDTO as OutputDTO,
    DeparnmentCreatingInputDTO,
    DepartmentDeletingInputDTO,
    DepartmentUpdatingInputDTO,
)
from crane_company.interactor.ports.repositories.employee import EmployeeRepository


@dataclass
class DepartmentCreatingUseCase:
    department_repository: DepartmentRepository

    async def execute(self, input_dto: DeparnmentCreatingInputDTO) -> OutputDTO:
        department = await self.department_repository.create_department(
            input_dto.company_id, input_dto.name, input_dto.head_id
        )
        return department


@dataclass
class DepartmentDeletingUseCase:
    department_repository: DepartmentRepository

    async def execute(self, input_dto: DepartmentDeletingInputDTO) -> None:
        department = await self.department_repository.get_company_department(
            input_dto.company_id, input_dto.department_id
        )
        if not department:
            raise DepartmentNotFound
        await self.department_repository.delete_department(department.id)


@dataclass
class CompanyDepartmentsGettingUseCase:
    department_repository: DepartmentRepository

    async def execute(self, company_id: int) -> list[OutputDTO]:
        departments = await self.department_repository.get_company_departments(
            company_id
        )
        return departments


@dataclass
class DepartmentUpdatingUseCase:
    department_repository: DepartmentRepository
    employee_repository: EmployeeRepository

    async def execute(
        self, company_id: int, department_id: int, input_dto: DepartmentUpdatingInputDTO
    ) -> OutputDTO:
        if input_dto.head_id:
            employee = await self.employee_repository.get_employee(input_dto.head_id)
            if not employee or employee.company_id != company_id:
                raise EmployeeNotFound

        department = await self.department_repository.get_company_department(
            company_id, department_id
        )
        if not department:
            raise DepartmentNotFound
        await self.department_repository.update_department(department, input_dto)
        return department
