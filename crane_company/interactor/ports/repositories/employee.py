from typing import Protocol

from crane_company.domain.models.employee import Employee
from crane_company.interactor.dto.employee import EmployeeCreatingInputDTO


class EmployeeRepository(Protocol):
    async def create_employee(self, data: EmployeeCreatingInputDTO) -> Employee: ...
