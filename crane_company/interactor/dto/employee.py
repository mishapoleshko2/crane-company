from pydantic import BaseModel, Field, EmailStr

from crane_company.domain.models.employee import Employee


class EmployeeCreatingPayload(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = Field(default=None)

    department_id: int | None = Field(default=None)

    phone_number: str | None = Field(default=None)
    phone_number: str | None = Field(default=None)
    email: EmailStr | None = Field(default=None)


class EmployeeCreatingInputDTO(EmployeeCreatingPayload):
    company_id: int


EmployeeUseCasesOutputDTO = Employee
