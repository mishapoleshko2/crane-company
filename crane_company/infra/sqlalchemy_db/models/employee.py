from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from crane_company.infra.sqlalchemy_db.db import Base
from crane_company.domain.models.employee import Employee as DomainEmployee


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    middle_name: Mapped[str] = mapped_column(nullable=False)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("company.id"), nullable=False, index=True
    )
    department_id: Mapped[int] = mapped_column(
        ForeignKey("department.id"), nullable=True, index=True
    )

    phone_number: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)

    def to_entity(self) -> DomainEmployee:
        employee = DomainEmployee(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name,
            company_id=self.company_id,
            department_id=self.department_id,
            phone_number=self.phone_number,
            email=self.email,
        )
        return employee
