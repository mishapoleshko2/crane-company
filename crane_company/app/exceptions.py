from fastapi.exceptions import HTTPException


credentials_exception = HTTPException(
    status_code=401,
    detail="Unable to validate credentials",
)

autherization_exceptions = HTTPException(
    status_code=403,
    detail="No access",
)
