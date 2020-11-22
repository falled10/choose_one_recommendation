from py2neo import Graph
from py2neo.ogm import Repository


settings = dict(user_agent="bolt+s",
                auth=('neo4j', 'password'), host="localhost")

graph = Graph(**settings)


repo = Repository(**settings)
