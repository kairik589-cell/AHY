from fastapi import APIRouter, Request
from app.services import network_service
from app.schemas import IPInfoResponse
from app.core.schemas import ResponseModel

router = APIRouter()

@router.get("/my-ip", response_model=ResponseModel[IPInfoResponse])
async def my_ip_info(request: Request):
    # Detect IP
    ip = request.client.host
    if "x-forwarded-for" in request.headers:
        ip = request.headers["x-forwarded-for"]

    # Parse User Agent
    ua_string = request.headers.get("user-agent", "")
    ua_data = network_service.parse_user_agent(ua_string)

    return ResponseModel(
        status="success",
        data=IPInfoResponse(
            ip=ip,
            user_agent=ua_data,
            headers={k: v for k, v in request.headers.items() if k.lower() in ["x-vercel-ip-country", "x-vercel-ip-city", "host"]}
        )
    )
