from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from crane_company.infra.sqlalchemy_db.db import Base


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=int)

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
