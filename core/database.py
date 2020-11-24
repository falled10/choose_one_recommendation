from py2neo import Graph
from py2neo.ogm import Repository

from core.settings import NEO4J_AUTH, DATABASE_HOST, DATABASE_PORT


settings = dict(user_agent="bolt+s",
                auth=NEO4J_AUTH.split('/'), host=DATABASE_HOST, port=DATABASE_PORT)

graph = Graph(**settings)


repo = Repository(**settings)
