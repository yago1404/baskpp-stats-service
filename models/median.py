from models.stat import Stat


class Median:
    def __init__(self, points: float, free_trow: float, failure_free_trow: float,
                 two_points: float, failure_two_points: float, tree_points: float, failure_tree_points: float,
                 assists: float,
                 steals: float, rebounds: float, blocks: float, falts: float, turnovers: float, game_id=None):
        self.game_id = game_id
        self.points = points
        self.free_trow = free_trow
        self.failure_free_trow = failure_free_trow
        self.two_points = two_points
        self.failure_two_points = failure_two_points
        self.tree_points = tree_points
        self.failure_tree_points = failure_tree_points
        self.assists = assists
        self.steals = steals
        self.rebounds = rebounds
        self.blocks = blocks
        self.falts = falts
        self.turnovers = turnovers

    @staticmethod
    def empty(game_id=None):
        return Median(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, game_id=game_id)

    def add_play(self, stat: Stat):
        if stat.free_trow is not None:
            self.free_trow += stat.free_trow
        if stat.failure_free_trow is not None:
            self.failure_free_trow += stat.failure_free_trow
        if stat.two_points is not None:
            self.two_points += stat.two_points
        if stat.failure_two_points is not None:
            self.failure_two_points += stat.failure_two_points
        if stat.tree_points is not None:
            self.tree_points += stat.tree_points
        if stat.failure_tree_points is not None:
            self.failure_tree_points += stat.failure_tree_points
        if stat.assists is not None:
            self.assists += stat.assists
        if stat.steals is not None:
            self.steals += stat.steals
        if stat.rebounds is not None:
            self.rebounds += stat.rebounds
        if stat.blocks is not None:
            self.blocks += stat.blocks
        if stat.falts is not None:
            self.falts += stat.falts
        if stat.turnovers is not None:
            self.turnovers += stat.turnovers

        self.points = self.free_trow + (self.two_points * 2) + (self.tree_points * 3)