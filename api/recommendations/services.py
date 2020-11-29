from py2neo import Relationship

from api.recommendations.schemas import UserSchema, PollSchema
from api.recommendations.models import User, Poll
from core.database import graph


def get_or_create_user(user_data: UserSchema):
    user = User.match(graph, user_data.user_id).first()
    if not user:
        user = User()
        user.user_id = user_data.user_id
        graph.push(user)
    return user


def get_or_create_poll(user: User, poll_data: PollSchema):
    poll = Poll.match(graph, poll_data.poll_id).first()
    tx = graph.begin()
    if not poll:
        poll = Poll()
        poll.id = poll_data.id
        poll.title = poll_data.title
        poll.image = poll_data.image
        poll.description = poll_data.description
        poll.slug = poll_data.slug
        poll.media_type = poll_data.media_type
        tx.create(poll)
    query = "RETURN EXISTS("\
            "(:User {user_id: $user_id})-"\
            "[:PASSED]-(:Poll {poll_id: $poll_id}))"
    relation_exists = graph.run(query, user_id=user.user_id, poll_id=poll_data.poll_id).evaluate()
    if not relation_exists:
        tx.create(Relationship(user.__node__, 'PASSED', poll.__node__))
        tx.create(Relationship(poll.__node__, 'PASSED_BY', user.__node__))
    tx.commit()
    return poll


def get_recommended_polls(user_id: int) -> list:
    query = "MATCH (u:User {user_id: $user_id})"\
            "-[:PASSED]->(:Poll)<-[:PASSED]-(o:User) "\
            "MATCH (o:User)<-[:PASSED*1..5]->(rec:Poll) "\
            "WHERE NOT EXISTS((u)-[:PASSED]->(rec)) RETURN DISTINCT rec"
    data = graph.run(query, user_id=user_id).data()
    return [poll['rec'] for poll in data]
