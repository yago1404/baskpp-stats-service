from fastapi import APIRouter, Request

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