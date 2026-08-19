from typing import Protocol

from crane_company.domain.models.employee import Employee
from crane_company.interactor.dto.employee import (
    EmployeeCreatingInputDTO,
    EmployeeUpdatingData,
)


class EmployeeRepository(Protocol):
    async def create_employee(self, data: EmployeeCreatingInputDTO) -> Employee: ...

    async def get_company_employees(self, company_id: int) -> list[Employee]: ...

    async def get_employee(self, employee_id: int) -> Employee | None: ...

    async def delepte_employee(self, employee_id: int) -> None: ...

    async def update_employee(
        self, employee: Employee, data: EmployeeUpdatingData
    ) -> None: ...
