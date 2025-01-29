from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

from crane_company.infra.sqlalchemy_db.db import Base
from crane_company.domain.models.company import Company as DomainCompany


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    def to_entity(self) -> DomainCompany:
        return DomainCompany(
            id=self.id,
            name=self.name,
        )


class UserCompany(Base):
    __tablename__ = "user_company"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    company_id: Mapped[int] = mapped_column(
        ForeignKey("company.id"), nullable=False, index=True
    )
