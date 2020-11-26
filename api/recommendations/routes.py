from typing import List

from fastapi import APIRouter

from api.recommendations.schemas import PollSchema
from api.recommendations.services import get_recommended_polls

router = APIRouter()


@router.get("/{user_id}", response_model=List[PollSchema])
async def get_recommended_polls_route(user_id: int):
    return get_recommended_polls(user_id)
