from pydantic import BaseModel


class QuestionAnswerResponseDto(BaseModel):
    correct: bool
