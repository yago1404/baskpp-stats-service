import asyncpg

from models.stat import Stat


class PlayRepository:
    def __init__(self, database_connection: asyncpg.connection.Connection):
        self.databaseConnection: asyncpg.connection.Connection = database_connection

    async def find_play_by_player_id(self, player_id: str) -> list[Stat]:
        rows = await self.databaseConnection.fetch('''
        SELECT p.*
        FROM plays p
        JOIN games g ON p.game = g.id
        WHERE p.player = $1
          AND p.game IN (
              SELECT g_sub.id
              FROM games g_sub
              JOIN plays p_sub ON g_sub.id = p_sub.game
              WHERE p_sub.player = $1
              GROUP BY g_sub.id, g_sub.date_time
              ORDER BY g_sub.date_time DESC
              LIMIT 15
          )
        ORDER BY g.date_time DESC;
        ''', player_id)
        stats = [Stat.from_dict(dict(row)) for row in rows]
        return stats

    async def add_play(self, player_id: str, game_id: str, court_locate: str, free_throw: int | None,
                       failure_free_throw: int | None,
                       tow_point: int | None, failure_tow_point: int | None, tree_point: int | None,
                       failure_tree_point: int | None, assist: int | None, steal: int | None, rebound: int | None,
                       block: int | None, falt: int | None, turnover: int | None) -> None:
        await self.databaseConnection.execute(
            'INSERT INTO plays (player, game, court_locate, free_throw, failure_free_throw, two_points, failure_two_points, tree_points, failure_tree_points, assistances, steals, rebounds, blocks, falts, turnovers) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15)',
            player_id, game_id, court_locate, free_throw, failure_free_throw, tow_point, failure_tow_point, tree_point, failure_tree_point, assist, steal, rebound, block, falt, turnover)
