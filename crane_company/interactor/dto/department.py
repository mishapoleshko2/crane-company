from pydantic import BaseModel, Field

from crane_company.domain.models.department import Department


class APIDeparnmentCreatingInputDTO(BaseModel):
    name: str


class DeparnmentCreatingInputDTO(BaseModel):
    name: str
    company_id: int
    head_id: int | None = None


class DepartmentDeletingInputDTO(BaseModel):
    company_id: int
    department_id: int


DepartmentUseCasesOutputDTO = Department


class DepartmentUpdatingInputDTO(BaseModel):
    name: str | None = Field(default=None)
    head_id: int | None = Field(default=None)
