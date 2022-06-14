from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime


def generate_id():
    return str(uuid4())


def generate_date():
    return str(datetime.now())


class UserStat(BaseModel):
    id: str = Field(default_factory=generate_id)
    user_email: str
    qty_posts: int = 0
    qty_followers: int = 0
    qty_likes: int = 0
    created_at: str = Field(default_factory=generate_date)
