from sqlalchemy.orm import mapped_column, Mapped

from crane_company.infra.sqlalchemy_db.db import Base


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
