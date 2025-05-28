import asyncpg

from models.game import Game


class GameRepository:
    def __init__(self, database_connection: asyncpg.connection.Connection):
        self.databaseConnection: asyncpg.connection.Connection = database_connection

    async def find_game_from_id(self, game_id: str):
        rows = await self.databaseConnection.fetch('SELECT * FROM games g WHERE g.id = $1', game_id)

        return Game.from_dict(rows[0])