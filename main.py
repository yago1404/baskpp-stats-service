from contextlib import asynccontextmanager

from asyncpg import connection
from fastapi import FastAPI
from sqlalchemy.sql.coercions import expect
from starlette.responses import JSONResponse

from core.database import connect_to_db, close_db_connection
from core.injector import build_dependencies
from models.exceptions.app_exception import AppException
from routes import stats_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    database_connection: connection.Connection = await connect_to_db()
    app.state.injector = build_dependencies(database_connection)
    yield
    await close_db_connection(database_connection)

app = FastAPI(lifespan=lifespan)

@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )

app.include_router(stats_routes.router)

@app.get("/status")
async def root():
    return {"status": "Online"}
