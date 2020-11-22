from fastapi import FastAPI

from py2neo import Relationship

from api.recommendations.models import User, Poll
from api.recommendations.schemas import UserSchema, PollSchema
from core.database import repo, graph


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello Friend'}


@app.post('/user')
async def create_user_root(data: UserSchema):
    user = User()
    user.user_id = data.user_id
    graph.push(user)
    print(user)


@app.get('/user/{user_id}', response_model=UserSchema)
async def get_one_user_route(user_id: int):
    user = User.match(repo, user_id).first()
    return user


@app.post('/users/{user_id}/polls', response_model=PollSchema)
async def add_poll_related_to_user_router(poll_data: PollSchema, user_id: int):
    user = User.match(graph, user_id).first()
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


@app.get("/user")
async def get_all_users():
    data = graph.run(
        "MATCH (p:Poll)-[:PASSED_BY]-(u:User) WHERE p.poll_id = $poll_id RETURN u, p", poll_id=2).data()
    print(data)
    return data
