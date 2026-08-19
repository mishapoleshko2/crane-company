from dataclasses import dataclass
from sqlalchemy.sql import select, delete
from sqlalchemy.ext.asyncio.session import AsyncSession

from crane_company.domain.models.employee import Employee
from crane_company.interactor.dto.employee import (
    EmployeeCreatingInputDTO,
    EmployeeUpdatingData,
)
from crane_company.interactor.ports.repositories.employee import EmployeeRepository
from crane_company.infra.sqlalchemy_db.models.employee import Employee as DBEmployee


@dataclass(frozen=True)
class PGEmployeeRepository(EmployeeRepository):
    session: AsyncSession

    async def create_employee(self, data: EmployeeCreatingInputDTO) -> Employee:
        db_employee = DBEmployee(
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name,
            company_id=data.company_id,
            department_id=data.department_id,
            phone_number=data.phone_number,
            email=data.email,
        )
        self.session.add(db_employee)
        await self.session.commit()
        employee = db_employee.to_entity()

        return employee

    async def get_company_employees(self, company_id: int) -> list[Employee]:
        query = select(DBEmployee).where(DBEmployee.company_id == company_id)
        result = await self.session.execute(query)
        db_employees = result.fetchall()
        employees = [e[0].to_entity() for e in db_employees] if db_employees else []
        return employees

    async def get_employee(self, employee_id: int) -> Employee | None:
        db_employee = await self.session.get(DBEmployee, employee_id)
        employee = db_employee.to_entity() if db_employee else None
        return employee

    async def delepte_employee(self, employee_id: int) -> None:
        query = delete(DBEmployee).where(DBEmployee.id == employee_id)
        await self.session.execute(query)
        await self.session.commit()

    async def update_employee(
        self, employee: Employee, data: EmployeeUpdatingData
    ) -> None:
        db_employee = await self.session.get(DBEmployee, employee.id)
        updatings = data.model_dump(exclude_unset=True)

        for key, value in updatings.items():
            setattr(employee, key, value)
            setattr(db_employee, key, value)

        await self.session.commit()
