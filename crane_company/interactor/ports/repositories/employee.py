from typing import Protocol

from crane_company.domain.models.employee import Employee


class EmployeeRepository(Protocol):
    def create_employee(
        self, first_name: str, last_name: str, middle_name: str | None = None
    ) -> Employee:
        pass
