import uvicorn
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from app import create_app
from app.config import Config

app = create_app()

# Global exception handler untuk exception umum
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc):
    logging.exception("Unhandled exception: %s", exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error."},
    )

# Daftarkan exception handler untuk RateLimitExceeded secara global
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Please try again later."},
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=Config.DEBUG)
