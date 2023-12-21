from typing import List
from fastapi import APIRouter, HTTPException, status, Depends, Header, Query

from app.dtos.question_answer_request_dto import QuestionAnswerRequestDto
from app.dtos.question_answer_response_dto import QuestionAnswerResponseDto
from app.models.question import QuestionSchema
from app.services.question_service import QuestionService
from app.repositories.question_repository import QuestionRepository
from app.database import get_question_repository

router = APIRouter()


def get_service(repo: QuestionRepository = Depends(get_question_repository)) -> QuestionService:
    return QuestionService(repo)


@router.post("/questions/", response_model=QuestionSchema, status_code=status.HTTP_201_CREATED)
async def create_question(question: QuestionSchema, service: QuestionService = Depends(get_service)):
    new_question = service.create_question(question.model_dump())
    if new_question is None:
        raise HTTPException(status_code=400, detail="Error creating question")
    return new_question


@router.get("/questions/", response_model=List[QuestionSchema])
async def read_all_questions(service: QuestionService = Depends(get_service),
                             page: int = Query(1, description="Page number", ge=1),
                             items_per_page: int = Query(10, description="Items per page", ge=1)):
    offset = (page - 1) * items_per_page

    questions = service.get_all_questions(offset, items_per_page)

    return questions


@router.get("/questions/{question_id}", response_model=QuestionSchema)
async def read_question(question_id: str, service: QuestionService = Depends(get_service)):
    question = service.get_question_by_id(question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@router.put("/questions/{question_id}", response_model=QuestionSchema)
async def update_question(question_id: str, question_update: QuestionSchema,
                          service: QuestionService = Depends(get_service)):
    updated_question = service.update_question(question_id, question_update.model_dump())
    if updated_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return updated_question


@router.delete("/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_question(question_id: str, service: QuestionService = Depends(get_service)):
    success = service.delete_question(question_id)
    if not success:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}
