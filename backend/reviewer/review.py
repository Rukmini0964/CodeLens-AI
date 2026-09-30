from backend.llm.chains import review_code


class CodeReviewer:

    @staticmethod
    def review(language: str, code: str):

        return review_code(
            language=language,
            code=code
        )