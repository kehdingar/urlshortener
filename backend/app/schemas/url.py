from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from urllib.parse import urlparse

# url base
class URLBase(BaseModel):
    full_url: str

    @field_validator("full_url")
    def validate_url(cls, v):
        try:
            parsed_url = urlparse(v)
            # Check if the scheme is valid
            if parsed_url.scheme not in ("http", "https"):
                raise HTTPException(status_code=422, detail="URL must have a valid scheme (http/https)")
            # Check if the domain contains a dot (.)
            if "." not in parsed_url.netloc:
                raise HTTPException(status_code=422, detail="Invalid URL format: missing dot in domain")
        except ValueError as e:
            raise HTTPException(status_code=422, detail="Invalid URL format") from e
        return v

# creating a URL
class URLCreate(URLBase):
    pass

# returning a URL after post
class URLReturn(URLBase):
    short_url: str

class GetUrlRequest(URLBase):
    pass