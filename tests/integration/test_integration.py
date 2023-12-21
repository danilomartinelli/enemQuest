import pytest
from mongomock import MongoClient
from app.repositories.question_repository import QuestionRepository
from app.services.question_service import QuestionService


@pytest.fixture(scope="module")
def test_db():
    client = MongoClient()
    yield client
    client.close()


@pytest.fixture(scope="module")
def test_question_repository(test_db):
    db = test_db.test_database
    return QuestionRepository(db)


@pytest.fixture(scope="module")
def test_question_service(test_question_repository):
    return QuestionService(test_question_repository)


def test_integration_question_service(test_question_service):
    question_data = {
        "statement": "Test question",
        "subject": "Test subject",
        "answers": [{"text": "Test answer 1"}, {"text": "Test answer 2"}],
        "correctAnswer": "Test answer 1",
    }

    new_question = test_question_service.create_question(question_data)

    retrieved_question = test_question_service.get_question_by_id(str(new_question["_id"]))

    del retrieved_question['_id']
    del question_data['_id']

    assert retrieved_question == question_data
