import unittest
from unittest.mock import Mock

from app.services.answer_service import AnswerService


class TestAnswerService(unittest.TestCase):
    def setUp(self):
        self.question_repo = Mock()
        self.user_repo = Mock()
        self.question_service = AnswerService(self.question_repo, self.user_repo)

    def test_process_answer_correct(self):
        question_id = "question-1"
        user_id = "user-1"
        correct_answer = "answer-1"
        question_data = {
            "_id": question_id,
            "correctAnswer": correct_answer
        }

        self.question_repo.get_question_by_id.return_value = question_data

        self.user_repo.get_user_by_id.return_value = {"_id": user_id, "score": 0}

        user_answer = "answer-1"

        is_correct, new_score = self.question_service.process_answer(question_id, user_id, user_answer)

        self.assertTrue(is_correct)
        self.assertEqual(new_score, 10)

    def test_process_answer_incorrect(self):
        question_id = "question-1"
        user_id = "user-1"
        correct_answer = "answer-1"
        question_data = {
            "_id": question_id,
            "correctAnswer": correct_answer
        }

        self.question_repo.get_question_by_id.return_value = question_data

        initial_score = 0
        self.user_repo.get_user_by_id.return_value = {"_id": user_id, "score": initial_score}

        user_answer = "incorrect-answer"

        is_correct, new_score = self.question_service.process_answer(question_id, user_id, user_answer)

        self.assertFalse(is_correct)
        self.assertEqual(new_score, initial_score)


if __name__ == "__main__":
    unittest.main()
