from celery import shared_task

from api.recommendations.schemas import PollSchema, UserSchema
from api.recommendations.services import get_or_create_user, get_or_create_poll


@shared_task(max_retries=3)
def create_relation(poll_data: dict, user_data: dict):
    poll_data = PollSchema(**poll_data)
    user_data = UserSchema(**user_data)
    user = get_or_create_user(user_data)
    get_or_create_poll(user, poll_data)
