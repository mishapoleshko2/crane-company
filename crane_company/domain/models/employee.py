from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    id: int

    first_name: str
    last_name: str
    middle_name: str | None

    company_id: int
    department_id: int | None = None

    phone_number: str | None = None
    email: EmailStr | None = None
