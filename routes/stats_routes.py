from fastapi import APIRouter, Request

from models.dtos.add_play_dto import AddPlayDto
from services.stats_service import StatsService

router = APIRouter(prefix="/stats")

@router.get("/{player_id}")
async def get_player_stats(player_id: str, request: Request):
    stats_service: StatsService = request.app.state.injector[StatsService]

    return await stats_service.get_player_stats(player_id)

@router.get("/medians/{player_id}")
async def get_player_medians(player_id: str, request: Request):
    stats_service: StatsService = request.app.state.injector[StatsService]

    return await stats_service.get_player_medians(player_id)

@router.post("/play/{player_id}", status_code=201)
async def add_play(player_id: str, play: AddPlayDto, request: Request):
    stats_service: StatsService = request.app.state.injector[StatsService]

    return await stats_service.add_play(player_id, play)