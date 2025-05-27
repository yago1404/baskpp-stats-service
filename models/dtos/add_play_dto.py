from pydantic import BaseModel


class AddPlayDto(BaseModel):
    game_id: str
    court_locate: str
    free_throw: int | None = None
    failure_free_throw: int | None = None
    two_point: int | None = None
    failure_two_point: int | None = None
    three_point: int | None = None
    failure_three_point: int | None = None
    assist: int | None = None
    steal: int | None = None
    rebound: int | None = None
    block: int | None = None
    falt: int | None = None
    turnover: int | None = None