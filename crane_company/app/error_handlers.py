from typing import Callable

from fastapi import Response, Request, status
from fastapi.responses import JSONResponse

from crane_company.exceptions import SystemException
from crane_company.interactor.exceptions import UserHasCompanyException, CompanyNotFound

__all__ = ("ERROR_HANDLERS",)


CODE_MAPPING: dict[type[Exception], int] = {
    UserHasCompanyException: status.HTTP_409_CONFLICT,
    CompanyNotFound: status.HTTP_404_NOT_FOUND,
}


def handle_system_exception(_: Request, exc: Exception) -> Response:
    code = CODE_MAPPING.get(type(exc), status.HTTP_400_BAD_REQUEST)
    return JSONResponse(status_code=code, content={"msg": str(exc)})


ERROR_HANDLERS: dict[
    type[SystemException], Callable[[Request, Exception], Response]
] = {
    SystemException: handle_system_exception,
}
