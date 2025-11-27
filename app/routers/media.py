from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services import media_service
from app.schemas import YTInfoRequest, YTInfoResponse, ExifResponse
from app.core.schemas import ResponseModel

router = APIRouter()

@router.post("/yt-info", response_model=ResponseModel[YTInfoResponse])
async def youtube_info(request: YTInfoRequest):
    try:
        data = media_service.get_youtube_info(request.url)
        return ResponseModel(
            status="success",
            data=YTInfoResponse(**data)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/exif-data", response_model=ResponseModel[ExifResponse])
async def extract_exif(file: UploadFile = File(...)):
    try:
        content = await file.read()
        exif_data = media_service.get_exif_data(content)
        return ResponseModel(
            status="success",
            data=ExifResponse(filename=file.filename, exif_data=exif_data)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
