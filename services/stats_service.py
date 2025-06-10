from asyncpg import ForeignKeyViolationError

from models.dtos.add_play_dto import AddPlayDto
from models.exceptions.not_found_exception import AppNotFound
from models.median import Median
from models.stat import Stat
from repositories.play_repository import PlayRepository


class StatsService:
    def __init__(self, repository: PlayRepository):
        self.repository: PlayRepository = repository

    async def get_player_plays(self, player_id: str):
        plays: list[Stat] = await self.repository.find_play_by_player_id(player_id)

        if plays is None or len(plays) == 0:
            raise AppNotFound('Sem estatisticas registradas')

        return plays

    async def get_player_medians(self, player_id: str):
        stats: list[Stat] = await self.get_player_plays(player_id)

        games = []

        free_trow = []
        failure_free_trow = []
        two_points = []
        failure_two_points = []
        tree_points = []
        failure_tree_points = []
        assists = []
        steals = []
        rebounds = []
        blocks = []
        falts = []
        turnovers = []

        for stat in stats:
            games.append(stat.game_id)
            if stat.free_trow is not None:
                free_trow.append(stat.free_trow)
            if stat.failure_free_trow is not None:
                failure_free_trow.append(stat.failure_free_trow)
            if stat.two_points is not None:
                two_points.append(stat.two_points)
            if stat.failure_two_points is not None:
                failure_two_points.append(stat.failure_two_points)
            if stat.tree_points is not None:
                tree_points.append(stat.tree_points)
            if stat.failure_tree_points is not None:
                failure_tree_points.append(stat.failure_tree_points)
            if stat.assists is not None:
                assists.append(stat.assists)
            if stat.steals is not None:
                steals.append(stat.steals)
            if stat.rebounds is not None:
                rebounds.append(stat.rebounds)
            if stat.blocks is not None:
                blocks.append(stat.blocks)
            if stat.falts is not None:
                falts.append(stat.falts)
            if stat.turnovers is not None:
                turnovers.append(stat.turnovers)

        games = set(games)

        free_trow_median = sum(free_trow) / len(games)
        two_points_median = sum(two_points) / len(games)
        three_points_median = sum(tree_points) / len(games)

        median: Median = Median(
            free_trow_median + (two_points_median * 2) + (three_points_median * 3),
            free_trow_median,
            sum(failure_free_trow) / len(games),
            two_points_median,
            sum(failure_two_points) / len(games),
            three_points_median,
            sum(failure_tree_points) / len(games),
            sum(assists) / len(games),
            sum(steals) / len(games),
            sum(rebounds) / len(games),
            sum(blocks) / len(games),
            sum(falts) / len(games),
            sum(turnovers) / len(games),
        )

        return median

    async def add_play(self, player_id: str, play: AddPlayDto):
        try:
            await self.repository.add_play(player_id,
                                           play.game_id, play.court_locate, play.free_throw, play.failure_free_throw,
                                           play.two_point, play.failure_two_point, play.three_point,
                                           play.failure_three_point, play.assist, play.steal, play.rebound,
                                           play.block, play.falt, play.turnover)
        except ForeignKeyViolationError:
            raise AppNotFound('Jogo não encontrado')

        return
