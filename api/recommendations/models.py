from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo


class Poll(GraphObject):
    __primarykey__ = "id"

    id = Property()

    image = Property()
    title = Property()
    description = Property()
    slug = Property()
    media_type = Property()

    users = RelatedFrom("User", "PASSED")


class User(GraphObject):
    __primarykey__ = "user_id"

    user_id = Property()

    passed = RelatedTo(Poll)
