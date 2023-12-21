from fastapi import APIRouter, Depends, HTTPException

from app.database import get_user_repository
from app.dtos.ranking_response_dto import RankingResponseDto
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter()


def get_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repo)


@router.get("/rankings/{user_id}", response_model=RankingResponseDto)
async def get_ranking_by_user_id(user_id: str, service: UserService = Depends(get_service)):
    ranking = service.get_ranking(user_id)
    if ranking is None:
        raise HTTPException(status_code=404, detail="User not found")
    return ranking
