class QuestionAnswerMapper:
    @staticmethod
    def map_question(question: dict) -> dict:
        return {
            "_id": str(question["_id"]) if "_id" in question else None,
            "statement": question["statement"],
            "subject": question["subject"],
            "answers": [QuestionAnswerMapper.map_answer(answer) for answer in question["answers"]],
            "correctAnswer": question["correctAnswer"],
        }

    @staticmethod
    def map_answer(answer: dict) -> dict:
        return {
            "text": answer["text"],
        }
