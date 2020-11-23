from fastapi import HTTPException, status
from py2neo import Relationship

from api.recommendations.schemas import UserSchema, PollSchema
from api.recommendations.models import User, Poll
from core.database import graph


def create_user(user_data: UserSchema):
    graph.run("create database test_database")
    graph.run(":use test_database")
    user = User()
    user.user_id = user_data.user_id
    graph.push(user)
    return user


def create_poll(user_id: int, poll_data: PollSchema):
    user = User.match(graph, user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"User with id '{user_id}' does not exists!")
    tx = graph.begin()
    poll = Poll()
    poll.poll_id = poll_data.poll_id
    poll.title = poll_data.title
    poll.image = poll_data.image
    poll.description = poll_data.description
    tx.create(poll)
    tx.create(Relationship(user.__node__, 'PASSED', poll.__node__))
    tx.create(Relationship(poll.__node__, 'PASSED_BY', user.__node__))
    tx.commit()
    return poll
