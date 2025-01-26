from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crane_company.infra.repositories.company import PGCompanyRepository
from crane_company.infra.repositories.department import PGDepartmentRepository
from crane_company.infra.repositories.employee import PGEmployeeRepository
from crane_company.infra.sqlalchemy_db.utils import get_session
from crane_company.interactor.ports.repositories.company import CompanyRepository
from crane_company.interactor.ports.repositories.departmeny import DepartmentRepository
from crane_company.interactor.ports.repositories.employee import EmployeeRepository


async def get_company_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> CompanyRepository:
    repo = PGCompanyRepository(session)
    return repo


async def get_department_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> DepartmentRepository:
    repo = PGDepartmentRepository(session)
    return repo


async def get_employee_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> EmployeeRepository:
    repo = PGEmployeeRepository(session)
    return repo
