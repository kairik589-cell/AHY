from fastapi import APIRouter, HTTPException
from app.services import security_service
from app.schemas import PasswordCheckRequest, PasswordCheckResponse
from app.core.schemas import ResponseModel

router = APIRouter()

@router.post("/password-check", response_model=ResponseModel[PasswordCheckResponse])
async def check_password(request: PasswordCheckRequest):
    try:
        data = security_service.check_password_strength(request.password)
        # Mask password for response safety
        masked = "*" * len(request.password)
        return ResponseModel(
            status="success",
            data=PasswordCheckResponse(
                password_hidden=masked,
                score=data['score'],
                crack_time_display=data['crack_time_display'],
                feedback=data['feedback']
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
