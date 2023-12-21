from fastapi import FastAPI

from app.routes.question_route import router as question_router

app = FastAPI()

app.include_router(question_router, prefix="/api/v1", tags=["questions"])
