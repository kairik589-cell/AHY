from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
from app.services import url_service
from app.schemas import ShortenUrlRequest, ShortenUrlResponse
from app.core.schemas import ResponseModel

router = APIRouter()

@router.post("/shorten", response_model=ResponseModel[ShortenUrlResponse])
async def shorten_url(request: ShortenUrlRequest, req: Request):
    try:
        short_id = url_service.shorten_url(str(request.url))
        # Build the full short URL based on the current request host
        base_url = str(req.base_url).rstrip("/")
        shortened_url = f"{base_url}/{short_id}"

        return ResponseModel(
            status="success",
            data=ShortenUrlResponse(
                original_url=request.url,
                short_id=short_id,
                shortened_url=shortened_url
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{short_id}")
async def redirect_url(short_id: str):
    original_url = url_service.get_original_url(short_id)
    if original_url:
        return RedirectResponse(url=original_url)
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")
