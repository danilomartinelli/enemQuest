class UserMapper:
    @staticmethod
    def map_user(user: dict) -> dict:
        return {
            "_id": str(user["_id"]) if "_id" in user else None,
            "user": user["user"],
            "score": user["score"]
        }
