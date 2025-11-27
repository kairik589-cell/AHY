from fastapi import FastAPI
from app.routers import utils, crypto, network, security
from app.core.middleware import setup_middleware
from app.core.errors import setup_exception_handlers

app = FastAPI(
    title="Vercel Serverless API Lite",
    description="A lightweight, modular FastAPI project optimized for Vercel.",
    version="2.1.0"
)

# Setup Core Components
setup_middleware(app)
setup_exception_handlers(app)

# Include Routers
app.include_router(utils.router, tags=["Utils"])
app.include_router(crypto.router, tags=["Crypto"])
app.include_router(network.router, tags=["Network"])
app.include_router(security.router, tags=["Security"])

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Welcome to the Vercel Serverless API Lite."
    }
