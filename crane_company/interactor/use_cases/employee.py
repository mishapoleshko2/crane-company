from dataclasses import dataclass

from crane_company.interactor.dto.employee import (
    EmployeeCreatingInputDTO,
    EmployeeUseCasesOutputDTO,
)
from crane_company.interactor.exceptions import CompanyHasNotDepartmenError
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
