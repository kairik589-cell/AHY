# Serverless URL Shortener

A lightweight URL shortener API designed for Vercel.

**Note:** This uses in-memory storage. Links will vanish when the serverless instance sleeps/restarts.

## Features

- **Create Short Link:** POST `/shorten`
- **Redirect:** GET `/{short_id}`
- **Serverless:** Optimized for Vercel with `Mangum`.

## API Usage

### 1. Shorten a URL
**Request:**
```bash
curl -X POST "https://your-app.vercel.app/shorten" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.google.com"}'
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "original_url": "https://www.google.com/",
    "short_id": "AbCd12",
    "shortened_url": "https://your-app.vercel.app/AbCd12"
  }
}
```

### 2. Access Short Link
Open `https://your-app.vercel.app/AbCd12` in your browser.

## Deployment

1.  **Install Vercel CLI:** `npm i -g vercel`
2.  **Deploy:** `vercel`
