import os

from pymongo import MongoClient

from app.repositories.question_repository import QuestionRepository


def get_db_connection():
    mongo_details = os.getenv('MONGO_DETAILS', 'mongodb://root:password@localhost:27017/enem_quest')
    client = MongoClient(mongo_details)
    return client['enem_quest']


def get_question_repository():
    db = get_db_connection()
    return QuestionRepository(db)
