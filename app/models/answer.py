from pydantic import Field, BaseModel


class AnswerSchema(BaseModel):
    text: str = Field(..., description="Answer text")

    class Config:
        schema_extra = {
            "example": {
                "text": "Resposta 1",
            }
        }
