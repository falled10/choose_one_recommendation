from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


class PollSchema(BaseModel):
    poll_id: int
    image: Optional[str] = None
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
