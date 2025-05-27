from typing import Any, Coroutine

import asyncpg
from asyncpg import Record

from models.stat import Stat


class PlayRepository:
    def __init__(self, database_connection):
        self.databaseConnection: asyncpg.connection.Connection = database_connection

    async def find_play_by_player_id(self, player_id: str) -> list[Stat]:
        rows = await self.databaseConnection.fetch('SELECT * FROM plays p WHERE p.player = $1', player_id)
        stats = [Stat.from_dict(dict(row)) for row in rows]
        return stats