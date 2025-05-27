import asyncpg
from dotenv import load_dotenv
import os
from core.app_logger import AppLogger

load_dotenv()

BASE_URL = os.getenv("DB_BASE_URL")
PASSWORD = os.getenv("DB_PASSWORD")
USER = os.getenv("DB_USERNAME")
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{BASE_URL}"


async def connect_to_db() -> asyncpg.Connection:
    AppLogger.info("[DATABASE] Connecting to database...")
    database_connection = await asyncpg.connect(DATABASE_URL)
    AppLogger.info("[DATABASE] Connected to database")

    return database_connection


async def close_db_connection(database_connection: asyncpg.connection.Connection) -> None:
    AppLogger.info("[DATABASE] Closing database connection...")
    await database_connection.close()
    AppLogger.info("[DATABASE] Closed database connection")
