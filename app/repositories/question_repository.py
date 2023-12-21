from bson import ObjectId
from pymongo.collection import Collection


class QuestionRepository:
    def __init__(self, db):
        self.collection: Collection = db['question_collection']

    def create_question(self, question_data: dict) -> dict:
        result = self.collection.insert_one(question_data)
        return self.collection.find_one({'_id': result.inserted_id})

    def get_question_by_id(self, question_id: str) -> dict:
        oid = ObjectId(question_id)
        return self.collection.find_one({'_id': oid})

    def update_question(self, question_id: str, update_data: dict) -> dict:
        oid = ObjectId(question_id)
        self.collection.update_one({'_id': oid}, {'$set': update_data})
        return self.collection.find_one({'_id': oid})

    def delete_question(self, question_id: str) -> bool:
        oid = ObjectId(question_id)
        result = self.collection.delete_one({'_id': oid})
        return result.deleted_count > 0

    def list_questions(self) -> list:
        return list(self.collection.find())
