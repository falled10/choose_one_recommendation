from celery import shared_task

from api.recommendations.schemas import PollSchema, UserSchema
from api.recommendations.services import get_or_create_user, get_or_create_poll
from core.loggers import celery_logger


@shared_task(max_retries=3)
def create_relation(poll_data: dict, user_data: dict):
    try:
        poll_data = PollSchema(**poll_data)
        user_data = UserSchema(**user_data)
        user = get_or_create_user(user_data)
        poll = get_or_create_poll(user, poll_data)
        celery_logger.info(f"Created relation between poll with id "
                           f"{poll.poll_id} and user with id {user.user_id}")
    except Exception as e:
        celery_logger.error(e)
