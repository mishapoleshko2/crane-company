from typing import Protocol, Any

from crane_company.domain.models.department import Department
from crane_company.interactor.dto.department import DepartmentUpdatingInputDTO


class DepartmentRepository(Protocol):
    async def get_company_department(
        self, company_id: int, department_id: int
    ) -> Department | None: ...

    async def get_company_departments(self, company_id: int) -> list[Department]: ...

    async def delete_department(self, department_id: int) -> None: ...

    async def create_department(
        self, company_id: int, name: str, head_id: int | None = None
    ) -> Department: ...

    async def update_department(
        self, department: Department, data: DepartmentUpdatingInputDTO
    ) -> None: ...
