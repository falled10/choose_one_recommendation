from typing import Optional

from core.schemas import CamelModel


class UserSchema(CamelModel):
    user_id: int

    class Config:
        orm_mode = True


class PollSchema(CamelModel):
    id: int
    image: Optional[str] = None
    title: str
    media_type: Optional[str] = None
    description: Optional[str] = None
    slug: str

    class Config:
        orm_mode = True


class RelationSchema(CamelModel):
    poll: PollSchema
    user: UserSchema
