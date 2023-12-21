from pydantic import BaseModel


class QuestionAnswerResponseDto(BaseModel):
    correct: bool
    new_score: int
