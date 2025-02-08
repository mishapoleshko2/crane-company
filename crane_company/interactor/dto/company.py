from pydantic import BaseModel

from crane_company.domain.models.company import Company


class CompanyCreatingSchema(BaseModel):
    name: str


class CompanyCreatingInputDTO(BaseModel):
    user_id: int
    schema: CompanyCreatingSchema


CompanyUseCasesOutputDTO = Company


class CompanyUpdatingInputDTO(BaseModel):
    name: str


class CompanyGettingInputDTO(BaseModel):
    company_id: int
