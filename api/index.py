from mangum import Mangum
from app.main import app

# lifespan="off" is critical for Vercel serverless environment compatibility
handler = Mangum(app, lifespan="off")
