from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
from .config import Config

def create_app():
    app = FastAPI(
        title="LinguaMate",
        version="0.1",
        description="Learn English with a AI chatbot.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=Config.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)
    return app