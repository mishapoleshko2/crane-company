from fastapi import APIRouter
from crane_company.app.routers.company import router as company_router
from crane_company.app.routers.employee import router as employee_router
from crane_company.app.routers.department import router as department_router


app_router = APIRouter(prefix="/api/companies")
app_router.include_router(company_router)
app_router.include_router(employee_router)
app_router.include_router(department_router)
