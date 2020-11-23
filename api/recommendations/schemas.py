from typing import Optional

from core.schemas import CamelModel


class UserSchema(CamelModel):
    user_id: int

    class Config:
        orm_mode = True


class PollSchema(CamelModel):
    poll_id: int
    image: Optional[str] = None
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class RelationSchema(CamelModel):
    poll: PollSchema
    user: UserSchema
