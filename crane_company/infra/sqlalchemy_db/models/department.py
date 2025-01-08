from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from crane_company.infra.sqlalchemy_db.db import Base


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    company_id: Mapped[str] = mapped_column(
        ForeignKey("company.id"), index=True, nullable=False
    )
    head_id: Mapped[int | None] = mapped_column(
        ForeignKey("employee.id"), index=True, nullable=True
    )