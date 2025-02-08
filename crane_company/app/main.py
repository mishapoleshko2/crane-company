import uvicorn
import typer
from fastapi import FastAPI
import pyfiglet  # type: ignore

from crane_company.app.error_handlers import ERROR_HANDLERS
from crane_company.app.app_router import app_router


app = FastAPI()
app.include_router(app_router)

for exc, handler in ERROR_HANDLERS.items():
    app.add_exception_handler(exc, handler)


def main(
    host: str = typer.Argument("127.0.0.1", help="Application host"),
    port: int = typer.Argument(8000, help="Application port"),
    workers: int = typer.Argument(1, help="Uvicorn workers"),
    reload: bool = typer.Option(False, help="Reload uvicorn app"),
) -> None:
    uvicorn.run("main:app", host=host, port=port, reload=reload, workers=workers)


if __name__ == "__main__":
    typer.echo(pyfiglet.figlet_format("CRANE-COMPANY", font="slant"))
    typer.run(main)
