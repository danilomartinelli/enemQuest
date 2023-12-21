from pydantic import Field, BaseModel


class UserSchema(BaseModel):
    id: str = Field(None, alias='_id', description="Unique identifier of the user")
    user: str = Field(..., description="Username of the user")
    score: int = Field(0, description="Score of the user")

    class Config:
        schema_extra = {
            "example": {
                "user": "danilo",
                "score": 10
            }
        }
