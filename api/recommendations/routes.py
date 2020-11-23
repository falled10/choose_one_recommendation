from typing import List

from fastapi import APIRouter

from api.recommendations.schemas import RelationSchema, PollSchema
from api.recommendations.services import create_relation, get_recommended_polls

router = APIRouter()


@router.post("", response_model=RelationSchema)
async def create_relation_route(relation_data: RelationSchema):
    return create_relation(relation_data.poll, relation_data.user)


@router.get("/{user_id}", response_model=List[PollSchema])
async def get_recommended_polls_route(user_id: int):
    return get_recommended_polls(user_id)
