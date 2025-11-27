from pydantic import BaseModel, HttpUrl

class ShortenUrlRequest(BaseModel):
    url: HttpUrl

class ShortenUrlResponse(BaseModel):
    original_url: HttpUrl
    short_id: str
    shortened_url: str
