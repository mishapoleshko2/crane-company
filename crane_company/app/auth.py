from typing import Annotated, TypedDict

import jwt
from fastapi import Depends, Path
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from crane_company.app.exceptions import credentials_exception, autherization_exceptions
from crane_company.app.dependencies import get_company_repository
from crane_company.interactor.ports.repositories.company import CompanyRepository
from crane_company.settings import settings


security = HTTPBearer()


class TokenPayload(TypedDict):
    user_id: int

    @classmethod
    def validate(cls, data: dict) -> bool:
        is_valid = next((False for key in cls.__annotations__ if key not in data), True)
        return is_valid


async def extract_jwt_payload(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> TokenPayload:
    token = credentials.credentials
    secret_key = settings.auth_jwt_secret.get_secret_value()
    try:
        payload = jwt.decode(token, secret_key, [settings.auth_jwt_encoding_algorithm])
        TokenPayload.validate(payload)
        return payload
    except Exception:
        raise credentials_exception


async def verify_user(
    company_id: Annotated[int, Path()],
    company_repository: Annotated[CompanyRepository, Depends(get_company_repository)],
    jwt_payload: Annotated[TokenPayload, Depends(extract_jwt_payload)],
) -> None:
    user_id = jwt_payload["user_id"]
    user_company = await company_repository.get_company(user_id)

    if not user_company or user_company.id != company_id:
        raise autherization_exceptions
