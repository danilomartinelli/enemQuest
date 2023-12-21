from typing import List, TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T")


class PaginatedDto(Generic[T], BaseModel):
    data: List[T]
    total: int
