from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any, List, Union

# --- Existing Models ---

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
    shortened_url: str

class UUIDResponse(BaseModel):
    uuid: str

class CryptoResponse(BaseModel):
    bitcoin: dict
    ethereum: dict

# --- New Models (Lite) ---

class IPInfoResponse(BaseModel):
    ip: str
    user_agent: Dict[str, Any]
    headers: Dict[str, str]

class PasswordCheckRequest(BaseModel):
    password: str

class PasswordCheckResponse(BaseModel):
    password_hidden: str
    score: int # 0-4
    crack_time_display: str
    feedback: Dict[str, Any]
