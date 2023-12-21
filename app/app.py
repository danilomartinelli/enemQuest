from fastapi import FastAPI

from app.routes.question_route import router as question_router
from app.routes.user_route import router as user_router
from app.routes.answer_route import router as answer_router
from app.routes.ranking_route import router as ranking_router

app = FastAPI()

app.include_router(question_router, prefix="/api/v1", tags=["questions"])
app.include_router(user_router, prefix="/api/v1", tags=["users"])
app.include_router(answer_router, prefix="/api/v1", tags=["answers"])
app.include_router(ranking_router, prefix="/api/v1", tags=["rankings"])
