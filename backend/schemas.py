from pydantic import BaseModel

# Define the Pydantic schema for creating a URL
class URLCreate(BaseModel):
    full_url: str

# Define the Pydantic schema for returning a URL after post
class URLReturn(BaseModel):
    full_url: str
    short_url: str

class GetUrlRequest(BaseModel):
    full_url: str