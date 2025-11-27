from fastapi import FastAPI
from app.routers import shortener
from app.core.middleware import setup_middleware
from app.core.errors import setup_exception_handlers

app = FastAPI(
    title="Vercel URL Shortener",
    description="A simple, serverless URL shortener on Vercel.",
    version="3.0.0"
)

# Setup Core Components
setup_middleware(app)
setup_exception_handlers(app)

# Include Routers
app.include_router(shortener.router)

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Welcome to the URL Shortener. POST to /shorten to create a link."
    }
