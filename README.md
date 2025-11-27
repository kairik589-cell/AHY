# FastAPI Serverless API on Vercel

This is a complete, modular FastAPI project designed to be deployed as a serverless function on Vercel. It includes a variety of utility endpoints, strict method handling, and standardized JSON responses.

**Lite Version:** Optimized for speed and stability. Heavy features (Whois, YouTube, EXIF) have been removed to ensure seamless serverless execution.

## Features

- **Serverless Ready:** Configured with `Mangum` (lifespan="off") for stable Vercel deployment.
- **Modular Structure:** Clean separation of concerns (`app/routers`, `app/services`, `app/core`).
- **Standardized Responses:** All endpoints return `{ "status": "success", "data": { ... } }`.
- **Method Restriction:** Middleware blocks any method other than GET or POST.
- **Utilities:**
  - **Utils:** Hashing (SHA256/SHA512), UUID, QR Code (Base64), Text Format, URL Shortener.
  - **Crypto:** BTC/ETH Prices.
  - **Network:** IP & Device Info (Magic Link).
  - **Security:** Password Strength Checker (Lightweight).

## Project Structure

```
.
├── api/
│   └── index.py        # Vercel entry point (Mangum handler)
├── app/
│   ├── core/           # Middleware, Error Handlers, Schemas
│   ├── routers/        # API Endpoints (utils, crypto, network, security)
│   ├── services/       # Business Logic
│   ├── schemas.py      # Pydantic Models
│   └── main.py         # App Initialization
├── requirements.txt    # Dependencies
└── vercel.json         # Vercel Configuration
```

## Running Locally

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Server:**
    ```bash
    uvicorn app.main:app --reload
    ```

3.  **Access Documentation:**
    Open `http://127.0.0.1:8000/docs` to see the interactive Swagger UI.

## Deployment to Vercel

1.  **Install Vercel CLI** (optional, or use the web dashboard):
    ```bash
    npm i -g vercel
    ```

2.  **Deploy:**
    ```bash
    vercel
    ```

## Example Requests

### 1. Hash Text (GET/POST)
```bash
curl "http://127.0.0.1:8000/hash?text=hello&algorithm=sha256"
```

### 2. My IP & Device Info (GET)
```bash
curl "http://127.0.0.1:8000/my-ip"
```

### 3. Generate QR Code (POST)
```bash
curl -X POST "http://127.0.0.1:8000/qr" \
     -H "Content-Type: application/json" \
     -d '{"data": "https://vercel.com"}'
```

### 4. Password Strength (POST)
```bash
curl -X POST "http://127.0.0.1:8000/password-check" \
     -H "Content-Type: application/json" \
     -d '{"password": "MySecretPassword123!"}'
```
