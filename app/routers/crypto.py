from fastapi import APIRouter, HTTPException
from app.services import crypto_service
from app.schemas import CryptoResponse
from app.core.schemas import ResponseModel

router = APIRouter()

@router.get("/crypto-price", response_model=ResponseModel[CryptoResponse])
async def get_crypto_prices():
    try:
        data = crypto_service.get_crypto_prices()
        return ResponseModel(
            status="success",
            data=CryptoResponse(
                bitcoin=data.get("bitcoin", {}),
                ethereum=data.get("ethereum", {})
            )
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
