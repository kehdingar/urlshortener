from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from urllib.parse import urlparse
from enum import Enum
from app.utils import validate_url_format


class TaskStatus(str, Enum):
    completed = "completed"
    pending = "pending"

# url base
class URLBase(BaseModel):
    full_url: str

    @field_validator("full_url")
    def validate_url(cls, v):
        validate_url_format(v)
        return v        

# creating a URL
class URLCreate(URLBase):
    pass

# returning a URL after post
class URLReturn(BaseModel):
    full_url: str
    short_url: str
    status: TaskStatus


class GetUrlRequest(URLBase):
    pass