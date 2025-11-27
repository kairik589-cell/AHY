from fastapi import APIRouter, HTTPException, Request
from app.services import tools, qr_service, url_service
from app.schemas import (
    HashRequest, HashResponse,
    UUIDResponse,
    QRRequest, QRResponse,
    FormatTextRequest, FormatTextResponse,
    ShortenUrlRequest, ShortenUrlResponse
)
from app.core.schemas import ResponseModel

router = APIRouter()

@router.get("/hash", response_model=ResponseModel[HashResponse])
@router.post("/hash", response_model=ResponseModel[HashResponse])
async def hash_text(data: HashRequest = None, text: str = None, algorithm: str = "sha256"):
    # Allow both GET (query params) and POST (body)
    if data:
        target_text = data.text
        target_algo = data.algorithm
    elif text:
        target_text = text
        target_algo = algorithm
    else:
        raise HTTPException(status_code=400, detail="Text is required")

    try:
        result = tools.generate_hash(target_text, target_algo)
        return ResponseModel(
            status="success",
            data=HashResponse(text=target_text, algorithm=target_algo, hash=result)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/uuid", response_model=ResponseModel[UUIDResponse])
async def get_uuid():
    return ResponseModel(
        status="success",
        data=UUIDResponse(uuid=tools.generate_uuid())
    )

@router.post("/qr", response_model=ResponseModel[QRResponse])
async def create_qr(request: QRRequest):
    try:
        base64_img = qr_service.generate_qr_base64(request.data)
        return ResponseModel(
            status="success",
            data=QRResponse(data=request.data, base64_image=f"data:image/png;base64,{base64_img}")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/format-text", response_model=ResponseModel[FormatTextResponse])
async def format_text_endpoint(request: FormatTextRequest):
    try:
        formatted = tools.format_text(request.text, request.action)
        return ResponseModel(
            status="success",
            data=FormatTextResponse(original=request.text, formatted=formatted, action=request.action)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/shorten-url", response_model=ResponseModel[ShortenUrlResponse])
async def shorten_url_endpoint(request: ShortenUrlRequest, req: Request): # req needed to build full url if we wanted
    try:
        short_id = url_service.shorten_url(str(request.url))
        # Construct a theoretical full URL (even if we don't have a redirect endpoint exposed in this specific spec,
        # it's good practice to show what it would look like, or just return the ID)
        # User asked for "shorten-url", implied getting a short URL back.
        # Since we are serverless, we can return the ID.
        return ResponseModel(
            status="success",
            data=ShortenUrlResponse(
                original_url=request.url,
                short_id=short_id,
                shortened_url=f"/{short_id}" # Placeholder relative path
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
