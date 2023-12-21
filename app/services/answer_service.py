from fastapi import HTTPException

from app.repositories.question_repository import QuestionRepository
from app.repositories.user_repository import UserRepository


class AnswerService:
    def __init__(self, question_repo: QuestionRepository, user_repo: UserRepository):
        self.question_repo = question_repo
        self.user_repo = user_repo

    def process_answer(self, question_id: str, user_id: str, user_answer: str) -> [bool, int]:
        question = self.question_repo.get_question_by_id(question_id)
        if question is None:
            raise HTTPException(status_code=404, detail="Question not found")

        user = self.user_repo.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        is_correct = question["correctAnswer"] == user_answer

        if is_correct:
            user["score"] += 10
        else:
            user["score"] = max(0, user["score"] - 5)

        self.user_repo.update_user(user_id, user)

        return is_correct, user["score"]
