from crane_company.exceptions import SystemException


class UserHasCompanyException(SystemException):
    def __init__(self) -> None:
        super().__init__("User can`t have more than 2 companies")


class CompanyNotFound(SystemException):
    def __init__(self) -> None:
        super().__init__("Company not found")


class DepartmentNotFound(SystemException):
    def __init__(self) -> None:
        super().__init__("Department not found")


class CompanyHasNotDepartmenError(SystemException):
    def __init__(self) -> None:
        super().__init__("The company doesn`t have the department")
