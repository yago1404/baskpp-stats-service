class Stat:
    def __init__(self, id: str, player_id: str, game_id: str, court_locale: str, free_trow: int, failure_free_trow: int,
                 two_points: int, failure_two_points: int, tree_points: int, failure_tree_points: int, assists: int,
                 steals: int, rebounds: int, blocks: int, falts: int, turnovers: int):
        self.id = id
        self.player_id = player_id
        self.game_id = game_id
        self.court_locale = court_locale
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
    def from_dict(data: dict) -> 'Stat':
        return Stat(
            id=data['id'],
            player_id=data['player'],
            game_id=data['game'],
            court_locale=data['court_locate'],
            free_trow=data['free_throw'],
            failure_free_trow=data['failure_free_throw'],
            two_points=data['two_points'],
            failure_two_points=data['failure_two_points'],
            tree_points=data['tree_points'],
            failure_tree_points=data['failure_tree_points'],
            assists=data['assistances'],
            steals=data['steals'],
            rebounds=data['rebounds'],
            blocks=data['blocks'],
            falts=data['falts'],
            turnovers=data['turnovers']
        )
