from pydantic import Field, BaseModel


class UserAnswerSchema(BaseModel):
    answer: str = Field(..., description="Answer text")

    class Config:
        schema_extra = {
            "example": {
                "answer": "Resposta 1",
            }
        }
