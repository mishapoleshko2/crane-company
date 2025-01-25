import uvicorn
import typer
from fastapi import FastAPI
import pyfiglet  # type: ignore

from crane_company.app.error_handlers import ERROR_HANDLERS
from crane_company.app.routers.company import router as company_router
from crane_company.app.routers.department import router as department_router

app = FastAPI()
app.include_router(company_router)
app.include_router(department_router)

for exc, handler in ERROR_HANDLERS.items():
    app.add_exception_handler(exc, handler)


def main(
    host: str = typer.Argument("127.0.0.1", help="Application host"),
    port: int = typer.Argument(8000, help="Application port"),
) -> None:
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    typer.echo(pyfiglet.figlet_format("CRANE-COMPANY", font="slant"))
    typer.run(main)
