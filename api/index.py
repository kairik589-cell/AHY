from mangum import Mangum
from app.main import app

# lifespan="off" is critical for Vercel serverless environment compatibility
# to prevent timeout or event loop issues during startup/shutdown.
handler = Mangum(app, lifespan="off")
