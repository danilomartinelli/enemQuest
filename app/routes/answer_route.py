from fastapi import APIRouter, HTTPException, Depends, Header

from app.dtos.question_answer_request_dto import QuestionAnswerRequestDto
from app.repositories.user_repository import UserRepository
from app.repositories.question_repository import QuestionRepository
from app.database import get_question_repository, get_user_repository
from app.services.answer_service import AnswerService

router = APIRouter()


def get_service(
        question_repo: QuestionRepository = Depends(get_question_repository),
        user_repo: UserRepository = Depends(get_user_repository)
) -> AnswerService:
    return AnswerService(question_repo, user_repo)


@router.post("/questions/{question_id}/answer")
async def send_answer(
        question_id: str,
        user_answer: QuestionAnswerRequestDto,
        user_id: str = Header(..., description="User ID"),
        service: AnswerService = Depends(get_service)
):
    is_correct, new_score = service.process_answer(question_id, user_id, user_answer.answer)

    return {"correct": is_correct, "new_score": new_score}
