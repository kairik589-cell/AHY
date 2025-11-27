from fastapi import APIRouter, HTTPException, Request
from app.services import network_service
from app.schemas import WhoisRequest, WhoisResponse, IPInfoResponse
from app.core.schemas import ResponseModel

router = APIRouter()

@router.post("/whois", response_model=ResponseModel[WhoisResponse])
async def whois_lookup(request: WhoisRequest):
    try:
        data = network_service.lookup_whois(request.domain)
        return ResponseModel(
            status="success",
            data=WhoisResponse(domain=request.domain, data=data)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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
