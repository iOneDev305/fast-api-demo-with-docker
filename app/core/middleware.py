from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "your-api-key-here")

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get("x-api-key")
        if not api_key or api_key != API_KEY:
            raise HTTPException(
                status_code=403,
                detail="Invalid API key"
            )
        response = await call_next(request)
        return response 