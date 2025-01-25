from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from crane_company.infra.sqlalchemy_db.db import Base
from crane_company.domain.models.department import Department as DomainDepartment


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("company.id"), index=True, nullable=False
    )
    head_id: Mapped[int | None] = mapped_column(
        ForeignKey("employee.id"), index=True, nullable=True
    )

    def to_entity(self) -> DomainDepartment:
        return DomainDepartment(
            id=self.id,
            name=self.name,
            company_id=self.company_id,
            head_id=self.head_id,
        )
