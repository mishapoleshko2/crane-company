from pydantic import BaseModel

from crane_company.domain.models.company import Company


class CompanyCreatingInputDTO(BaseModel):
    name: str
    user_id: int


CompanyCreatingOutputDTO = Company
