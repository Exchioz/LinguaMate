import os

class Config:
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    TESTING = os.getenv("TESTING", "False").lower() == "true"
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS","*").split(",")
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    if not OPENAI_API_KEY:
        raise EnvironmentError("Environment variable 'OPENAI_API_KEY' not found.")