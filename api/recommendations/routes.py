from fastapi import APIRouter

from api.recommendations.schemas import UserSchema, PollSchema
from api.recommendations.services import create_user, create_poll

router = APIRouter()


@router.post('/users', response_model=UserSchema)
async def create_user_route(user_data: UserSchema):
    return create_user(user_data)


@router.post('/users/{user_id}/polls', response_model=PollSchema)
async def create_poll_route(poll_data: PollSchema, user_id: int):
    return create_poll(user_id, poll_data)
