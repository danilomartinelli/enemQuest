from typing import List
from app.repositories.question_repository import QuestionRepository
from app.mappers.question_answer_mapper import QuestionAnswerMapper
from app.repositories.user_repository import UserRepository


class QuestionService:
    def __init__(self, question_repo: QuestionRepository, user_repo: UserRepository):
        self.question_repo = question_repo
        self.user_repo = user_repo

    def create_question(self, question_data: dict) -> dict:
        new_question = self.question_repo.create_question(question_data)
        return QuestionAnswerMapper.map_question(new_question)

    def get_all_questions(self) -> List[dict]:
        questions = self.question_repo.list_questions()
        return [QuestionAnswerMapper.map_question(question) for question in questions]

    def get_question_by_id(self, question_id: str) -> dict:
        question = self.question_repo.get_question_by_id(question_id)
        if question:
            return QuestionAnswerMapper.map_question(question)
        else:
            return None

    def update_question(self, question_id: str, update_data: dict) -> dict:
        updated_question = self.question_repo.update_question(question_id, update_data)
        if updated_question:
            return QuestionAnswerMapper.map_question(updated_question)
        else:
            return None

    def delete_question(self, question_id: str) -> bool:
        return self.question_repo.delete_question(question_id)
