from fastapi import FastAPI
from app.routers import utils, crypto, network, media, security
from app.core.middleware import setup_middleware
from app.core.errors import setup_exception_handlers

app = FastAPI(
    title="Vercel Serverless API",
    description="A modular FastAPI project ready for Vercel deployment.",
    version="2.0.0"
)

# Setup Core Components
setup_middleware(app)
setup_exception_handlers(app)

# Include Routers
app.include_router(utils.router, tags=["Utils"])
app.include_router(crypto.router, tags=["Crypto"])
app.include_router(network.router, tags=["Network"])
app.include_router(media.router, tags=["Media"])
app.include_router(security.router, tags=["Security"])

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Welcome to the Vercel Serverless API. Check /docs for documentation."
    }
