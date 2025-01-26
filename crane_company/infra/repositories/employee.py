from dataclasses import dataclass
from sqlalchemy.ext.asyncio.session import AsyncSession

from crane_company.domain.models.employee import Employee
from crane_company.interactor.dto.employee import EmployeeCreatingInputDTO
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
