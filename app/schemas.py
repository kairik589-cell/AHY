from pydantic import BaseModel, HttpUrl
from typing import Optional

class HashRequest(BaseModel):
    text: str
    algorithm: Optional[str] = "sha256"

class HashResponse(BaseModel):
    text: str
    algorithm: str
    hash: str

class QRRequest(BaseModel):
    data: str

class QRResponse(BaseModel):
    data: str
    base64_image: str

class FormatTextRequest(BaseModel):
    text: str
    action: str  # uppercase, lowercase, slug

class FormatTextResponse(BaseModel):
    original: str
    formatted: str
    action: str

class ShortenUrlRequest(BaseModel):
    url: HttpUrl

class ShortenUrlResponse(BaseModel):
    original_url: HttpUrl
    short_id: str
    shortened_url: str  # For display purposes

class UUIDResponse(BaseModel):
    uuid: str

class CryptoResponse(BaseModel):
    bitcoin: dict
    ethereum: dict
