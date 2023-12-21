from pydantic import Field, BaseModel


class QuestionAnswerRequestDto(BaseModel):
    answer: str = Field(..., description="Answer text")
