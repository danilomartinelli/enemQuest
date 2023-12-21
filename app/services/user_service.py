from typing import List
from app.repositories.user_repository import UserRepository
from app.mappers.user_mapper import UserMapper

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, user_data: dict) -> dict:
        new_user = self.repo.create_user(user_data)
        return UserMapper.map_user(new_user)

    def get_all_users(self) -> List[dict]:
        users = self.repo.list_users()
        return [UserMapper.map_user(user) for user in users]

    def get_user_by_id(self, user_id: str) -> dict:
        user = self.repo.get_user_by_id(user_id)
        if user:
            return UserMapper.map_user(user)
        else:
            return None

    def update_user(self, user_id: str, update_data: dict) -> dict:
        updated_user = self.repo.update_user(user_id, update_data)
        if updated_user:
            return UserMapper.map_user(updated_user)
        else:
            return None

    def delete_user(self, user_id: str) -> bool:
        return self.repo.delete_user(user_id)
