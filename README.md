# FastAPI Serverless API on Vercel

This is a complete, modular FastAPI project designed to be deployed as a serverless function on Vercel. It includes a variety of utility endpoints, strict method handling, and standardized JSON responses.

## Features

- **Serverless Ready:** Configured with `Mangum` and `vercel.json` for immediate deployment.
- **Modular Structure:** Clean separation of concerns (`app/routers`, `app/services`, `app/core`).
- **Standardized Responses:** All endpoints return `{ "status": "success", "data": { ... } }`.
- **Method Restriction:** Middleware blocks any method other than GET or POST.
- **Utilities:**
  - Hashing (SHA256/SHA512)
  - UUID Generation
  - QR Code Generation (Base64)
  - Text Formatting (Uppercase, Lowercase, Slug)
  - Crypto Prices (BTC/ETH via Coingecko)
  - URL Shortener (In-memory, ephemeral)

## Project Structure

```
.
├── api/
│   └── index.py        # Vercel entry point (Mangum handler)
├── app/
│   ├── core/           # Middleware, Error Handlers, Schemas
│   ├── routers/        # API Endpoints
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
    Follow the prompts. The `vercel.json` file handles the configuration.

## Example Requests

### 1. Hash Text (GET/POST)
**Request (GET):**
```bash
curl "http://127.0.0.1:8000/hash?text=hello&algorithm=sha256"
```
**Request (POST):**
```bash
curl -X POST "http://127.0.0.1:8000/hash" \
     -H "Content-Type: application/json" \
     -d '{"text": "hello", "algorithm": "sha512"}'
```

### 2. Generate UUID (GET)
```bash
curl "http://127.0.0.1:8000/uuid"
```

### 3. Generate QR Code (POST)
```bash
curl -X POST "http://127.0.0.1:8000/qr" \
     -H "Content-Type: application/json" \
     -d '{"data": "https://example.com"}'
```

### 4. Get Crypto Prices (GET)
```bash
curl "http://127.0.0.1:8000/crypto-price"
```

### 5. Format Text (POST)
```bash
curl -X POST "http://127.0.0.1:8000/format-text" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello World", "action": "slug"}'
```

### 6. Shorten URL (POST)
```bash
curl -X POST "http://127.0.0.1:8000/shorten-url" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.google.com"}'
```
