from fastapi import FastAPI, Request
from starlette.responses import JSONResponse


def add_exception_handler(app: FastAPI):
    @app.exception_handler(Exception)
    async def handle_generic_exception(request: Request, exc: Exception):
        return JSONResponse(status_code=400, content=str(exc))
