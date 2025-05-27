import asyncpg

from core.app_logger import AppLogger
from repositories.play_repository import PlayRepository
from services.stats_service import StatsService

def build_dependencies(database_connection: asyncpg.connection.Connection) -> dict:
    play_repository: PlayRepository = PlayRepository(database_connection)

    dependencies = {
        StatsService: StatsService(play_repository),
    }

    AppLogger.info("[INJECTOR] Inject dependencies [StatsService]")

    return dependencies