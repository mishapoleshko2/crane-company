from crane_company.exceptions import SystemException


class UserHasCompanyException(SystemException):
    def __init__(self) -> None:
        super().__init__("User cann`t have more than 2 companies")
