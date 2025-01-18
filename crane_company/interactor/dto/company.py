from pydantic import BaseModel

from crane_company.domain.models.company import Company


class CompanyCreatingInputDTO(BaseModel):
    name: str
    user_id: int


CompanyUseCasesOutputDTO = Company


class CompanyUpdatingInputDTO(BaseModel):
    name: str


class CompanyGettingInputDTO(BaseModel):
    company_id: int
