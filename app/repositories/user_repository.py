from bson import ObjectId
from pymongo.collection import Collection


class UserRepository:
    def __init__(self, db):
        self.collection: Collection = db['user_collection']

    def create_user(self, user_data: dict) -> dict:
        result = self.collection.insert_one(user_data)
        return self.collection.find_one({'_id': result.inserted_id})

    def get_user_by_id(self, user_id: str) -> dict:
        oid = ObjectId(user_id)
        return self.collection.find_one({'_id': oid})

    def update_user(self, user_id: str, update_data: dict) -> dict:
        oid = ObjectId(user_id)
        self.collection.update_one({'_id': oid}, {'$set': update_data})
        return self.collection.find_one({'_id': oid})

    def delete_user(self, user_id: str) -> bool:
        oid = ObjectId(user_id)
        result = self.collection.delete_one({'_id': oid})
        return result.deleted_count > 0

    def list_users(self) -> list:
        return list(self.collection.find())
