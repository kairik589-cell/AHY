from fastapi import FastAPI
from app.routers import utils, crypto
from app.core.middleware import setup_middleware
from app.core.errors import setup_exception_handlers

app = FastAPI(
    title="Vercel Serverless API",
    description="A modular FastAPI project ready for Vercel deployment.",
    version="1.0.0"
)

# Setup Core Components
setup_middleware(app)
setup_exception_handlers(app)

# Include Routers
app.include_router(utils.router)
app.include_router(crypto.router)

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Welcome to the Vercel Serverless API. Check /docs for documentation."
    }
