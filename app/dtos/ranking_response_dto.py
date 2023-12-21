from pydantic import BaseModel


class RankingResponseDto(BaseModel):
    score: int
    title: str
