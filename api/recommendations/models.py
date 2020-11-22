from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo


class Poll(GraphObject):
    __primarykey__ = "poll_id"

    poll_id = Property()

    image = Property()
    title = Property()
    description = Property()

    users = RelatedFrom("User", "PASSED")


class User(GraphObject):
    __primarykey__ = "user_id"

    user_id = Property()

    passed = RelatedTo(Poll)
