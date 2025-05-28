from datetime import datetime


class Game:
    def __init__(self, game_id: str, team: str, adversary: str, date_time: datetime):
        self.id = game_id
        self.team = team
        self.adversary = adversary
        self.date_time = date_time

    @staticmethod
    def from_dict(data: dict) -> 'Game':
        return Game(data['id'], data['team'], data['adversary'], data['date_time'])