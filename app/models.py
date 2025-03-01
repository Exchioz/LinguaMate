from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    difficulty: Optional[str] = Field("beginner", pattern="^(beginner|intermediate|advance)$")
    style: Optional[str] = Field("formal", pattern="^(formal|semi-formal|non-formal)$")
    evaluate: Optional[bool] = Field(False)

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "message": "Hello, how are you?",
                    "difficulty": "beginner",
                    "style": "formal",
                    "evaluate": True
                }
            ]
        }
    )
