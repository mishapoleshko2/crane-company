from dataclasses import dataclass

from sqlalchemy.sql import delete, and_, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from crane_company.domain.models.department import Department
from crane_company.interactor.ports.repositories.departmeny import DepartmentRepository
from crane_company.infra.sqlalchemy_db.models.department import (
    Department as DBDepartment,
)
from crane_company.interactor.dto.department import DepartmentUpdatingInputDTO


@dataclass
class PGDepartmentRepository(DepartmentRepository):
    session: AsyncSession

    async def get_company_department(
        self, company_id: int, department_id: int
    ) -> Department | None:
        query = select(DBDepartment).where(
            and_(
                DBDepartment.id == department_id,
                DBDepartment.company_id == company_id,
            )
        )
        res = await self.session.execute(query)
        db_department = res.scalar_one_or_none()
        return db_department.to_entity() if db_department else None

    async def get_company_departments(self, company_id: int) -> list[Department]:
        query = select(DBDepartment).where(DBDepartment.company_id == company_id)
        answer = await self.session.execute(query)
        res = answer.fetchall()
        departments = [e[0].to_entity() for e in res] if res else []
        return departments

    async def delete_department(self, department_id: int) -> None:
        query = delete(DBDepartment).where(DBDepartment.id == department_id)
        await self.session.execute(query)
        await self.session.commit()

    async def create_department(
        self, company_id: int, name: str, head_id: int | None = None
    ) -> Department:
        db_department = DBDepartment(
            company_id=company_id,
            name=name,
            head_id=head_id,
        )
        self.session.add(db_department)
        await self.session.commit()

        department = db_department.to_entity()
        return department

    async def update_department(
        self, department: Department, data: DepartmentUpdatingInputDTO
    ) -> Department:
        updatings = data.model_dump(exclude_unset=True)
        db_department = await self.session.get(DBDepartment, department.id)

        for key, value in updatings.items():
            setattr(db_department, key, value)
            setattr(department, key, value)

        await self.session.commit()
