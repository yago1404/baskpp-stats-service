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
    def empty():
        return Median(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
