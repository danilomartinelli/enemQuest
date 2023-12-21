from typing import List
from fastapi import APIRouter, HTTPException, status, Depends

from app.models.user import UserSchema
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.database import get_user_repository

router = APIRouter()


def get_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repo)


@router.post("/users/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserSchema, service: UserService = Depends(get_service)):
    new_user = service.create_user(user.model_dump())
    if new_user is None:
        raise HTTPException(status_code=400, detail="Error creating user")
    return new_user


@router.get("/users/", response_model=List[UserSchema])
async def read_all_users(service: UserService = Depends(get_service)):
    users = service.get_all_users()
    return users


@router.get("/users/{user_id}", response_model=UserSchema)
async def read_user(user_id: str, service: UserService = Depends(get_service)):
    user = service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=UserSchema)
async def update_user(user_id: str, user_update: UserSchema,
                      service: UserService = Depends(get_service)):
    updated_user = service.update_user(user_id, user_update.model_dump())
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, service: UserService = Depends(get_service)):
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
