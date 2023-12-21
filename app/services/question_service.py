from typing import List
from app.repositories.question_repository import QuestionRepository
from app.mappers.question_answer_mapper import QuestionAnswerMapper


class QuestionService:
    def __init__(self, repo: QuestionRepository):
        self.repo = repo

    def create_question(self, question_data: dict) -> dict:
        new_question = self.repo.create_question(question_data)
        return QuestionAnswerMapper.map_question(new_question)

    def get_all_questions(self, offset: int, limit: int) -> (List[dict], int):
        questions = self.repo.list_questions(offset, limit)
        total = self.repo.count_questions()

        return [QuestionAnswerMapper.map_question(question) for question in questions], total

    def get_question_by_id(self, question_id: str) -> dict:
        question = self.repo.get_question_by_id(question_id)
        if question:
            return QuestionAnswerMapper.map_question(question)
        else:
            return None

    def update_question(self, question_id: str, update_data: dict) -> dict:
        updated_question = self.repo.update_question(question_id, update_data)
        if updated_question:
            return QuestionAnswerMapper.map_question(updated_question)
        else:
            return None

    def delete_question(self, question_id: str) -> bool:
        return self.repo.delete_question(question_id)
