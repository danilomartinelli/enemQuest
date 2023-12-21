from typing import List

from pydantic import Field, BaseModel

from app.models.answer import AnswerSchema


class QuestionSchema(BaseModel):
    id: str = Field(None, alias='_id', description="Unique identifier of the question")
    statement: str = Field(..., description="Question statement")
    subject: str = Field(..., description="The subject of the")
    answers: List[AnswerSchema] = Field(..., description="List of answers")
    correctAnswer: str = Field(..., description="The text of the correct answer")

    class Config:
        schema_extra = {
            "example": {
                "statement": "Questão 01",
                "subject": "Área 01",
                "answers": [
                    {"text": "Answer 1"},
                    {"text": "Answer 2"},
                    {"text": "Answer 3"}
                ],
                "correctAnswer": "Answer 2"
            }
        }
